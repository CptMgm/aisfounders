import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 1, 100)
y1 = 0.8 * x  # Adjusted to represent the lower quarter (2-3 on a clock)
y2 = 0.1 * (1 - x)  # Adjusted to represent the upper quarter (12-1 on a clock)

# Plot
plt.fill_between(x, y1, 0, color='lightgrey')
plt.fill_between(x, 1, y2, color='lightgrey')
plt.plot(x, y1, label='80% angle')
plt.plot(x, y2, label='10% angle')

# Dots
dot_sizes = [10, 1, 1, 1]
dot_positions_x = [0.9, 0.1, 0.1, 0.1]  # Adjusted positions for OpenAI, Apart, METR
dot_positions_y = [0.1, 0.9, 0.9, 0.9]  # Adjusted positions for OpenAI, Apart, METR
plt.scatter(dot_positions_x, dot_positions_y, color='red')

# Labels
plt.text(0.9, 0.1, 'OpenAI', fontsize=12, ha='right')
plt.text(0.1, 0.9, 'Apart', fontsize=12, ha='left')
plt.text(0.1, 0.9, 'METR', fontsize=12, ha='left')

# Axes
plt.xlabel('Focus on Profitability')
plt.ylabel('Focus on Reducing Risk of AI')

# Show
plt.legend()
plt.show()