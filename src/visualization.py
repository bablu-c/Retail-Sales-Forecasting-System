import matplotlib.pyplot as plt
import pandas as pd

def plot_sales(df, forecast):
    plt.figure(figsize=(12,6))

    plt.plot(df["date"], df["sales"], label="Actual", color="blue")

    future_dates = pd.date_range(start=df["date"].iloc[-1], periods=len(forecast)+1)[1:]
    plt.plot(future_dates, forecast, label="Forecast", color="red")

    plt.title("Retail Sales Forecast")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.legend()
    plt.grid()

    plt.savefig("outputs/forecast.png")
    plt.show()