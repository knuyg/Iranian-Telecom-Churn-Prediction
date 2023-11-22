import streamlit as st
import pandas as pd

def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == "KNN":
        K = st.sidebar.slider("K", 1, 15)
        params["K"] = K
    elif clf_name == "SVM":
        C = st.sidebar.slider("K", 0.01, 10.0)
        params["C"] = C
    elif clf_name == "Decision Tree":
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 1, 100)
        params["max_depth"] = max_depth
        params["n_estimators"] = n_estimators
    return params

st.set_page_config(page_title="ML Model", page_icon="📈")

st.markdown("# Machine Learning Model Selection")
st.sidebar.header("Select Model")

# Fetch data from session state
data = st.session_state.data

classifier_name = st.sidebar.selectbox("Select model", ("KNN", "SVM", "Decision Tree"), label_visibility="collapsed")

st.sidebar.subheader("Hyperparameters tuning")

add_parameter_ui(classifier_name)