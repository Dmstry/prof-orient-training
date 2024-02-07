colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
filtered_colors = [color for i, color in enumerate(colors) if i not in [0, 4, 5]]
print(filtered_colors)
