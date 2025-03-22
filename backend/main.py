
import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to the AI Inventory Prediction API!"}


# Ensure model path is correct
model_path = os.path.join(os.path.dirname(__file__), "model", "inventory_model.pkl")

# Load AI model
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    raise RuntimeError(f"❌ Model file not found at {model_path}. Please train and save the model.")

class InventoryData(BaseModel):
    past_sales: float
    seasonality: float
    market_trends: float

@app.post("/predict/")
def predict_inventory(data: InventoryData):
    try:
        df = pd.DataFrame([[data.past_sales, data.seasonality, data.market_trends]],
                          columns=["past_sales", "seasonality", "market_trends"])
        prediction = model.predict(df)[0]
        return {"predicted_demand": prediction}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
