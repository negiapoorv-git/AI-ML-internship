import pandas as pd

# Sample student performance data
student_data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Score": [35, 45, 48, 52, 60, 68, 75, 82, 88, 95]
}

# Build the DataFrame
students_df = pd.DataFrame(student_data)

# Display a preview of the dataset
print("Dataset Preview:")
print(students_df.head())

# Find any missing values
print("\nMissing Values in Each Column:")
missing = students_df.isna().sum()
print(missing)

# Generate summary statistics
print("\nSummary Statistics:")
summary = students_df.describe()
print(summary)
