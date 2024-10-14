import matplotlib.pyplot as plt

# Data for years 1985 to 2024
years = list(range(1985, 2025))  # 40 values for years
world_population = [
    4868943465, 4958072838, 5049746397, 5141992542, 5234431732, 5327803110, 5421043738, 5515551255,
    5611220598, 5705787982, 5801154122, 5898310247, 5995826228, 6093000000, 6190361634, 6288617388,
    6386973015, 6485455013, 6584848183, 6684964791, 6785617954, 6886544952, 6988129365, 7091732954,
    7194928344, 7298902138, 7403253445, 7508351083, 7613248990, 7718355301, 7823326573, 7928624266,
    8034697555, 8141972572, 8249439648, 8346123982, 8436357555, 8524695528, 8597822842, 8653490024
]  # 40 values

yearly_change = [
    1.81, 1.83, 1.85, 1.83, 1.85, 1.80, 1.78, 1.71, 1.61, 1.55, 1.50, 1.47, 1.44, 1.42, 1.39, 1.36,
    1.35, 1.32, 1.30, 1.29, 1.29, 1.28, 1.27, 1.27, 1.26, 1.23, 1.20, 1.18, 1.15, 1.12, 1.10, 1.08,
    1.05, 1.03, 1.01, 0.98, 0.95, 0.92, 0.89, 0.87
]  # 40 values

# Plotting the data
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot World Population
ax1.set_xlabel('Year')
ax1.set_ylabel('World Population', color='b')
ax1.plot(years, world_population, label='World Population', color='b', marker='o')
ax1.tick_params(axis='y', labelcolor='b')

# Create a second y-axis for the Yearly Change (%)
ax2 = ax1.twinx()  
ax2.set_ylabel('Yearly Change (%)', color='r')
ax2.plot(years, yearly_change, label='Yearly Change (%)', color='r', marker='x')
ax2.set_ylim(0, 2.5)  # Set y-axis limit for percentage
ax2.tick_params(axis='y', labelcolor='g')

# Set title and grid
plt.title('World Population vs Yearly Change (%) Over Time (1985-2024)')
ax1.grid(True)
plt.xticks(rotation=45)

# Show the chart
plt.tight_layout()
plt.show()
