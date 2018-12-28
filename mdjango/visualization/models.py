from django.db import models

# Create your models here.
from mova.models import *
from visualization.views import VisualizationChart
from reportlab.pdfgen import canvas
import shutil
import os


# 从数据库中获取数据的接口函数
# 输入：year--年，season--季度, month--月份
# 输出：存有数据信息的字典列表
def film_out(year, season, month):
    fid = []
    film = []
    # month比season具有更高的优先级，即选择month后season参数被忽略，仅当month=='0'时season参数有效
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


# 根据年、季度、月份、TOP读取电影数据的类
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

    # 获取各题材电影的票房数据
    def get_boxoffice_ratio(self):
        source_data = film_out(self.year, self.quarter, self.month)    # 从数据库中获取数据
        # 每部电影的题材数据是一串由逗号分隔的字符串，因此先用split(',')将字符串分割，得到每部电影的题材列表
        # 然后将所有电影的题材列表合并，去重，得到所有题材的列表
        source_theme_list = [x['type'].split(',') for x in source_data]
        source_theme_list = [x for j in source_theme_list for x in j]
        theme_name = list(set(source_theme_list))
        theme_boxoffice = []
        for theme in theme_name:
            boxoffice = [x['boxoffice'] for x in source_data if theme in x['type']]
            boxoffice = int(sum(boxoffice))
            theme_boxoffice.append(boxoffice)
        # 为作图时使图表美观，仅保留票房前十的题材，其余的归入‘其它’类
        if len(theme_name) > 10:
            theme_dict = dict(zip(theme_name, theme_boxoffice))
            # 根据票房值对题材-票房字典进行排序
            theme_dict = dict(sorted(theme_dict.items(), key=lambda x: x[1], reverse=True))
            theme_name = list(theme_dict.keys())
            theme_boxoffice = list(theme_dict.values())
            theme_name[10] = '其它'
            theme_boxoffice[10] = sum(theme_boxoffice[10:])
            del theme_name[11:]
            del theme_boxoffice[11:]
        self.x_axis = theme_name
        self.y_axis = theme_boxoffice
        # 根据输入的参数确定图表的标题，其中month比quarter具有更高的优先级，
        # 即选择month后quarter参数被忽略，仅当month=='0'时quarter参数有效
        # 参数 == 0时，该参数被忽略，也不会在图表标题中被显示出来
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

    # 获取历年来的电影票房数据
    def get_boxoffice_trend(self):
        boxoffice_list = []
        # 在制作电影票房趋势图时，year, quarter, month对应的是选择的三个年份
        self.year = sorted([self.year, self.quarter, self.month])
        for year in self.year:
            one_year_boxoffice_list = []
            for month in range(1, 13):
                source_data = film_out(year, '0', str(month))    # 逐个从数据库获取year年各个月份的票房数据
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
    
    # 获取top电影数据
    def get_top_movie(self):
        source_data = film_out(self.year, '0', '0')
        movie_name = [x['name'] for x in source_data]
        movie_boxoffice = [x['boxoffice'] for x in source_data]
        movie_dict = dict(zip(movie_name, movie_boxoffice))
        # 根据票房值对电影名-票房字典进行排序
        movie_dict = dict(sorted(movie_dict.items(), key=lambda x: x[1], reverse=True))
        self.x_axis = list(movie_dict.keys())[0:self.top_x]    # 只取前top_x的数据
        self.y_axis = list(movie_dict.values())[0:self.top_x]
        self.title = self.year + '年电影票房TOP' + str(self.top_x)
        self.data_name = ''
        self.chart_name = 'top_movie'

    # 获取top劳模演员
    def get_top_actor(self):
        source_data = film_out(self.year, '0', '0')
        # 演员数据已经处理过逗号分隔符，因此无需像题材数据那样再用split分割
        # 最后得到的actor_name是所有演员名的列表
        actor = [x['actor'] for x in source_data]
        actor = [x for j in actor for x in j]
        actor_name = list(set(actor))
        appearance_number = [actor.count(x) for x in actor_name]    # 计算每个演员名出现的次数
        actor_dict = dict(zip(actor_name, appearance_number))
        actor_dict = dict(sorted(actor_dict.items(), key=lambda x: x[1], reverse=True))    # 根据演员出演次数进行排序
        if '--' in list(actor_dict.keys())[0:self.top_x]:
            # '--'为电影数据爬取无演员数据时的默认缺失值
            # 如果前top个数据中出现了'--'，则需要进行处理，将'--'数据删掉
            del actor_dict['--']
        self.x_axis = list(actor_dict.keys())[0:self.top_x]    # 只取前top_x的数据
        self.y_axis = list(actor_dict.values())[0:self.top_x]
        self.title = self.year + '年TOP' + str(self.top_x) + '劳模演员'
        self.data_name = ''
        self.chart_name = 'top_actor'


# 后端数据可视化函数
# 功能：在后端画图，将图片存储到文件中，并返回输入参数对应的电影数据
# 输入：func_selected: '1'-'7'，对应七种可视化功能；year：'2015'-'2018'或'0'，年份；quarter: '1'-'4'或'0'，四个季度；
#      month：'1'-'12'或'0'，月份；top_x：int型数据，前TOP个数据
# 输出：data_dict：字典，输入参数对应的电影数据
def data_visualization(func_selected, year, quarter, month, top_x):
    data_dict = {}
    movie_data = MovieData(year, quarter, month, top_x)    # 接收参数，初始化movie_data类
    # 根据不同的功能选择，执行不同的操作
    if func_selected == '1':
        # 题材票房比例柱状图
        # 对movie_data类执行get_boxoffice_ratio获取各题材电影的票房，将数据保存在输出data_dict中
        # 再通过VisualizationChart类画图
            movie_data.get_boxoffice_ratio()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.histogram()    # 柱状图
    elif func_selected == '2':
        # TOP电影柱状图
            movie_data.get_top_movie()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.histogram()
    elif func_selected == '3':
        # TOP劳模演员柱状图
            movie_data.get_top_actor()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.histogram()
    elif func_selected == '4':
        # 电影变化趋势折线图
            movie_data.get_boxoffice_trend()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.line()
    elif func_selected == '5':
        # 题材票房比例饼状图
            movie_data.get_boxoffice_ratio()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.pie()
    elif func_selected == '6':
        # TOP电影词云
            movie_data.get_top_movie()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.word_cloud()
    elif func_selected == '7':
        # TOP劳模演员词云
            movie_data.get_top_actor()
            data_dict = {'chart_title': movie_data.title, 'x_axis': movie_data.x_axis, 'y_axis': movie_data.y_axis}
            movie_charts = VisualizationChart(movie_data.title, movie_data.data_name, movie_data.x_axis,
                                                                                movie_data.y_axis, movie_data.chart_name)
            movie_charts.word_cloud()
    return data_dict


# 将要保存的图表png文件写入到pdf文件中，生成数据报表
# 输入：save_charts：字符串，说明了要保存的图表，
# 例如"1457"表示将第1、4、5、7号文件（具体对应关系见下方chart_file_chart字典）写入到数据报表pdf文件中
def save_charts_as_pdf(save_charts):
    pdf_pagesize = (600, 300*len(save_charts))    # 设置pdf的大小：600为pdf宽度，300为一个图表的长度
    c = canvas.Canvas("visualization_report.pdf", pagesize=pdf_pagesize)
    cur_pos_in_pdf = 300 * (len(save_charts) - 1)    # 设置第一个图表在pdf中的位置（pdf从上至下pos值逐渐减小）
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



