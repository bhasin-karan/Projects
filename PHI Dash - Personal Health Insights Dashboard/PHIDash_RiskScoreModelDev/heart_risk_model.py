import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load generated data
df = pd.read_csv('generated_heart_data.csv')

# Split data into features and target
X = df[['Age', 'BMI', 'Sex', 'PhysicalActivity', 'FamilyHistory']]
y = df['HeartStatus']

# Split features and target data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=444)

# Feature scaling
heart_scaler = StandardScaler()
X_train = heart_scaler.fit_transform(X_train)
X_test = heart_scaler.transform(X_test)

# Develop model
heart_model = LogisticRegression()
heart_model.fit(X_train, y_train)
y_pred = heart_model.predict(X_test)

# Save trained model and scaler
joblib.dump(heart_model, 'heart_model.joblib')
joblib.dump(heart_scaler, 'heart_scaler.joblib')

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
