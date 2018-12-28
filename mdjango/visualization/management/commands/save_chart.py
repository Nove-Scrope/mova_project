# save_chart.py -- 一个文件复制脚本
# 原先采用的数据报表方案是前端在命令行中执行该脚本，将生成的图表文件复制到指定文件夹中
# 后面采用将图表写入pdf文件的方法
# 原方案被废弃，脚本也失去了意义
from django.core.management.base import BaseCommand
import shutil
import os


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('func-selected', nargs='+', type=str)

    def handle(self, *args, **options):
        funcs_selected = options['func-selected']
        chart_save_path = './downloads'
        chart_file_dict = {
            '1': "boxoffice_ratio_bar.png",
            '2': "top_movie_bar.png",
            '3': "top_actor_bar.png",
            '4': "boxoffice_trend_line.png",
            '5': "boxoffice_ratio_pie.png",
            '6': "top_movie_wordcloud.png",
            '7': "top_actor_wordcloud.png",
        }
        if not os.path.exists(chart_save_path):
            os.makedirs(chart_save_path)
        for func in funcs_selected:
            if not os.path.isfile(chart_file_dict[func]):
                print("%s not exist!" % chart_file_dict[func])
            else:
                shutil.copy(chart_file_dict[func], chart_save_path)
                print("%s has been saved successfully." % chart_file_dict[func])

