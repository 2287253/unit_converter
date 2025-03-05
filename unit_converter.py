import streamlit as st
import pandas as pd

def length_conversion(value, from_unit, to_unit):
    # Base unit is meters
    length_factors = {
        'Kilometers': 1000,
        'Meters': 1,
        'Centimeters': 0.01,
        'Millimeters': 0.001,
        'Miles': 1609.34,
        'Yards': 0.9144,
        'Feet': 0.3048,
        'Inches': 0.0254
    }
    # Convert to base unit first, then to target unit
    return value * length_factors[from_unit] / length_factors[to_unit]

def weight_conversion(value, from_unit, to_unit):
    # Base unit is kilograms
    weight_factors = {
        'Tonnes': 1000,
        'Kilograms': 1,
        'Grams': 0.001,
        'Milligrams': 0.000001,
        'Pounds': 0.453592,
        'Ounces': 0.0283495
    }
    return value * weight_factors[from_unit] / weight_factors[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄")
    
    # Add custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 20px;
        }
        .stButton>button {
            width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.title("📐 Unit Converter")
    st.write("Convert between different units of measurement")
    
    # Create tabs for different conversion types
    tab1, tab2, tab3 = st.tabs(["Length", "Weight", "Temperature"])
    
    with tab1:
        st.header("Length Conversion")
        length_units = ['Kilometers', 'Meters', 'Centimeters', 'Millimeters', 
                       'Miles', 'Yards', 'Feet', 'Inches']
        
        col1, col2 = st.columns(2)
        with col1:
            length_value = st.number_input("Enter Length", value=0.0, key="length")
            from_length = st.selectbox("From", length_units, key="from_length")
        with col2:
            to_length = st.selectbox("To", length_units, key="to_length")
            if st.button("Convert Length"):
                result = length_conversion(length_value, from_length, to_length)
                st.success(f"{length_value} {from_length} = {result:.4f} {to_length}")
    
    with tab2:
        st.header("Weight Conversion")
        weight_units = ['Tonnes', 'Kilograms', 'Grams', 'Milligrams', 
                       'Pounds', 'Ounces']
        
        col1, col2 = st.columns(2)
        with col1:
            weight_value = st.number_input("Enter Weight", value=0.0, key="weight")
            from_weight = st.selectbox("From", weight_units, key="from_weight")
        with col2:
            to_weight = st.selectbox("To", weight_units, key="to_weight")
            if st.button("Convert Weight"):
                result = weight_conversion(weight_value, from_weight, to_weight)
                st.success(f"{weight_value} {from_weight} = {result:.4f} {to_weight}")
    
    with tab3:
        st.header("Temperature Conversion")
        temp_units = ['Celsius', 'Fahrenheit', 'Kelvin']
        
        col1, col2 = st.columns(2)
        with col1:
            temp_value = st.number_input("Enter Temperature", value=0.0, key="temp")
            from_temp = st.selectbox("From", temp_units, key="from_temp")
        with col2:
            to_temp = st.selectbox("To", temp_units, key="to_temp")
            if st.button("Convert Temperature"):
                result = temperature_conversion(temp_value, from_temp, to_temp)
                st.success(f"{temp_value} {from_temp} = {result:.2f} {to_temp}")
    
    # Add footer
    st.markdown("---")
    st.markdown("Built with ❤️ using Streamlit")

if __name__ == "__main__":
    main()
