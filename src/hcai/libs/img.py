import base64
from io import BytesIO
import matplotlib.pyplot as plt
from django.utils.html import format_html

class Img():
    def __init__(self):
            self.image = None

    def from_figure(self, input: plt.Figure):
        plot_file = BytesIO()
        input.savefig(plot_file, format='png')
        self.image = base64.b64encode(plot_file.getvalue()).decode()

    def to_html(self):
        return format_html('<img src="data:image/png;base64,{}">', self.image)