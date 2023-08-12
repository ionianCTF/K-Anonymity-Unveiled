#import libraries
import csv
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np

def microaggregate(data, column, k):
    # Find unique values in the column
    unique_vals = np.unique(data[column])
    # Create a dictionary to store the aggregated values
    aggregated_vals = {}
    for val in unique_vals:
        # Find the indices of all rows with the same value
        indices = np.where(data[column] == val)[0]
        # Aggregate the values by finding the mean
        mean = np.mean(data.iloc[indices][column])
        # Store the aggregated value in the dictionary
        aggregated_vals[val] = mean
    # Replace the original values with the aggregated values
    for index, row in data.iterrows():
        data.at[index, column] = aggregated_vals[row[column]]
    return data

def k_anonymize(file_path, k, quasiidentifiers, generalization_intervals={}):
    # Read the CSV file
    anon_rows = 0
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
        row_count = len(data)
    # Find the indices of the quasiidentifiers
    quasi_indices = [header.index(feature) for feature in quasiidentifiers]

    # Perform the generalization of attributes if necessary
    for attribute, interval in generalization_intervals.items():
        attribute_index = header.index(attribute)
        for row in data:
            row[attribute_index] = str(int(np.floor(float(row[attribute_index])/interval)) * interval) + "-" + str((int(np.floor(float(row[attribute_index])/interval)) + 1) * interval)

    # Create a dictionary to store the count of each combination of quasiidentifier values
    counts = {}

    # Count the occurrences of each combination of quasiidentifier values
    for row in data:
        value = tuple([row[i] for i in quasi_indices])
        counts[value] = counts.get(value, 0) + 1

    # Perform the k-anonymization
    for row in data:
        value = tuple([row[i] for i in quasi_indices])
        if counts[value] < k:
            for i in quasi_indices:
                row[i] = '*' * len(row[i])
            anon_rows = anon_rows + 1
    percentage = (anon_rows/row_count)*100

    # Write the anonymous data to a new CSV file
    with open('/content/sample_data/anonymised.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
    return percentage

#Example Execution
    
#k_anonymize('/content/sample_data/heart.csv', 3, ["Age","Cholesterol"])
#anon_percentage=k_anonymize('/content/sample_data/heart.csv', 10, ["Age","Cholesterol"], generalization_intervals={"Age": 15})
#k_anonymize('/content/sample_data/heart.csv', 3, ["Cholesterol","FastingBS"], generalization_intervals={"Cholesterol": 80})
