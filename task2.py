# Import the required libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Select the input feature and output label
input_data = df[["Hours"]]
target_data = df["Score"]

# Divide the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    input_data,
    target_data,
    test_size=0.20,
    random_state=42,
    shuffle=True
)

# Build the Linear Regression model
regressor = LinearRegression()

# Train the model using the training data
regressor.fit(x_train, y_train)

# Store the learned parameters
slope = regressor.coef_[0]
intercept = regressor.intercept_

# Display the model equation
print("Linear Regression Model")
print("-----------------------")
print(f"Slope (Coefficient): {slope:.2f}")
print(f"Intercept: {intercept:.2f}")

# Display the regression equation
print(f"\nEquation: Score = {slope:.2f} × Hours + {intercept:.2f}")
