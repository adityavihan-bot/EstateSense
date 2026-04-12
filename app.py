import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st

# Load dataset
house_data = pd.read_csv("house_price.csv")

# Features and target
X_house = house_data[["BHK", "Area"]]
y_house = house_data["Price"]

# Train model
house_model = LinearRegression()
house_model.fit(X_house, y_house)

# Streamlit UI
st.title("🏠 EstateSense")
st.write("Predict House, Flat and Land Prices")

# Inputs
property_type = st.selectbox("Select Property Type", ("House", "Flat", "Land"))

area = st.number_input("Enter Area (sq ft)", min_value=100, step=100)

bhk = 0
if property_type != "Land":
    bhk = st.number_input("Enter BHK", min_value=1, step=1)

# Prediction
if st.button("Predict Price"):

    if area <= 0:
        st.error("Please enter a valid area")
    else:
        # Create DataFrame (IMPORTANT FIX)
        input_data = pd.DataFrame([[bhk, area]], columns=["BHK", "Area"])

        price = house_model.predict(input_data)[0]

        if property_type == "House":
            st.success(f"🏡 Estimated House Price: ₹ {price:,.0f}")

        elif property_type == "Flat":
            st.success(f"🏢 Estimated Flat Price: ₹ {price:,.0f}")

        elif property_type == "Land":
            st.success(f"🌍 Estimated Land Price: ₹ {price:,.0f}")