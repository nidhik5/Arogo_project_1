from flask import Flask, render_template, request
import pandas as pd
import joblib
import plotly.express as px
import os

app = Flask(__name__)

# Load the pre-trained model
MODEL_PATH = 'best_model.joblib'
best_model = joblib.load(MODEL_PATH)

# Function for prediction
def predict_delay(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = best_model.predict(input_df)
    return 'Yes' if prediction[0] == 1 else 'No'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    input_data = {
        'Distance (km)': float(request.form['distance']),
        'Origin': request.form['origin'],
        'Destination': request.form['destination'],
        'Vehicle Type': request.form['vehicle_type'],
        'Weather Conditions': request.form['weather_conditions'],
        'Traffic Conditions': request.form['traffic_conditions'],
    }

    # Make prediction
    prediction = predict_delay(input_data)

    # Load data and calculate additional columns for graphing
    df = pd.read_excel('data.xlsx')

    # Calculate Delay Duration
    df['Delay Duration'] = (df['Actual Delivery Date'] - df['Planned Delivery Date']).dt.days.abs()

    # Example graph 1: Planned Transit Time
    df['Planned Transit Time'] = (
        pd.to_datetime(df['Planned Delivery Date']) - pd.to_datetime(df['Shipment Date'])
    ).dt.days
    fig1 = px.histogram(
        df, x='Planned Transit Time', nbins=10, color='Delayed',
        title="Distribution of Planned Transit Times",
        labels={'Planned Transit Time': 'Transit Time (Days)'}
    )
    graph1 = fig1.to_html(full_html=False)

    # Example graph 2: Distance vs Delay
    fig2 = px.scatter(
        df, x='Distance (km)', y='Delay Duration', color='Delayed',
        title="Distance vs. Delay Duration",
        labels={'Distance (km)': 'Distance (km)', 'Delay Duration': 'Delay Duration (Days)'}
    )
    graph2 = fig2.to_html(full_html=False)

    return render_template('result.html', prediction=prediction, graph1=graph1, graph2=graph2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
