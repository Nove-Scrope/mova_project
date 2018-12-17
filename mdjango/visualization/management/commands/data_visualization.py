import sys
import getopt
from visualization.models import MovieData
from visualization.views import VisualizationChart
from mova.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('movie-params', nargs='+', type=str)

    def handle(self, *args, **options):
        movie_params = options['movie-params']
        func_selected = str(movie_params[0])
        year = str(movie_params[1])
        quarter = str(movie_params[2])
        month = str(movie_params[3])
        top_x = int(movie_params[4])
        movie_data = MovieData(year, quarter, month, top_x)
        if func_selected == '1':
            movie_data.get_boxoffice_ratio()
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                              movie_data.y_axis, movie_data.chart_name)
            movie_charts.histogram()
        elif func_selected == '2':
            movie_data.get_top_movie()
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                              movie_data.y_axis, movie_data.chart_name)
            movie_charts.histogram()
        elif func_selected == '3':
            movie_data.get_top_actor()
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                              movie_data.y_axis, movie_data.chart_name)
            movie_charts.histogram()
        elif func_selected == '4':
            movie_data.get_boxoffice_trend()
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                              movie_data.y_axis, movie_data.chart_name)
            movie_charts.line()
        elif func_selected == '5':
            movie_data.get_boxoffice_ratio()
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                              movie_data.y_axis, movie_data.chart_name)
            movie_charts.pie()
        elif func_selected == '6':
            movie_data.get_top_movie()
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                              movie_data.y_axis, movie_data.chart_name)
            movie_charts.word_cloud()
        elif func_selected == '7':
            movie_data.get_top_actor()
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                              movie_data.y_axis, movie_data.chart_name)
            movie_charts.word_cloud()
        else:
            print('input error')
