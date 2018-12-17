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
            '1': "./frontend/src/diagrams/boxoffice_ratio_bar.png",
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

