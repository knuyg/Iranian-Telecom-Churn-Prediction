import streamlit as st
import pandas as pd
import utils.functions as f

st.set_page_config(page_title="ML Model", page_icon="📈")

st.markdown("# Machine Learning Model Selection")
st.sidebar.header("Select Model")

# Fetch data from session state
data = st.session_state.data

classifier_name = st.sidebar.selectbox("Select model", ("KNN", "SVM", "Decision Tree"), label_visibility="collapsed")

# Select classifier hyperparameters
st.sidebar.subheader("Hyperparameters tuning")

params = f.add_parameter_ui(classifier_name)
clf = f.get_classifier(classifier_name, params)

# Train model

# later: put it into the preprocessing file and replace it
X = data.drop(columns=['Churn'])
y = data['Churn']
y_pred, acc = f.predict(clf, X, y)

st.write(f"accuracy score:", acc)