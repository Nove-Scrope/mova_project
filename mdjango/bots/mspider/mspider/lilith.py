from mova import models
from mova.models import *


def film_in(self, film):    # 接收字典传入
    if self.name == "No database connected":
        print("No database connected or established")
        return
    Film.objects.create(name=film['name'], type=film['type'], score_rate=film['score_rate'], score_num=film['score_num'],
                        date=film['date'], boxoffice=film['boxoffice'], day_boxoffice=film['day_boxoffice'],
                        week_boxoffice=film['week_boxoffice'], score=film['score'])
    # 演员table中，一名演员有多个存储block,每一个block对应一部电影


def actor_in(self, actor, film):  # 接收字典,film为string
    if self.name == "No database connected":
        print("No database connected or established")
        return
    target = Film.objects.get(name=film)
    fid = target.filmid
    Actor.objects.create(name=actor['name'],filmid=fid)


# 演员table中，一名导演有多个存储block,每一个block对应一部电影
def director_in(self, director, film):    # 接收字典,film为string
    if self.name == "No database connected":
        print("No database connected or established")
        return
    target = Film.objects.get(name=film)
    fid = target.filmid
    Director.objects.create(name=director['name'], filmid=fid)


# 类型table中，一部电影有多个存储block,每一个block对应一种电影类型
def type_in(self, ty_pe, film):   # film，ty_pe为string
    if self.name == "No database connected":
        print("No database connected or established")
        return
    target = Film.objects.get(name=film)
    fid = target.filmid
    t = ty_pe.split(',')
    for item in t:
        Type.objects.create(name=item, filmid=fid)


def film_out(self, year, season, month):
    if self.name == "No database connected":
        print("No database connected or established")
        return
    fid = []
    film = []
    if year == '0':
        year = ''
    if month != '0':
        if len(month) == 1:
            month = "0" + month
        select = year + '-' + month
        print(select)
        target = Film.objects.all().values_list('name','filmid')
        for item in target:
            if item.name.find(select) != -1:
                fid.append(item.filmid)
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
        target = Film.objects.all().values_list('name','filmid')
        for item in target:
            if item.name.find(year + '-' + mm[0]) != -1 or item.name.find(year + '-' + mm[1]) != -1 or item.name.find(year + '-' + mm[2]) != -1:
                fid.append(item.filmid)
    # print(filmid)
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
