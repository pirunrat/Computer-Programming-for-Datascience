from joblib import load
import seaborn as sns
import numpy as np
import pandas as pd

class Model:

    def __init__(self,model_path):
        self.model = load(model_path)
        
    def load(self, model_path):
        loaded_model = load(model_path)
        return loaded_model
    
    def predict(self, newData):
        return self.model.predict(newData)
    

    