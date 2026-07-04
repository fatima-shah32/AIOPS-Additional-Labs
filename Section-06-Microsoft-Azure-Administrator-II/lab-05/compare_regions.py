import pandas as pd

df=pd.read_csv("results/latency_results.csv")

print(df)

print()

print("Average Latencies")

print(df.groupby("Metric").mean(numeric_only=True))
