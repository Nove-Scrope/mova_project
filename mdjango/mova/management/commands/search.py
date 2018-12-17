from django.core.management.base import BaseCommand, CommandError
import json
from mova.models import *

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('film_params', nargs='+', type=str)
    def handle(self, *args, **options):
        film_params = options['film_params']
        f_name = str(film_params[0])
        f_director = str(film_params[1])
        f_actor = str(film_params[2])
        ans = []
        fid = []
        if f_name != '0':
            op = {}
            it = Film.objects.get(name=f_name)
            fid.append(it.filmid)
        else:
            for item in Film.objects.all().values_list('filmid'):
                fid.append(int(list(item)[0]))
        if f_director != '0':
            res = Director.objects.filter(name=f_director)
            fid1 = []
            for it in res:
                if it.filmid in fid:
                    fid1.append(it.filmid)
            fid = fid1
        if f_actor != '0':
            res = Actor.objects.filter(name=f_actor)
            fid1 = []
            for it in res:
                if it.filmid in fid:
                    fid1.append(it.filmid)
            fid = fid1
        for it in fid:
            target = Film.objects.get(filmid=it)
            op = {}
            op['name'] = target.name
            op['type'] = target.type
            op['score_rate'] = target.score_rate
            op['score_num'] = target.score_num
            op['date'] = target.date
            op['boxoffice'] = target.boxoffice
            op['day_boxoffice'] = target.day_boxoffice
            op['week_boxoffice'] = target.week_boxoffice
            op['score'] = target.score
            op['actor'] = []
            op['director'] = []
            res = Actor.objects.filter(filmid=it)
            for uu in res:
                op['actor'].append(uu.name)
            res = Director.objects.filter(filmid=it)
            for uu in res:
                op['director'].append(uu.name)
            ans.append(op)
        json_str = json.dumps(ans)
        with open('frontend/static/data.json','wb') as j:
            j.write(json_str.encode())
