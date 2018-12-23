from django.db import models

# Create your models here.
from mova.models import *
from visualization.views import VisualizationChart
from reportlab.pdfgen import canvas
import shutil
import os


def film_out(year, season, month):
    fid = []
    film = []
    if year == '0':
        year = ''
    if month != '0':
        if len(month) == 1:
            month = "0" + month
        select = year + '-' + month
        target = Film.objects.all().values_list('date', 'filmid')
        for item in target:
            item = list(item)
            if item[0].find(select) != -1:
                fid.append(item[1])
    elif month == '0':
        mm = []
        if season == '1':
            mm.append('01')
            mm.append('02')
            mm.append('03')
        elif season == '2':
            mm.append('04')
            mm.append('05')
            mm.append('06')
        elif season == '3':
            mm.append('07')
            mm.append('08')
            mm.append('09')
        elif season == '4':
            mm.append('10')
            mm.append('11')
            mm.append('12')
        else:
            mm.append('')
            mm.append('')
            mm.append('')
        target = Film.objects.all().values_list('date', 'filmid')
        for item in target:
            item = list(item)
            if item[0].find(year +'-'+ mm[0]) != -1 or item[0].find(year +'-'+ mm[1]) != -1 or item[0].find(year +'-'+ mm[2]) != -1:
                fid.append(item[1])
    for item in fid:
        op = {}
        it = Film.objects.get(filmid=item)
        op['name'] = it.name
        op['type'] = it.type
        op['score_rate'] = it.score_rate
        op['score_num'] = it.score_num
        op['date'] = it.date
        op['boxoffice'] = it.boxoffice
        op['day_boxoffice'] = it.day_boxoffice
        op['week_boxoffice'] = it.week_boxoffice
        op['score'] = it.score
        op['actor'] = []
        op['director'] = []
        res = Actor.objects.filter(filmid=item)
        for it in res:
            op['actor'].append(it.name)
        res = Director.objects.filter(filmid=item)
        for it in res:
            op['director'].append(it.name)
        film.append(op)
    return film


class MovieData:
    def __init__(self, year, quarter, month, top_x):
        self.year = year        # year为一表示年份的字符串，下quarter, month同
        self.quarter = quarter
        self.month = month
        self.title = ''
        self.data_name = []
        self.x_axis = []
        self.y_axis = []
        self.top_x = top_x
        self.chart_name = ''

    def get_boxoffice_ratio(self):
        source_data = film_out(self.year, self.quarter, self.month)
        source_theme_list = [x['type'].split(',') for x in source_data]
        source_theme_list = [x for j in source_theme_list for x in j]
        theme_name = list(set(source_theme_list))
        theme_boxoffice = []
        for theme in theme_name:
            boxoffice = [x['boxoffice'] for x in source_data if theme in x['type']]
            boxoffice = int(sum(boxoffice))
            theme_boxoffice.append(boxoffice)
        if len(theme_name) > 10:
            theme_dict = dict(zip(theme_name, theme_boxoffice))
            theme_dict = dict(sorted(theme_dict.items(), key=lambda x: x[1], reverse=True))
            theme_name = list(theme_dict.keys())
            theme_boxoffice = list(theme_dict.values())
            theme_name[10] = '其它'
            theme_boxoffice[10] = sum(theme_boxoffice[10:])
            del theme_name[11:]
            del theme_boxoffice[11:]
        self.x_axis = theme_name
        self.y_axis = theme_boxoffice
        self.title = '历年' if self.year == '0' else self.year+'年'
        if self.month == '0' and self.quarter == '0':
            self.title = self.title
        elif self.month != '0':
            self.title = self.title + self.month + '月'
        else:
            self.title = self.title + '第' + self.quarter + '季度'
        self.title = self.title + '题材票房比例'
        self.data_name = ''
        self.chart_name = 'boxoffice_ratio'

    def get_boxoffice_trend(self):
        boxoffice_list = []
        self.year = sorted([self.year, self.quarter, self.month])
        for year in self.year:
            one_year_boxoffice_list = []
            for month in range(1, 13):
                source_data = film_out(year, '0', str(month))
                source_boxoffice = [x['boxoffice'] for x in source_data]
                one_month_boxoffice = int(sum(source_boxoffice))
                one_year_boxoffice_list.append(one_month_boxoffice)
            boxoffice_list.append(one_year_boxoffice_list)
        self.x_axis = []
        for month in range(1, 13):
            self.x_axis.append(str(month) + '月')
        self.y_axis = boxoffice_list
        self.title = self.year[0]+'年至'+self.year[-1]+'年每月\n电影票房变化趋势(单位：万元)'
        self.data_name = self.year
        self.chart_name = 'boxoffice_trend'

    def get_top_movie(self):
        source_data = film_out(self.year, '0', '0')
        movie_name = [x['name'] for x in source_data]
        movie_boxoffice = [x['boxoffice'] for x in source_data]
        movie_dict = dict(zip(movie_name, movie_boxoffice))
        movie_dict = dict(sorted(movie_dict.items(), key=lambda x: x[1], reverse=True))
        self.x_axis = list(movie_dict.keys())[0:self.top_x]
        self.y_axis = list(movie_dict.values())[0:self.top_x]
        self.title = self.year + '年电影票房TOP' + str(self.top_x)
        self.data_name = ''
        self.chart_name = 'top_movie'

    def get_top_actor(self):
        source_data = film_out(self.year, '0', '0')
        actor = [x['actor'] for x in source_data]
        actor = [x for j in actor for x in j]
        actor_name = list(set(actor))
        appearance_number = [actor.count(x) for x in actor_name]
        actor_dict = dict(zip(actor_name, appearance_number))
        actor_dict = dict(sorted(actor_dict.items(), key=lambda x: x[1], reverse=True))
        self.x_axis = list(actor_dict.keys())[0:self.top_x]
        self.y_axis = list(actor_dict.values())[0:self.top_x]
        self.title = self.year + '年TOP' + str(self.top_x) + '劳模演员'
        self.data_name = ''
        self.chart_name = 'top_actor'


