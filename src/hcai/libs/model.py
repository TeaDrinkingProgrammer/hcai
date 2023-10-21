import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from hcai.libs.img import Img
import numpy as np
import shap

class Model:
    def __init__(self):
        self.iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    def test(self):
        plt.switch_backend('agg')
        plot = sns.heatmap(self.iris.corr(numeric_only= True))
        image = Img()
        image.from_figure(plot.get_figure())

        return (self.iris.head().to_records(), self.iris.head(), image)
    def predict(carat: float, x: float, y: float, z: float):
        return 100.0
