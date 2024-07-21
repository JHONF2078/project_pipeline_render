from fastapi import FastAPI
from data_model import Water
import pickle
import pandas  as pd


app = FastAPI(
    title="water potability prediction",
    description="Predicting water potability",
)

with open("model.pkl", 'rb') as file:
    model = pickle.load(file)
    
@app.get("/")
def index():
    return {"message": "Welcome to the water potability prediction FastAPI"}

@app.post("/predict")
def model_predict(water: Water):
    sample = pd.DataFrame(
        {
            'ph': [water.ph],
            'Hardness': [water.Hardness],
            'Solids': [water.Solids],
            'Chloramines': [water.Chloramines],
            'Sulfate': [water.Sulfate],
            'Conductivity': [water.Conductivity],
            'Organic_carbon': [water.Organic_carbon],
            'Trihalomethanes': [water.Trihalomethanes],
            'Turbidity': [water.Turbidity],
        }
    )
    
    predicted_value = model.predict(sample)
    
    if predicted_value == 1:
        return "Water is Consumable"
    else:
        return "Water is not Consumable"
    
    
