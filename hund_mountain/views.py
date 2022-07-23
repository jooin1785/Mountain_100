from django.shortcuts import render, redirect
from .models import Coordinate, Mountain1, Mountain2, Mountain3, LiveWeather, Subway, Train, Bus
from tkinter import messagebox
import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

custom_header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}



def index(request):
    return render(request, 'index.html')


def zoom_1(request, areacode):
    area = Coordinate.objects.get(areacode=areacode)
    return render(request, 'mt_map_zoom_1.html', {'area': area})



def zoom_2(request, id):
    vo = dict()
    dto = Mountain1.objects.get(id=id)
    vo['dto'] = dto

    sun_stuffs = {
        'nowWeather': nowWeather(id),
        'nowTemp': nowTemp(id),
        'sunriseTime': sunriseTime(id),
        'sunsetTime': sunsetTime(id),
        'tw': today_weather(id),
        'tommorow_weather': tommorow_weather(id),
        'after_tommorow_weather': after_tommorow_weather(id)
    }

    vo['sun_stuffs'] = sun_stuffs

    return render(request, 'mt_map_zoom_2.html', {'vo': vo})


def sunriseTime(id):
    try:
        url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
        req = requests.get(url, headers=custom_header).text
        document = json.loads(req)
        others = document['others']
        sunriseTime = others['sunriseTime']
        return sunriseTime
    except:
        return '-'

def sunsetTime(id):
    try:
        url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
        req = requests.get(url, headers=custom_header).text
        document = json.loads(req)
        others = document['others']
        sunsetTime = others['sunsetTime']
        return sunsetTime
    except:
        return '-'

def nowTemp(id):
    try:
        url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
        req = requests.get(url, headers=custom_header).text
        document = json.loads(req)
        weather = document['famousMTSDTO']['forestAWS10Min']
        nowTemp = weather['tm2m']
        return nowTemp
    except:
        return '-'

def nowWeather(id):
    try:
        url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
        req = requests.get(url, headers=custom_header).text
        document = json.loads(req)
        others = document['others']
        nowWeather = int(others['iconCode'])
        return nowWeather
    except:
        return '-'

def today_weather(id):
    try:
        url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
        req = requests.get(url, headers=custom_header).text
        document = json.loads(req)
        others = document['others']
        weather_info = document['hr3List']
        tw = dict()
        tw['wcond'] = weather_info[0]['wcond'] # 날씨 코드
        tw['temp'] = weather_info[0]['temp'] # 기온
        tw['humi'] = weather_info[0]['humi'] # 습도
        tw['wspd'] = weather_info[0]['wspd'] # 풍속
        tw['rainp'] = weather_info[0]['rainp'] # 강우 확률
        return tw
    except:
        return ''

def tommorow_weather(id):
    try:
        url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
        req = requests.get(url, headers=custom_header).text
        document = json.loads(req)
        others = document['others']
        weather_info = document['hr3List']
        tommorow_weather = dict()
        tommorow_weather['wcond'] = weather_info[-14]['wcond'] # 내일 9시 기준
        tommorow_weather['temp'] = weather_info[-14]['temp']
        tommorow_weather['humi'] = weather_info[-14]['humi']
        tommorow_weather['wspd'] = weather_info[-14]['wspd']
        tommorow_weather['rainp'] = weather_info[-14]['rainp']
        return tommorow_weather
    except:
        return ''

def after_tommorow_weather(id):
    try:
        url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
        req = requests.get(url, headers=custom_header).text
        document = json.loads(req)
        others = document['others']
        weather_info = document['hr3List']
        after_tommorow_weather = dict()
        after_tommorow_weather['wcond'] = weather_info[-6]['wcond'] # 모레 9시 기준
        after_tommorow_weather['temp'] = weather_info[-6]['temp']
        after_tommorow_weather['humi'] = weather_info[-6]['humi']
        after_tommorow_weather['wspd'] = weather_info[-6]['wspd']
        after_tommorow_weather['rainp'] = weather_info[-6]['rainp']
        return after_tommorow_weather
    except:
        return ''


def details(request, id):
    weather_detail = {
        'df': df(id)
    }
    return render(request, 'mt_map_zoom_2.html', {'weather_detail': weather_detail})


def df(id):
    url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
    req = requests.get(url, headers=custom_header).text
    document = json.loads(req)
    others = document['others']
    weather_info = document['hr3List']
    df = pd.DataFrame(columns=['시간', '날씨', '강우 확률', '기온'])
    for i in range(0, len(weather_info), 2):
        tmeF = weather_info[i]['tmEf'].replace('2022', '')
        wcond = weather_info[i]['wcond']
        rainp = weather_info[i]['rainp']
        temp = weather_info[i]['temp']
        df = df.append(pd.DataFrame([[tmeF, wcond, rainp, temp]], columns=['시간', '날씨', '강우 확률', '기온']))
    print(df)


def time(id):
    url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
    req = requests.get(url, headers=custom_header).text
    document = json.loads(req)
    others = document['others']
    weather_info = document['hr3List']
    for i in range(0, len(weather_info), 2):
        time = weather_info[i]['tmEf'].replace('2022', '')
        return time


def wcond_details(id):
    url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
    req = requests.get(url, headers=custom_header).text
    document = json.loads(req)
    others = document['others']
    weather_info = document['hr3List']
    for i in range(0, len(weather_info), 2):
        wcond_details = weather_info[i]['wcond']
        return wcond_details


