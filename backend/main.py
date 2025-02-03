# Backend Prototype

# Import required libraries
from fastapi import FastAPI
import numpy as np
import asyncio

# Create an instance of FastAPI
app = FastAPI()

# Define the home route
@app.get('/')
def home():
    return {"message": "FastAPI is running!"}

# Define the prediction route
@app.get('/predict')
async def predict():
    # Simulate a dummy ML model randomly generating number predictions
    await asyncio.sleep(2)  # Simulate model processing time (2 seconds)
    random_prediction = np.random.rand(5).tolist()
    return {"prediction": random_prediction}




