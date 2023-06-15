from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score

# Example confusion matrix
y_true = [1, 0, 1, 1, 0, 1]
y_pred = [0, 0, 1, 1, 0, 1]
confusion = confusion_matrix(y_true, y_pred)

# Calculate metrics
accuracy = accuracy_score(y_true, y_pred)
sensitivity = recall_score(y_true, y_pred)
specificity = confusion[0, 0] / (confusion[0, 0] + confusion[0, 1])
precision = precision_score(y_true, y_pred)
f_score = f1_score(y_true, y_pred)

# Print results
print(f'Confusion Matrix: \n{confusion}')
print(f'Accuracy: {accuracy:.2f}')
print(f'Sensitivity (Recall): {sensitivity:.2f}')
print(f'Specificity: {specificity:.2f}')
print(f'Precision: {precision:.2f}')
print(f'F-score: {f_score:.2f}')