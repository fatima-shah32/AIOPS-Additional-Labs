import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from prophet import Prophet

print("=== Lab 04: SysOps System Health Prediction ===")

# Generate simulated system logs
np.random.seed(42)

timestamps = pd.date_range(
    start="2023-01-01",
    periods=1000,
    freq="h"
)

status = np.random.choice(
    [0, 1],
    size=1000,
    p=[0.1, 0.9]
)

df = pd.DataFrame({
    "timestamp": timestamps,
    "status": status
})

df.to_csv("results/system_logs.csv", index=False)

print("\nSystem logs created:")
print(df.head())

# Convert system status into daily uptime average
df["date"] = df["timestamp"].dt.date

daily_status = df.groupby("date")["status"].mean().reset_index()

# Downtime percentage = 1 - uptime average
daily_status["downtime_percentage"] = 1 - daily_status["status"]

forecast_data = daily_status[["date", "downtime_percentage"]]
forecast_data.columns = ["ds", "y"]

forecast_data["ds"] = pd.to_datetime(forecast_data["ds"])

forecast_data.to_csv("results/daily_downtime.csv", index=False)

print("\nDaily downtime data:")
print(forecast_data.head())

# Train Prophet model
model = Prophet()

model.fit(forecast_data)

# Forecast next 30 days
future = model.make_future_dataframe(periods=30)

forecast = model.predict(future)

forecast_output = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

forecast_output.to_csv("results/downtime_forecast.csv", index=False)

print("\nForecast preview:")
print(forecast_output.tail())

# Plot forecast
fig1 = model.plot(forecast)

plt.title("System Downtime Forecast")
plt.xlabel("Date")
plt.ylabel("Predicted Downtime Percentage")
plt.tight_layout()
plt.savefig("results/system_downtime_forecast.png")
plt.close()

# Plot forecast components
fig2 = model.plot_components(forecast)

plt.tight_layout()
plt.savefig("results/forecast_components.png")
plt.close()

# Create simple downtime risk report
future_forecast = forecast_output.tail(30).copy()

average_predicted_downtime = future_forecast["yhat"].mean()
highest_predicted_downtime = future_forecast["yhat"].max()

risk_level = "Low"

if highest_predicted_downtime > 0.20:
    risk_level = "High"
elif highest_predicted_downtime > 0.10:
    risk_level = "Medium"

with open("reports/final_report.txt", "w") as report:
    report.write("Lab 04: SysOps System Health Prediction with Time Series Analysis\n\n")
    report.write("Objective:\n")
    report.write("Use time series forecasting to predict future system downtimes or disruptions.\n\n")
    report.write("Dataset:\n")
    report.write("Simulated hourly system logs with system status.\n\n")
    report.write("Model Used:\n")
    report.write("Facebook Prophet\n\n")
    report.write("Results:\n")
    report.write(f"Average Predicted Downtime: {average_predicted_downtime:.4f}\n")
    report.write(f"Highest Predicted Downtime: {highest_predicted_downtime:.4f}\n")
    report.write(f"Risk Level: {risk_level}\n\n")
    report.write("Files Generated:\n")
    report.write("- system_logs.csv\n")
    report.write("- daily_downtime.csv\n")
    report.write("- downtime_forecast.csv\n")
    report.write("- system_downtime_forecast.png\n")
    report.write("- forecast_components.png\n\n")
    report.write("Conclusion:\n")
    report.write("Prophet successfully forecasted future system downtime trends based on historical system logs.\n")

print("\nLab completed successfully.")
print("Risk Level:", risk_level)
