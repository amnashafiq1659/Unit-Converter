import streamlit as st 
import pandas as pd   
import io
from io import BytesIO 
from conversion import conversions, unit_categories, unit_names

st.set_page_config(page_title="UnitX: Convert with Ease ⚡", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state for conversion history
if "conversion_history" not in st.session_state:
    st.session_state.conversion_history = []

# Define the convert_unit function
def convert_unit(value, unit_from, unit_to): 
    key = f"{unit_from}_{unit_to}" #Generate a key based on the unit_from and unit_to

    if key in conversions:
        conversion = conversions[key]
        return value * conversion

# Define the title
st.title("UnitX: Convert with Ease ⚡")

category = st.selectbox("Select Category", list(unit_categories.keys()))

# Define the input fields
value = st.number_input("Enter the value to convert", min_value=1)
if category:
    units = unit_categories[category]
    unit_from = st.selectbox("Select the unit to convert from", units)
    unit_to = st.selectbox("Select the unit to convert to", units)

# Define the convert button
if st.button("Convert"):
        result = convert_unit(value, unit_from, unit_to)

        if result is None:
            st.error("⚠️ Conversion not supported! Please select valid units.")
        else:
            # Store structured history
            conversion_text = {
                "Value": value, 
                "From": unit_names[unit_from], 
                "To": unit_names[unit_to], 
                "Result": result
            }
            st.session_state.conversion_history.append(conversion_text)
            
            st.success(f"✅ {value} {unit_names[unit_from]} successfully converted to {result} {unit_names[unit_to]}.")


# Sidebar: Display Conversion History
st.sidebar.title("🕒 Conversion History")
st.sidebar.markdown("---")

# Sidebar: Display  History
if len(st.session_state.conversion_history) > 0:
    for entry in reversed(st.session_state.conversion_history[-10:]):  
        st.sidebar.write(entry)
else:
    st.sidebar.write("No history yet! Convert a unit to see history.")
st.sidebar.markdown("---")

# Sidebar: Clear history button
if st.sidebar.button("🗑 Clear History"):
    st.session_state.conversion_history.clear()
    st.sidebar.success("History cleared!")
    st.rerun()

#Define download conversion button in csv format
if st.session_state.conversion_history:
    df = pd.DataFrame(st.session_state.conversion_history)
    json_data = df.to_json(orient="records",indent=4)
    buffer = io.BytesIO()
    buffer.write(json_data.encode())
    buffer.seek(0)
    st.sidebar.download_button(
        label="📥 Download Conversions",
        data= buffer,
        file_name="conversion_history.json", 
        mime="application/json")

# Define the footer
st.markdown("---")
st.write("Made with ❤️ by Amna Shafiq")
