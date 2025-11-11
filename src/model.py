from sklearn.ensemble import IsolationForest
import pandas as pd 

def detect_anomalies(df, contamination = 0.05):
    df_numeric = df.select_dtypes(include=["float64","int64"])
    model = IsolationForest(contamination = contamination, random_state = 42)
    preds = model.fit_predict(df_numeric)
    
    df['Anomaly'] = preds
    df['Anomaly'] = df["Anomaly"].map({1:'Normal', -1:'Outlier'})
    return df