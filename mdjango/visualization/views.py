from django.shortcuts import render
from PIL import Image
import pyecharts
# Create your views here.


class VisualizationChart:
    def __init__(self, title, data_name, x_axis, y_axis, chart_name):
        self.title = title
        self.data_name = data_name
        self.x_axis = x_axis
        self.y_axis = y_axis
#        self.chart_name = './frontend/src/diagrams/' + chart_name
        self.chart_name = './frontend/dist/static/' + chart_name


    def histogram(self):
        bar = pyecharts.Bar(self.title)
        if '电影票房TOP' in self.title:
            bar.add("", self.x_axis, self.y_axis, xaxis_interval=0, xaxis_rotate=20)
        else:
            bar.add(self.data_name, self.x_axis, self.y_axis)
        save_file_name = self.chart_name + '_bar.png'
        bar.render(path=save_file_name)
        self.zoom_out_image(save_file_name)

    def line(self):
        # line = pyecharts.Line(self.title, width=400, height=200, title_text_size=10)
        line = pyecharts.Line(self.title)
        for (name, y) in zip(self.data_name, self.y_axis):
            # line.add(name, self.x_axis, y, xaxis_label_textsize=8, yaxis_label_textsize=8, legend_text_size=6, legend_pos='40%')
            line.add(name, self.x_axis, y)
        save_file_name = self.chart_name + '_line.png'
        line.render(path=save_file_name)
        self.zoom_out_image(save_file_name)

    def pie(self):
        pie = pyecharts.Pie(self.title)
        pie.add("", self.x_axis, self.y_axis, legend_orient="vertical", legend_pos="left")
        save_file_name = self.chart_name + '_pie.png'
        pie.render(path=save_file_name)
        self.zoom_out_image(save_file_name)

    def word_cloud(self):
        wordcloud = pyecharts.WordCloud(self.title)
        wordcloud.add("", self.x_axis, self.y_axis, shape='diamond')
        save_file_name = self.chart_name + '_wordcloud.png'
        wordcloud.render(path=save_file_name)
        self.zoom_out_image(save_file_name)

    def zoom_out_image(self, filename):
        image = Image.open(filename)
        new_im = image.resize((800, 400), Image.ANTIALIAS)
        image.close()
        new_im.save(filename)




