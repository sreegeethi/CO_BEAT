from django.shortcuts import render
import keras
import os
from tensorflow.keras.preprocessing.image import load_img
from pyAudioAnalysis import audioTrainTest as aT
import numpy as np
from tensorflow.keras.models import load_model
from django.core.files.storage import default_storage
import requests
from CO_BEAT_Webapp.models import Alerts

def home(request):
    return render(request,'index.html')

def about_covid(request):
    return render(request,'aboutcovid.html')

def contact_tracing(request):
    if request.method=="POST":
        place = request.POST['placeName']
        alerts = Alerts.objects.filter(venue__contains=place).order_by('-time_date')
    else:
        alerts = Alerts.objects.order_by('-time_date')

    data = {
        "alert": alerts
    }
    return render(request,'contact_tracing_alerts.html', data)

def cough_sound_pred(request):
    if request.method=="POST":
        f = request.FILES['coughSound']
        response = {}
        file_name = default_storage.save(f.name, f)
        media_dir = os.path.dirname(os.path.dirname(__file__))+'/media'
        audio_file = os.path.join(media_dir,file_name)
        model=os.path.dirname(__file__)+'/svm_model'
        pred = aT.file_classification(audio_file, model ,"svm")
        print(pred)
        response['pred']=pred[0]
        return render(request,'cough_sound_detection.html',response)
    else:
        return render(request,'cough_sound_detection.html')

def xray_pred(request):
    if request.method=="POST":
        f=request.FILES['sentFile']
        response = {}
        file_name = default_storage.save(f.name, f)
        media_dir = os.path.dirname(os.path.dirname(__file__))+'/media'
        image = load_img((os.path.join(media_dir,file_name)), target_size=(224, 224))
        image = np.array(image)/255
        image = image.reshape(-1, 224, 224, 3)

        #Load the model
        model=load_model(os.path.dirname(__file__)+'/model.h5')
        prediction = model.predict(image)

        if prediction>0.5:
            result="COVID NOT DETECTED"
        else:
            result="COVID DETECTED"
        
        response['pred']=result

        response['pred']=result
        return render(request,'detection.html',response)
    else:
        return render(request,'detection.html')
        
        
def dashboard(request):
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

    headers = {
        'x-rapidapi-key': "bf587f137fmshbd08cf4ce75ac18p1ac3a8jsn727586255fb6",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
        }

    r = requests.request("GET", url, headers=headers).json()
    total=r['total_values']['active']
    recover=r['total_values']['recovered']
    confirm=r['total_values']['confirmed']
    deaths=r['total_values']['deaths']
    time=r['total_values']['lastupdatedtime']
    s=[[]]
    state=[]
    s_active=[]
    s_recover=[]
    s_confirm=[]
    s_deaths=[]
    for each in r['state_wise']:
        if int(r['state_wise'][each]['active'])!=0:
            state.append(each)
            a =int(r['state_wise'][each]['active'])
            print(a)
            s_active.append(a)
            d =int(r['state_wise'][each]['recovered'])
            s_recover.append(d)
            c = int( r['state_wise'][each]['deaths'])
            s_deaths.append(c)
            b = int( r['state_wise'][each]['confirmed'])
            s_confirm.append(b)

    for i in range(len(state)):
        s.append([s_confirm[i],s_active[i],s_deaths[i],s_recover[i],state[i]])
    # print(s_confirm)

    return render(request,'covid_dashboard.html',{'s':s,'total':total,'recover':recover,'confirm':confirm,'death':deaths,'time':time, 'state':state,'s_active':s_active,'s_recover':s_recover,'s_deaths':s_deaths,'s_confirm':s_confirm})

