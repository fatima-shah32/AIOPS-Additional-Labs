import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from prophet import Prophet

print("="*60)
print("Lab 05 : SysOps Alert Forecasting with Prophet")
print("="*60)

# -----------------------------
# Generate Historical Data
# -----------------------------

np.random.seed(42)

dates = pd.date_range(
    start="2024-01-01",
    end="2024-12-31",
    freq="D"
)

alerts = np.random.poisson(
    lam=5,
    size=len(dates)
)

df = pd.DataFrame({
    "ds": dates,
    "y": alerts
})

df.to_csv("historical_alerts.csv", index=False)

print("\nHistorical data saved.")

# -----------------------------
# Train Prophet
# -----------------------------

model = Prophet(
    daily_seasonality=True
)

model.fit(df)

future = model.make_future_dataframe(
    periods=30
)

forecast = model.predict(future)

forecast[
    [
        "ds",
        "yhat",
        "yhat_lower",
        "yhat_upper"
    ]
].to_csv(
    "forecast_results.csv",
    index=False
)

print("Forecast generated.")

# -----------------------------
# Forecast Plot
# -----------------------------

fig1 = model.plot(forecast)

plt.title("Forecast of System Alerts")

plt.savefig(
    "alert_forecast.png"
)

plt.close()

# -----------------------------
# Components Plot
# -----------------------------

fig2 = model.plot_components(forecast)

plt.savefig(
    "forecast_components.png"
)

plt.close()

# -----------------------------
# Report
# -----------------------------

with open(
    "sysops_forecast_report.txt",
    "w"
) as report:

    report.write(
        "Lab 05\n"
    )

    report.write(
        "SysOps Alert Forecasting using Prophet\n\n"
    )

    report.write(
        "Historical Samples : {}\n".format(
            len(df)
        )
    )

    report.write(
        "Forecast Days : 30\n\n"
    )

    report.write(
        "Model : Facebook Prophet\n\n"
    )

    report.write(
        "Outputs Generated:\n"
    )

    report.write(
        "- historical_alerts.csv\n"
    )

    report.write(
        "- forecast_results.csv\n"
    )

    report.write(
        "- alert_forecast.png\n"
    )

    report.write(
        "- forecast_components.png\n"
    )

print("\nReport Generated Successfully.")

print("\nForecast Preview:\n")

print(
    forecast[
        [
            "ds",
            "yhat"
        ]
    ].tail()
)

print("\nLab Completed Successfully.")
