import streamlit as st
import pandas as pd

st.set_page_config(page_title="ML Model", page_icon="📈")

st.markdown("# Machine Learning Model Selection")
st.sidebar.header("Select Model")

# Fetch data from session state
data = st.session_state.data

classifier_name = st.sidebar.selectbox("Select Classifier", ("KNN", "SVM", "Decision Tree"))