import streamlit as st

# Title
st.title("🧮 Simple Calculator App")

# Input numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Operation selector
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation
def calculate(n1, n2, op):
    if op == "Add":
        return n1 + n2
    elif op == "Subtract":
        return n1 - n2
    elif op == "Multiply":
        return n1 * n2
    elif op == "Divide":
        if n2 == 0:
            return "❌ Error: Division by zero"
        return n1 / n2

# Calculate when button is pressed
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")
