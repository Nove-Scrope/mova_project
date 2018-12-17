from django.shortcuts import render
import pyecharts
# Create your views here.


class VisualizationChart:
    def __init__(self, title, data_name, x_axis, y_axis, chart_name):
        self.title = title
        self.data_name = data_name
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.chart_name = './frontend/src/diagrams/' + chart_name

    def histogram(self):
        bar = pyecharts.Bar(self.title)
        if '电影票房TOP' in self.title:
            bar.add("", self.x_axis, self.y_axis, xaxis_interval=0, xaxis_rotate=20)
        else:
            bar.add(self.data_name, self.x_axis, self.y_axis)
        save_file_name = self.chart_name + '_bar.png'
        bar.render(path=save_file_name)

    def line(self):
        line = pyecharts.Line(self.title)
        for (name, y) in zip(self.data_name, self.y_axis):
            line.add(name, self.x_axis, y)
        save_file_name = self.chart_name + '_line.png'
        line.render(path=save_file_name)

    def pie(self):
        pie = pyecharts.Pie(self.title, title_pos='center')
        pie.add("", self.x_axis, self.y_axis, legend_orient="vertical", legend_pos="left")
        save_file_name = self.chart_name + '_pie.png'
        pie.render(path=save_file_name)

    def word_cloud(self):
        wordcloud = pyecharts.WordCloud(self.title)
        wordcloud.add("", self.x_axis, self.y_axis, shape='diamond')
        save_file_name = self.chart_name + '_wordcloud.png'
        wordcloud.render(path=save_file_name)



