import streamlit as st
import pandas as pd
import utils.functions as f

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

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

st.divider()
st.write(f"**Model selected**:", classifier_name)
st.write(f"**Hyperparameters values**:", params)
st.write(f"**Accuracy score**:", round(acc, 4))
st.divider()

# keep 2 dimensions so we can plot it
pca = PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap='viridis')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()

st.pyplot(fig)