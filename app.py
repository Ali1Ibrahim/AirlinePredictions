import streamlit as st
import pandas as pd
import joblib

Model = joblib.load("Final_Model.pkl")
Inputs = joblib.load("Inputs.pkl")

def get_prediction(Airline, Source, Destination, Day_In_Numbers, Stops, Arrival_Period, Duration_Cat, Distance_Cat, Meal):
    df = pd.DataFrame(columns=Inputs)
    df.at[0, "Airline"] = Airline
    df.at[0, 'Source'] = Source
    df.at[0, 'Destination'] = Destination
    df.at[0, 'Stops'] = Stops
    df.at[0, 'Day_In_Numbers'] = Day_In_Numbers
    df.at[0, 'Arrival_Period'] = Arrival_Period
    df.at[0, 'Duration_Cat'] = Duration_Cat
    df.at[0, 'Distance_Cat'] = Distance_Cat
    df.at[0, 'Meal'] = Meal
    results = Model.predict(df)
    return results[0]

def get_period(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    elif 18 <= hour < 23:
        return "Evening"
    else:
        return "Night"

def categorize(duration):
    if duration < 750:
        return "Short"
    elif duration <= 1500:
        return "Medium"
    else:
        return "Long"

def Main():
    Airline = st.selectbox("Airline", ['Air India', 'Jet Airways', 'IndiGo', 'SpiceJet', 'GoAir', 'Vistara', 'Air Asia'])
    Source = st.selectbox("Source", ['Kolkata', 'Delhi', 'Banglore'])
    Destination = st.selectbox("Destination", ['Banglore', 'Cochin', 'New Delhi', 'Delhi'])
    Stops = st.selectbox("Stops", [2, 1, 0])
    Day_In_Numbers = st.selectbox("Day_In_Numbers", range(1, 32))
    Arrival_Period = st.selectbox("Arrival_Period", ['Morning', 'Afternoon', 'Evening', 'Night'])
    Duration = st.slider("Duration", min_value=100, max_value=1000, value=120, step=20)
    Duration_Cat = categorize(Duration)
    Distance_Cat = st.selectbox("Distance_Cat", ['Short', 'Medium', 'Long'])
    Meal = st.selectbox("Meal", [1, 0])
    
    if st.button("Predict"):
        results = get_prediction(Airline, Source, Destination, Day_In_Numbers, Stops, Arrival_Period, Duration_Cat, Distance_Cat, Meal)
        st.text(f"The Estimated Price of Flight is {results}")

Main()
