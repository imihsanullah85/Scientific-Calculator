# streamlit_app.py
import streamlit as st
import math

# Title
st.title("Scientific Calculator")

# Input fields
st.write("Enter numbers and select the operation to perform:")

# User inputs
num1 = st.number_input("Enter the first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter the second number (if needed):", value=0.0, step=1.0)

# Select operation
operation = st.selectbox(
    "Select an operation",
    ("Addition", "Subtraction", "Multiplication", "Division", 
     "Square Root", "Power", "Sine", "Cosine", "Tangent")
)

# Perform calculation based on selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif operation == "Square Root":
        result = math.sqrt(num1) if num1 >= 0 else "Error: Negative number"
    elif operation == "Power":
        result = math.pow(num1, num2)
    elif operation == "Sine":
        result = math.sin(math.radians(num1))
    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
    elif operation == "Tangent":
        result = math.tan(math.radians(num1))
    
    st.write("Result:", result)
