import pandas as pd
import numpy as np

def load_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=250)

    trend = np.linspace(50, 100, 250)
    seasonality = 15 * np.sin(np.arange(250) * 2 * np.pi / 7)
    noise = np.random.normal(0, 5, 250)

    promo = np.random.choice([0,1], size=250, p=[0.8,0.2])
    promo_effect = promo * 20

    sales = trend + seasonality + noise + promo_effect

    df = pd.DataFrame({
        "date": dates,
        "sales": sales,
        "promo": promo
    })

    return df