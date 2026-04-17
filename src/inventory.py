import numpy as np

def inventory_logic(forecast):
    demand_mean = np.mean(forecast)
    demand_std = np.std(forecast)

    lead_time = 5   # days
    service_level = 1.65  # ~95%

    safety_stock = service_level * demand_std * np.sqrt(lead_time)
    reorder_point = demand_mean * lead_time + safety_stock

    return {
        "Avg Demand": round(demand_mean,2),
        "Std Dev": round(demand_std,2),
        "Safety Stock": round(safety_stock,2),
        "Reorder Point": round(reorder_point,2)
    }