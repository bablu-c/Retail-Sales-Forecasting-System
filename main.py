from src.data_loader import load_data
from src.preprocessing import preprocess
from src.model import train_model, predict
from src.inventory import inventory_logic
from src.visualization import plot_sales

df = load_data()
df = preprocess(df)

model = train_model(df)
forecast = predict(model, df)

inventory = inventory_logic(forecast)

plot_sales(df, forecast)

print(inventory.head())

print("\n📦 Inventory Recommendation:")
for key, value in inventory.items():
    print(f"{key}: {value}")