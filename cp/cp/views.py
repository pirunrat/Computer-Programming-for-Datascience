from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import PatientDataForm
import pandas as pd
import numpy as np
from .model import Model
from django.conf import settings
import os


def your_view_function(request):

    dict_diagnos = {0:"Non-Diabetic",1:"Diabetic",None:''}

    model_path = os.path.join(settings.BASE_DIR, 'cp/models/' + 'model.pkl')
     # Initialize prediction variable
    prediction = [None]
    if request.method == 'POST':
        form = PatientDataForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            age = form.cleaned_data['age']
            blood_glucose_level = form.cleaned_data['blood_glucose_level']
            HbA1c_level = form.cleaned_data['HbA1c_level']
            bmi = form.cleaned_data['bmi']
            gender = form.cleaned_data['gender']
            hypertension = form.cleaned_data['hypertension']
            heart_disease = form.cleaned_data['heart_disease']
            smoking_history = form.cleaned_data['smoking_history']
            
            # Now you can put the input data into your DataFrame as you did before
            data = {
                'gender': [gender],
                'age': [age],
                'hypertension': [hypertension],
                'heart_disease': [heart_disease],
                'smoking_history': [smoking_history],
                'bmi': [bmi],
                'HbA1c_level': [HbA1c_level],
                'blood_glucose_level': [blood_glucose_level],
            }
            
            # Perform your DataFrame operations here

            df = pd.DataFrame(data)

            model = Model(model_path)

            prediction = model.predict(df)

            if(prediction is None):
                prediction = 2
                

            print(f"The prediction : {prediction}")

    else:
        form = PatientDataForm()
      # Pass the prediction result to the template context
    context = {
        'form': form,
        'prediction': dict_diagnos[prediction[0]],
    }
        
    return render(request, 'main.html', context)


@api_view(['GET'])
def APIs_document(request):
    return render(request, 'api.html')


@api_view(['POST'])
def API(request):
    dict_diagnos = {0: "Non-Diabetic", 1: "Diabetic", None: ''}
    model_path = os.path.join(settings.BASE_DIR, 'cp/models/' + 'model.pkl')

    # Initialize prediction variable
    prediction = None
    
    if request.method == 'POST':
        data = request.data  # Assuming you send the same data as in the form

        gender = data.get('gender')
        age = data.get('age')
        hypertension = data.get('hypertension')
        heart_disease = data.get('heart_disease')
        smoking_history = data.get('smoking_history')
        bmi = data.get('bmi')
        HbA1c_level = data.get('HbA1c_level')
        blood_glucose_level = data.get('blood_glucose_level')

        # Now you can put the input data into your DataFrame as you did before
        data = {
            'gender': [gender],
            'age': [age],
            'hypertension': [hypertension],
            'heart_disease': [heart_disease],
            'smoking_history': [smoking_history],
            'bmi': [bmi],
            'HbA1c_level': [HbA1c_level],
            'blood_glucose_level': [blood_glucose_level],
        }

        # Perform your DataFrame operations here
        df = pd.DataFrame(data)
        model = Model(model_path)
        prediction = model.predict(df)

        if prediction is None:
            prediction = 2

        print(f"The prediction : {prediction[0]}")

    return Response({'prediction': dict_diagnos[prediction[0]]})
        
        
