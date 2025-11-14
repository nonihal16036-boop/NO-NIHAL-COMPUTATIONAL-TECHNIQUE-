# Python program to compute mean, median, and mode for grouped data

# Grouped data
classes = [(15, 25), (25, 35), (35, 45), (45, 55), (55, 65)]
frequencies = [350, 375, 120, 80, 90]

# Step 1: Calculate Mean
midpoints = [(c[0] + c[1]) / 2 for c in classes]
fx = [midpoints[i] * frequencies[i] for i in range(len(classes))]
mean = sum(fx) / sum(frequencies)

# Step 2: Calculate Median
N = sum(frequencies)
median_class_index = 0
cumulative = 0

for i, f in enumerate(frequencies):
    cumulative += f
    if cumulative >= N / 2:
        median_class_index = i
        break

L = classes[median_class_index][0]   # lower limit of median class
F = sum(frequencies[:median_class_index])  # cumulative frequency before median class
f = frequencies[median_class_index]        # frequency of median class
h = classes[median_class_index][1] - classes[median_class_index][0]  # class width

median = L + ((N/2 - F) / f) * h

# Step 3: Calculate Mode
modal_class_index = frequencies.index(max(frequencies))

L = classes[modal_class_index][0]
f1 = frequencies[modal_class_index]
f0 = frequencies[modal_class_index - 1] if modal_class_index > 0 else 0
f2 = frequencies[modal_class_index + 1] if modal_class_index < len(frequencies)-1 else 0
h = classes[modal_class_index][1] - classes[modal_class_index][0]

mode = L + ((f1 - f0) / (2*f1 - f0 - f2)) * h

# Output Results
print("Mean  :", mean)
print("Median:", median)
print("Mode  :", mode)
