def add_parameter_ui(clf_name):
    """Adds hyperparameters tuning UI, based on the selected classifier

    Parameters
    ----------
    clf_name : str
        Name of the classifier chosen

    Returns
    -------
    params
        a dictionnary of the selected hyperparameters values
    """
    
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
