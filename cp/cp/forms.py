from django import forms

class PatientDataForm(forms.Form):
    age = forms.IntegerField()
    blood_glucose_level = forms.FloatField()
    HbA1c_level = forms.FloatField()
    bmi = forms.FloatField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('other', 'other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    hypertension = forms.BooleanField(required=False)
    heart_disease = forms.BooleanField(required=False)
    smoking_history = forms.CharField(max_length=255)