def rainp_details(id):
    url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
    req = requests.get(url, headers=custom_header).text
    document = json.loads(req)
    others = document['others']
    weather_info = document['hr3List']
    for i in range(0, len(weather_info), 2):
        rainp_details = weather_info[i]['rainp']
        return rainp_details


def temp_details(id):
    url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={id}'
    req = requests.get(url, headers=custom_header).text
    document = json.loads(req)
    others = document['others']
    weather_info = document['hr3List']
    for i in range(0, len(weather_info), 2):
        temp_details = weather_info[i]['temp']
        return temp_details



def list(request):
    mountains = Mountain1.objects.all()
    return render(request, 'list.html', {'mountains': mountains})



def detail(request, id):
    if request.method == 'GET':
        mountain1 = Mountain1.objects.get(id=id)
        mountain2 = Mountain2.objects.get(id=id)
        mountain3 = Mountain3.objects.get(id=id)

        vo = dict()
        dto = Mountain1.objects.get(id=id)
        vo['dto'] = dto
        sun_stuffs = {
            'nowWeather': nowWeather(id),
            'nowTemp': nowTemp(id),
            'sunriseTime': sunriseTime(id),
            'sunsetTime': sunsetTime(id),
            'tw': today_weather(id),
            'tommorow_weather': tommorow_weather(id),
            'after_tommorow_weather': after_tommorow_weather(id)
        }
        vo['sun_stuffs'] = sun_stuffs

        return render(request, 'detail.html', {'mountain1':mountain1, 'mountain2': mountain2, 'mountain3': mountain3, 'vo':vo, 'id':id})

    else:
        mt_name = request.POST['mt_name']
        try:
            mountain1 = Mountain1.objects.get(name=mt_name)
            id = mountain1.id
            mountain2 = Mountain2.objects.get(id=id)
            mountain3 = Mountain3.objects.get(id=id)

            vo = dict()
            dto = Mountain1.objects.get(id=id)
            vo['dto'] = dto
            sun_stuffs = {
                'nowWeather': nowWeather(id),
                'nowTemp': nowTemp(id),
                'sunriseTime': sunriseTime(id),
                'sunsetTime': sunsetTime(id),
                'tw': today_weather(id),
                'tommorow_weather': tommorow_weather(id),
                'after_tommorow_weather': after_tommorow_weather(id)
            }
            vo['sun_stuffs'] = sun_stuffs

            return render(request, 'detail.html', {'mountain1': mountain1, 'mountain2': mountain2, 'mountain3': mountain3, 'vo': vo, 'id':id})
        except:
            messagebox.showinfo('Error', '해당 산이 목록에 없습니다')
            return redirect('/list/')


def analyze_2(request):
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    tm = str(tomorrow)
    tmr = tm[:4] + tm[5:7] + tm[8:10] + '09'

    lW = LiveWeather.objects.filter(day=tmr)
    df = pd.DataFrame(columns=['name', 'temp', 'hum', 'di', 'num'])
    j = 0
    for i in lW:
        df.loc[j] = [str(i.name), float(i.temp), float(i.hum), float(i.di), float(i.num)]
        j += 1

    conditionlist = [
        (df['di'] <= 68),
        (df['di'] <= 70) & (df['di'] > 68),
        (df['di'] <= 75) & (df['di'] > 70),
        (df['di'] <= 80) & (df['di'] > 75),
        (df['di'] <= 83) & (df['di'] > 80),
        (df['di'] <= 86) & (df['di'] > 83)]
    choicelist = ["매우 쾌적", "쾌적", "조금 쾌적", "조금 불쾌", "불쾌", "매우 불퇘"]
    df['di_count'] = np.select(conditionlist, choicelist)

    color = ['#008080']
    sns.set_palette(color)

    sns.displot(x='hum', y='temp', data=df, kind='hist', binwidth=(3, 1))
    plt.savefig('./hund_mountain/static/assets/img/graph.png')

    colors = ['#0100FF', '#00D8FF', "#B2EBF4", '#FFC19E', '#FFA7A7']
    #colors = ['#FFA7A7', '#FFC19E', "#B2EBF4", '#00D8FF', '#0100FF']

    sns.set_palette(sns.color_palette(colors))
    ax = sns.countplot(data=df, y='di_count', order=['매우 쾌적', '쾌적', '조금 쾌적', '조금 불쾌', '불쾌'])
    plt.yticks(rotation=90)
    plt.ylabel('불쾌 지수')
    ax.figure.savefig('./hund_mountain/static/assets/img/graph2.png')

    cf1 = LiveWeather.objects.filter(di__lt = 68) & LiveWeather.objects.filter(day=tmr)
    cf2 = LiveWeather.objects.filter(di__lt = 70) & LiveWeather.objects.filter(di__gt =68) & LiveWeather.objects.filter(day=tmr)
    cf3 = LiveWeather.objects.filter(di__lt = 75) & LiveWeather.objects.filter(di__gt =70) & LiveWeather.objects.filter(day=tmr)

    return render(request, 'analyze_2.html', {'cf1':cf1, 'cf2':cf2, 'cf3':cf3})


def transit(request, id):
    subway = Subway.objects.all()
    train = Train.objects.all()
    bus = Bus.objects.all()
    mountain = Mountain1.objects.all()
    center = Mountain1.objects.get(id=id)
    return render(request, 'transit.html', {'subway': subway, 'train': train, 'bus': bus, 'mountain': mountain, 'id': id, 'center':center})


def recommend(request):
    return render(request, 'recommend.html')


def analyze_1(request):
    return render(request, 'analyze_1.html')
