import matplotlib.pyplot as plt
from collections import Counter

# Function to clean and validate numbers
def clean_number(number):
    number = number.strip().lstrip('0') or '0'
    return number

# Read and clean the data from the file
with open('aime_scores.txt', 'r') as file:
    # Clean and validate numbers
    data = []
    for line in file:
        cleaned_number = clean_number(line)
        if cleaned_number.isdigit() and len(cleaned_number) <= 3:  # Ensure it's a valid number
            data.append(cleaned_number)

# Count the frequency of each number
frequency = Counter(data)

# Sort the frequencies by number
sorted_frequency = dict(sorted(frequency.items(), key=lambda item: int(item[0])))

# Prepare data for plotting
numbers = sorted(sorted_frequency.keys(), key=int)
frequencies = [sorted_frequency[number] for number in numbers]

# Plotting the data
plt.figure(figsize=(12, 6))
plt.bar(numbers, frequencies, color='skyblue')
plt.xlabel('Answer Numbers')
plt.ylabel('Frequency')
plt.title('Frequency of AIME Answer Numbers')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot to a file
plt.savefig('aime_frequencies.png')

# Show the plot
plt.show()