def data_visualization(func_selected, year, quarter, month, top_x):
    data_dict = {}
    movie_data = MovieData(year, quarter, month, top_x)
    if func_selected == '1':
            movie_data.get_boxoffice_ratio()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.histogram()
    elif func_selected == '2':
            movie_data.get_top_movie()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.histogram()
    elif func_selected == '3':
            movie_data.get_top_actor()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.histogram()
    elif func_selected == '4':
            movie_data.get_boxoffice_trend()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.line()
    elif func_selected == '5':
            movie_data.get_boxoffice_ratio()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.pie()
    elif func_selected == '6':
            movie_data.get_top_movie()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.word_cloud()
    elif func_selected == '7':
            movie_data.get_top_actor()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.word_cloud()
    return data_dict

def save_charts_as_pdf(save_charts):
    pdf_pagesize = (600, 300*len(save_charts))
    c = canvas.Canvas("visualization_report.pdf", pagesize=pdf_pagesize)
    cur_pos_in_pdf = 300 * (len(save_charts) - 1)
    chart_file_dict = {
        '1': "boxoffice_ratio_bar.png",
        '2': "top_movie_bar.png",
        '3': "top_actor_bar.png",
        '4': "boxoffice_trend_line.png",
        '5': "boxoffice_ratio_pie.png",
        '6': "top_movie_wordcloud.png",
        '7': "top_actor_wordcloud.png",
    }
    file_path_prefix = './frontend/dist/static/'
    for chart in save_charts:
        c.drawImage(file_path_prefix+chart_file_dict[chart], 25, cur_pos_in_pdf, 550, 275)
        cur_pos_in_pdf -= 300
    c.showPage()
    c.save()
    return 'done'


# opts, args = getopt.getopt(sys.argv[1:], "f:y:q:m:t:")
# func_selected = ''
# year = ''
# quarter = ''
# month = ''
# top_x = 0
# for op, value in opts:
#     if op == '-f':
#         func_selected = value
#     if op == '-y':
#         year = value
#     if op == '-q':
#         quarter = value
#     if op == '-m':
#         month = value
#     if op == '-t':
#         top_x = int(value)
# movie_data = MovieData(year, quarter, month, top_x)
# if func_selected == '1':
#     movie_data.get_boxoffice_ratio()
#     movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis, movie_data.y_axis)
#     movie_charts.histogram()
# elif func_selected == '2':
#     movie_data.get_top_movie()
#     movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis, movie_data.y_axis)
#     movie_charts.histogram()
# elif func_selected == '3':
#     movie_data.get_top_actor()
#     movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis, movie_data.y_axis)
#     movie_charts.histogram()
# elif func_selected == '4':
#     movie_data.get_boxoffice_trend()
#     movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis, movie_data.y_axis)
#     movie_charts.line()
# elif func_selected == '5':
#     movie_data.get_boxoffice_ratio()
#     movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis, movie_data.y_axis)
#     movie_charts.pie()
# elif func_selected == '6':
#     movie_data.get_top_movie()
#     movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis, movie_data.y_axis)
#     movie_charts.word_cloud()
# elif func_selected == '7':
#     movie_data.get_top_actor()
#     movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis, movie_data.y_axis)
#     movie_charts.word_cloud()
# else:
#     print('input error')



