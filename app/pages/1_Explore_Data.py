import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

@st.cache_data
def load_data():
    data = pd.read_csv('./data/customer_churn.csv')
    return data

st.set_page_config(page_title="Customer Churn Data Visualization", page_icon="📈")

st.markdown("# Explore Dataset")
st.sidebar.header("Navigation")
st.sidebar.markdown('''
- [Raw data](#raw-data)
- [Correlation Heatmap](#correlation-heatmap)
''', unsafe_allow_html=True)

# Load the data and store it in a session state so it can be accessed across different pages
if 'data' not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data


## --- Raw Data --- ##

if st.checkbox("Show raw data"):
    st.subheader("Raw data")

    # User Control for number of rows to display
    rows_option = st.slider("Select number of rows to display", min_value=5, max_value=50, value=15, step=5)

    # Pagination
    page_size = rows_option
    page_number = st.number_input("Page Number", min_value=1, max_value=(len(data) // page_size) + 1, step=1, value=1)

    # Calculate the start and end indices of the current page
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size

    # Display the shape of the dataset
    __shape__ = data.shape
    st.write("Dataset contains", __shape__[0]," rows and ", __shape__[1], "columns.")

    # Display the data for the current page
    st.table(data.iloc[start_idx:end_idx])

## --- Heatmap --- ##

st.subheader("Correlation Heatmap")
corr_matrix = data.corr()
fig = ff.create_annotated_heatmap(
    z=corr_matrix.values[::-1],  # Reverse the order of rows for the heatmap
    x=list(corr_matrix.columns), 
    y=list(corr_matrix.index)[::-1],  # Reverse the Y-axis labels
    annotation_text=corr_matrix.round(3).values[::-1].astype(str),  # Reverse the annotations
    colorscale='YlGnBu'
)
st.plotly_chart(fig, use_container_width=True)