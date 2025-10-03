import streamlit as st
import pandas as pd
import numpy as np
import os

# --- Title ---
st.title("🎉 Simple Streamlit App")

st.write("This is a beginner-friendly Streamlit project!")

# --- User Input ---
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)

if name:
    st.success(f"Hello, {name}! You are {age} years old.")

# --- Load or Create Sample Data ---
file_path = "data/sample.csv"
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    os.makedirs("data", exist_ok=True)
    data = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['Column A', 'Column B', 'Column C']
    )
    data.to_csv(file_path, index=False)

# --- Display Data ---
st.write("### Sample Data Table:")
st.dataframe(data)

# --- Line Chart ---
st.write("### Line Chart:")
st.line_chart(data)

# --- Button Action ---
if st.button("Click Me"):
    st.info("You clicked the button! ✅")
