import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Ensure 'model/' directory exists
if not os.path.exists("model"):
    os.makedirs("model")

data = {
    "past_sales": [100, 200, 150, 300, 400],
    "seasonality": [1, 0, 1, 0, 1],
    "market_trends": [0.5, 0.8, 0.6, 0.9, 1.0],
    "demand_forecast": [120, 220, 160, 310, 420]
}

df = pd.DataFrame(data)

X = df[["past_sales", "seasonality", "market_trends"]]
y = df["demand_forecast"]

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

# Save the trained model
joblib.dump(model, "model/inventory_model.pkl")
print("✅ Model trained & saved successfully!")
