def preprocess(df):
    df = df.dropna()
    df["day"] = df["date"].dt.dayofweek
    return df