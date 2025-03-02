import streamlit as st
import matplotlib.pyplot as plt

st.title("Length Conversion")

length_units = {
    "Millimeter (mm)": 0.001,
    "Centimeter (cm)": 0.01,
    "Meter (m)": 1,
    "Kilometer (km)": 1000,
    "Inch (in)": 0.0254,
    "Foot (ft)": 0.3048,
    "Yard (yd)": 0.9144,
    "Mile (mi)": 1609.34
}

from_unit = st.selectbox("From Unit", list(length_units.keys()))
to_unit = st.selectbox("To Unit", list(length_units.keys()))
value = st.number_input("Enter Value", min_value=0.0, step=1.0, value=1.0, format="%.2f")

converted_value = (value * length_units[from_unit]) / length_units[to_unit]

st.write(f"### {value} {from_unit} is equal to {converted_value:.2f} {to_unit}")

# Graph
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar([from_unit, to_unit], [value, converted_value], color=['blue', 'green'])
ax.set_xlabel("Units")
ax.set_ylabel("Values")
st.pyplot(fig)
