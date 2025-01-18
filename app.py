# calculator_app.py
import streamlit as st

def main():
    st.title("Simple Calculator")
    
    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)
    
    # Operation selector
    operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])
    
    # Perform calculation
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
                result = "Error! Division by zero."
        
        st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()
