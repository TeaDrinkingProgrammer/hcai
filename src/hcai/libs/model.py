import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from hcai.libs.img import Img
import numpy as np
import shap
import pickle
import os
from sklearn.preprocessing import StandardScaler
from django.conf import settings

class Model:
    def __init__(self):
        self.iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
        def load_model(file_name: str):
            print(os.path.join(settings.MODELS, file_name))
            return pickle.load(open(os.path.join(settings.MODELS, file_name), 'rb'))
        self.random_forest_model = load_model('random_forest_model.sav')
        self.linear_model = load_model('linear_model.sav')
        self.scaler = load_model('scaler.sav')
    def test(self):
        plt.switch_backend('agg')
        plot = sns.heatmap(self.iris.corr(numeric_only= True))
        image = Img()
        image.from_figure(plot.get_figure())

        return (self.iris.head().to_records(), self.iris.head(), image)
    def predict_good(self, carat: float, x: float, y: float, z: float):
        x_input = np.array([carat, x, y, z]).reshape(1, -1)
        x_input = self.scaler.transform(x_input)
        if (carat > 5.01 or x > 10.74 or y > 58.9 or z > 31.8):
            print("Using linear model")
            prediction = self.linear_model.predict(x_input)
            return 0 if prediction < 0 else prediction
        else:
            print("Using random forest model")
            prediction = self.random_forest_model.predict(x_input)
            return 0 if prediction < 0 else prediction
        

    def predict_bad(self, carat: float, x: float, y: float, z: float, buy: bool, fast_sale: bool = False):
        prediction = self.predict_good(carat, x, y, z)
        if buy:
            return self.mutate_price_by_percentage(prediction, 10)
        else:
            if fast_sale:
                return self.mutate_price_by_percentage(prediction, -15)
            else:
                return self.mutate_price_by_percentage(prediction, -10)
    
    def mutate_price_by_percentage(price, percentage):
        return price + (price * percentage / 100)