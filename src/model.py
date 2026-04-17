from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def create_features(df):
    df["day"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["lag_1"] = df["sales"].shift(1)
    df["lag_7"] = df["sales"].shift(7)

    df = df.dropna()
    return df

def train_model(df):
    df = create_features(df)

    X = df[["day", "month", "lag_1", "lag_7", "promo"]]
    y = df["sales"]

    model = RandomForestRegressor(n_estimators=200)
    model.fit(X, y)

    return model, df

def predict(model, df):
    last_row = df.iloc[-1:].copy()

    future = []
    for i in range(7):
        row = last_row.copy()
        row["day"] = (row["day"] + 1) % 7

        pred = model.predict(row[["day","month","lag_1","lag_7","promo"]])[0]
        future.append(pred)

        row["lag_1"] = pred
        last_row = row

    return future