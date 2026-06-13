import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Histogram
# -----------------------------
data = np.random.randn(1000)

plt.figure(figsize=(8,6))
plt.hist(
    data,
    bins=30,
    color='skyblue',
    edgecolor='black'
)

plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.savefig('histogram.png')
plt.close()

print("Histogram saved as histogram.png")

# -----------------------------
# Scatter Plot
# -----------------------------
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(8,6))
plt.scatter(
    x,
    y,
    color='red',
    edgecolor='black',
    marker='o'
)

plt.title('Random Scatter Plot')
plt.xlabel('X Value')
plt.ylabel('Y Value')

plt.savefig('scatter_plot.png')
plt.close()

print("Scatter plot saved as scatter_plot.png")

# -----------------------------
# Line Chart
# -----------------------------
x = np.linspace(0,10,100)
y = np.sin(x)

plt.figure(figsize=(8,6))

plt.plot(
    x,
    y,
    label='sin(x)',
    color='green',
    linewidth=2,
    linestyle='--'
)

plt.title('Line Chart of sin(x)')
plt.xlabel('X')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)

plt.savefig('line_chart.png')
plt.close()

print("Line chart saved as line_chart.png")

# -----------------------------
# Bar Chart
# -----------------------------
categories = ['A','B','C','D','E']
values = [3,7,2,5,4]

plt.figure(figsize=(8,6))

plt.bar(
    categories,
    values,
    color='orange',
    edgecolor='black'
)

plt.title('Bar Chart of Categories')
plt.xlabel('Category')
plt.ylabel('Value')

plt.savefig('bar_chart.png')
plt.close()

print("Bar chart saved as bar_chart.png")

print("\nLab completed successfully.")
