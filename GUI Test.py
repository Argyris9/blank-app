import streamlit as st

st.title("🚗 Parking Optimization App")
st.subheader("Find the best parking routes around you!")
st.text("Enter your location and we'll calculate the optimal route to find parking.")

latitude = st.number_input("Enter Latitude:")
longitude = st.number_input("Enter Longitude:")

if st.button("Calculate Best Route"):
    st.success(f"Calculating best route near ({latitude}, {longitude})...")
    # Placeholder: later we'll add your real model here!
