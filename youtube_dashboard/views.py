import inspect

import StoreToDB as SDB
import json
from StoreToDB import views as v
from hashlib import sha512
from django.shortcuts import render, redirect

def data_all_ads(user_id):
    data = v.data_all_ads(user_id)
    return data

def data_general_statistics(user_id):
    data = v.data_general_stat(user_id)
    return data


# Create your views here.
def get_general_statistics(request):
    try:
	print('this is the id',request.GET.get('id', None))
       # user_id =  "f9207a067be204106ecb39c45f69ecaa3727de20d05d00d2e5fcf0f1498461d6d61508dbc593d0c5bf8f3e4cbe479bc218f5d9ae77f0492cd8bbe3731f18a4f9"
       # user_id = "62407086e5f6f9f6eaa70d6c4a524ece4c478e03358eb50b285ea330b33522b3285de474eb9ac91f6b9705a9926ebd171f51e43d19c9ef0cb75503eaa7d50ee9"
	#user_id = "f16590b7874e881df3ee997bd8c158771b3a28f3d342102f2441ca2d44d50e8963de04db6d3521e362f50f693ffb0c76f494fe69f21aa2e9cfd7c77138f79a28"
	user_id = sha512(str(request.GET.get('id', None)).encode('utf-8')).hexdigest()
        print('hash id',user_id) 
        data = data_general_statistics(user_id)
	print("this is data",data)
        return render(None, 'users_statistics/general_statistics.html',
                      {'total_video_ads': json.dumps(data['total_video_ads']) ,
                       'total_ads': json.dumps(data['total_ads'] ),
                       'distinct_videos': json.dumps(data['distinct_videos'] ),
                       'average_ads_videos': json.dumps(data['average_ads_videos'] ),
                       'advertisers': json.dumps(data['advertisers'] ),
                       'attributes': json.dumps(data['attributes'] ),
                       'targeting': json.dumps(data['targeting'] ),
                       'chartData': json.dumps(data['chartData'] )})
    except (KeyError) as e:
        return "wrong"


def get_all_ads(request):
    try:
        #user_id = "f9207a067be204106ecb39c45f69ecaa3727de20d05d00d2e5fcf0f1498461d6d61508dbc593d0c5bf8f3e4cbe479bc218f5d9ae77f0492cd8bbe3731f18a4f9"
        #user_id = "62407086e5f6f9f6eaa70d6c4a524ece4c478e03358eb50b285ea330b33522b3285de474eb9ac91f6b9705a9926ebd171f51e43d19c9ef0cb75503eaa7d50ee9"
	#user_id = "f16590b7874e881df3ee997bd8c158771b3a28f3d342102f2441ca2d44d50e8963de04db6d3521e362f50f693ffb0c76f494fe69f21aa2e9cfd7c77138f79a28"
        user_id = sha512(str(request.GET.get('id', None)).encode('utf-8')).hexdigest()
        data = data_all_ads(user_id)
	print('Okey lets have the advertisers',json.dumps(data['advertisers']))
        return render(None, 'users_statistics/view_all_ads.html',
                      {
                          "ads":json.dumps(data['ads']),
                          "advertisers": json.dumps(data['advertisers']),
                          "targetings": json.dumps(data['targetings']),
                      })
    except (KeyError) as e:
        return "wrong"


def get_site(request):
    try:
        return render(None, 'landing-page.html',
                      {})
    except (KeyError) as e:
        return "wrong"
