import streamlit as st
import pandas as pd
import utils.functions as f

st.set_page_config(page_title="ML Model", page_icon="📈")

st.markdown("# Machine Learning Model Selection")
st.sidebar.header("Select Model")

# Fetch data from session state
data = st.session_state.data

classifier_name = st.sidebar.selectbox("Select model", ("KNN", "SVM", "Decision Tree"), label_visibility="collapsed")

st.sidebar.subheader("Hyperparameters tuning")

params = f.add_parameter_ui(classifier_name)
f.get_classifier(classifier_name, params)