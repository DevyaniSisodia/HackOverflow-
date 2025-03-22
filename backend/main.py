from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Load the trained model
model = joblib.load("model/inventory_model.pkl")

class InventoryData(BaseModel):
    past_sales: float
    seasonality: float
    market_trends: float

@app.post("/predict/")
def predict_inventory(data: InventoryData):
    df = pd.DataFrame([[data.past_sales, data.seasonality, data.market_trends]],
                      columns=["past_sales", "seasonality", "market_trends"])
    
    prediction = model.predict(df)[0]
    return {"predicted_demand": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
