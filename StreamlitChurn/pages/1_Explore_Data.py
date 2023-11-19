import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv("./Customer Churn.csv")
    return data

st.set_page_config(page_title="Customer Churn Data Visualization", page_icon="📈")

st.markdown("# Explore Dataset")
st.sidebar.header("Explore Dataset")

# Load the data
data = load_data()

# User Control for number of rows to display
rows_option = st.slider('Select number of rows to display', min_value=5, max_value=100, value=25, step=5)
st.write(f"Displaying {rows_option} rows of data")

# Pagination
page_size = rows_option
page_number = st.number_input('Page Number', min_value=1, max_value=(len(data) // page_size) + 1, step=1, value=1)

# Calculate the start and end indices of the current page
start_idx = (page_number - 1) * page_size
end_idx = start_idx + page_size

# Display the data for the current page
st.table(data.iloc[start_idx:end_idx])