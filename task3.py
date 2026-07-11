from sklearn.metrics import mean_absolute_error
import pandas as pd

# Generate predictions using the test dataset
predicted_values = regressor.predict(x_test)

# Calculate Mean Absolute Error (MAE)
error_value = mean_absolute_error(y_test, predicted_values)

# Display the evaluation result
print("Model Evaluation")
print("----------------")
print(f"Mean Absolute Error (MAE): {error_value:.2f}")

# Compare actual scores with predicted scores
comparison_table = pd.DataFrame({
    "Actual Score": y_test.values,
    "Predicted Score": predicted_values
})

print("\nComparison of Actual vs Predicted Scores")
print(comparison_table)

# Predict the score for a student studying 4.5 hours
study_time = [[4.5]]
estimated_score = regressor.predict(study_time)

print(f"\nEstimated score for studying 4.5 hours: {estimated_score[0]:.2f}")
