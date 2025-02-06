import matplotlib.pyplot as plt

input_values = []
squares = []

for value in range(1,6):
    input_values.append(value)
    squares.append(value**2)

print(squares)

plt.style.use('seaborn-v0_8-deep')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=2)
ax.scatter(input_values, squares)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()