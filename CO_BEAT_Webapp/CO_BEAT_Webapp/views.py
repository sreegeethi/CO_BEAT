from django.shortcuts import render
import keras
import os
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
from tensorflow.keras.models import load_model
from django.core.files.storage import default_storage

def home(request):
    return render(request,'index.html')

def about_covid(request):
    return render(request,'aboutcovid.html')

def xray_pred(request):
    if request.method=="POST":
        f=request.FILES['sentFile']
        response = {}
        file_name = default_storage.save(f.name, f)
        file_url = default_storage.url(file_name)
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
        
        

