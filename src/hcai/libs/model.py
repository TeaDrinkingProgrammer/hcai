import html
import numpy as np
import pickle
import os
# Neccessary for the model
import sklearn
from django.conf import settings
import shap
import matplotlib
class Model:
    def __init__(self):
        def load_model(file_name: str):
            print(os.path.join(settings.MODELS, file_name))
            return pickle.load(open(os.path.join(settings.MODELS, file_name), 'rb'))
        self.random_forest_model = load_model('random_forest_model.sav')
        self.linear_model = load_model('linear_model.sav')
        self.scaler = load_model('scaler.sav')
        self.x_data_summary = load_model("shap/test_data_summary.sav")
        self.rf_explainer_single = shap.KernelExplainer(self.random_forest_model.predict, self.x_data_summary)
        self.linear_explainer_single = shap.KernelExplainer(self.linear_model.predict, self.x_data_summary)
        # rf_explainer_single = shap.KernelExplainer(loaded_model_randomforest.predict, X_test_summary)
    def predict_good(self, carat: float, x: float, y: float, z: float):
        x_input = np.array([carat, x, y, z]).reshape(1, -1)
        x_input = self.scaler.transform(x_input)
        if (carat > 5.01 or x > 10.74 or y > 10.54 or z > 6.98):
            print("Using linear model")
            prediction = self.linear_model.predict(x_input)[0]
            print("Prediction 2: ", prediction)
            return 0 if prediction < 0 else prediction, "linear"
        else:
            print("Using random forest model")
            prediction = self.random_forest_model.predict(x_input)[0]
            return 0 if prediction < 0 else prediction, "rf"
        

    def predict_bad(self, carat: float, x: float, y: float, z: float, fast_sale: bool = False):
        prediction, model_type = self.predict_good(carat, x, y, z)
        if fast_sale:
            return self.mutate_price_by_percentage(prediction, -15), model_type
        else:
            return self.mutate_price_by_percentage(prediction, -10), model_type
    
    def mutate_price_by_percentage(self, price, percentage):
        return price + (price * percentage / 100)

    def shap(self, model_type: str, carat: float, x: float, y: float, z: float):
        x_input = np.array([carat, x, y, z]).reshape(1, -1)
        x_input = self.scaler.transform(x_input)
        print("Model type: ", model_type)
        explainer_single = self.rf_explainer_single if model_type == "rf" else self.linear_explainer_single
        shap_values_single = explainer_single.shap_values(x_input)
        print("---- Features that have positive impact on the prediction ----")
        print(model_type)
        print("Carat", shap_values_single[0, 0])
        print("x", shap_values_single[0, 1])
        print("y", shap_values_single[0, 2])
        print("z", shap_values_single[0, 3])

        force_plot = shap.force_plot(explainer_single.expected_value, shap_values_single[0], feature_names=['karaat', 'x', 'y', 'z'], plot_cmap=['#77dd77', '#f99191'])
        shap_html = f"{shap.getjs()}<section>{force_plot.html()}</section>"
        texts = []

        texts.append(f"De ingevoerde waarde voor karaat drukt de prijs {'naar boven.' if shap_values_single[0, 0] >= 0 else 'naar beneden.'}")
        texts.append(f"De ingevoerde waarde voor x drukt de prijs {'naar boven.' if shap_values_single[0, 1] >= 0 else 'naar beneden.'}")
        texts.append(f"De ingevoerde waarde voor y drukt de prijs {'naar boven.' if shap_values_single[0, 2] >= 0 else 'naar beneden.'}")
        texts.append(f"De ingevoerde waarde voor z drukt de prijs {'naar boven.' if shap_values_single[0, 3] >= 0 else 'naar beneden.'}")
        return shap_html, texts
        # return self._force_plot_html(self.rf_explainer_single.expected_value, self.rf_shap_values_single[0], x_input, ) 
        