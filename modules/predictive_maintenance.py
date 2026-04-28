#Coded by @nmurthydev 

# predictive_maintenance.py - placeholder functional code
#import os, pickle
#from sklearn.ensemble import RandomForestRegressor
#import pandas as pd

#MODEL_PATH = 'models/maint_model.pkl'

#def train_model(df):
    #X = df[['hours_running','miles','vibration','temp']]
   # y = df['rul']
    #model = RandomForestRegressor(n_estimators=50, random_state=0)
    #model.fit(X,y)
    #os.makedirs('models', exist_ok=True)
    #pickle.dump(model, open(MODEL_PATH,'wb'))
   # return model

#def load_model():
    #if os.path.exists(MODEL_PATH):
        #return pickle.load(open(MODEL_PATH,'rb'))
    #return None

#def predict(features: dict):
    #model = load_model()
    #if model is None:
        #return {'error':'no model'}
   # X = [[features.get('hours_running',0), features.get('miles',0), features.get('vibration',0), features.get('temp',0)]]
    #return {'rul': float(model.predict(X)[0])}

import os, pickle
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

MODEL_PATH = 'models/maint_model.pkl'
DEFAULT_DATA_PATH = 'training_data.csv'

def train_model(df):
    X = df[['hours_running', 'miles', 'vibration', 'temp']]
    y = df['rul']
    model = RandomForestRegressor(n_estimators=50, random_state=0)
    model.fit(X, y)
    os.makedirs('models', exist_ok=True)
    pickle.dump(model, open(MODEL_PATH, 'wb'))
    return model

def load_model():
    if os.path.exists(MODEL_PATH):
        return pickle.load(open(MODEL_PATH, 'rb'))
    # Auto-train if model not found
    elif os.path.exists(DEFAULT_DATA_PATH):
        df = pd.read_csv(DEFAULT_DATA_PATH)
        print("🔧 Training model automatically using default training_data.csv...")
        return train_model(df)
    else:
        print("⚠️ No model or training_data.csv found.")
        return None

def predict(features: dict):
    model = load_model()
    if model is None:
        return {'error': 'No model or training data available'}
    X = [[
        features.get('hours_running', 0),
        features.get('miles', 0),
        features.get('vibration', 0),
        features.get('temp', 0)
    ]]
    rul = round(float(model.predict(X)[0]))

    return f"Remaining useful life: {rul}"
    

    #return {'rul': float(model.predict(X)[0])}


