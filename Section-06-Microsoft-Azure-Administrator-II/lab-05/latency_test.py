import os
import time
import statistics
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
from azure.cosmos import CosmosClient

print("=== Cosmos DB Latency Test ===")

endpoint = os.environ.get("COSMOS_ENDPOINT")
key = os.environ.get("COSMOS_KEY")
database_name = os.environ.get("DATABASE_NAME", "GlobalTestDB")
container_name = os.environ.get("CONTAINER_NAME", "TestContainer")

if not endpoint or not key:
    print("ERROR: COSMOS_ENDPOINT and COSMOS_KEY must be set.")
    print("Run: source scripts/export_env.sh")
    exit(1)

client = CosmosClient(endpoint, credential=key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

write_latencies = []
read_latencies = []

print("\nTesting write latency...")

for i in range(10):
    document = {
        "id": f"write-test-{i}-{int(time.time())}",
        "region": "test-region",
        "data": f"Sample document {i}",
        "timestamp": datetime.utcnow().isoformat()
    }

    start = time.time()
    container.create_item(body=document)
    end = time.time()

    latency = (end - start) * 1000
    write_latencies.append(latency)

    print(f"Write {i + 1}: {latency:.2f} ms")

print("\nCreating documents for read test...")

read_doc_ids = []

for i in range(5):
    doc = {
        "id": f"read-test-{i}-{int(time.time())}",
        "region": "read-region",
        "data": f"Read test document {i}",
        "timestamp": datetime.utcnow().isoformat()
    }

    container.create_item(body=doc)
    read_doc_ids.append(doc["id"])

print("\nTesting read latency...")

for i in range(10):
    doc_id = read_doc_ids[i % len(read_doc_ids)]

    start = time.time()
    container.read_item(item=doc_id, partition_key="read-region")
    end = time.time()

    latency = (end - start) * 1000
    read_latencies.append(latency)

    print(f"Read {i + 1}: {latency:.2f} ms")

results = {
    "Metric": [
        "Write Average",
        "Write Median",
        "Write Min",
        "Write Max",
        "Read Average",
        "Read Median",
        "Read Min",
        "Read Max"
    ],
    "Latency_ms": [
        statistics.mean(write_latencies),
        statistics.median(write_latencies),
        min(write_latencies),
        max(write_latencies),
        statistics.mean(read_latencies),
        statistics.median(read_latencies),
        min(read_latencies),
        max(read_latencies)
    ]
}

df = pd.DataFrame(results)
df.to_csv("results/latency_results.csv", index=False)

plt.figure(figsize=(8, 5))
plt.plot(write_latencies, label="Write Latency")
plt.plot(read_latencies, label="Read Latency")
plt.xlabel("Operation Number")
plt.ylabel("Latency ms")
plt.title("Cosmos DB Read/Write Latency")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/latency_chart.png")
plt.close()

with open("reports/latency_report.txt", "w") as report:
    report.write("Cosmos DB Latency Test Report\n\n")
    report.write(df.to_string(index=False))
    report.write("\n\nConclusion:\n")
    report.write("Read and write latency tests completed successfully.\n")

print("\nLatency test completed.")
print("Saved results/latency_results.csv")
print("Saved results/latency_chart.png")
print("Saved reports/latency_report.txt")
