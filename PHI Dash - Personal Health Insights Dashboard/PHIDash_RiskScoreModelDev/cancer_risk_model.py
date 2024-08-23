# Referenced https://medium.com/@draj0718/logistic-regression-with-standardscaler-from-the-scratch-ec01def674e8
# and https://neptune.ai/blog/saving-trained-model-in-python for both risk_model scripts
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load generated data
df = pd.read_csv('generated_cancer_data.csv')

# Split data into features and target
X = df[['Age', 'BMI', 'Sex', 'PhysicalActivity', 'FamilyHistory']]
y = df['CancerStatus']

# Split features and target data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=111)

# Feature scaling
cancer_scaler = StandardScaler()
X_train_scaled = cancer_scaler.fit_transform(X_train)
X_test_scaled = cancer_scaler.transform(X_test)

# Develop model
cancer_model = LogisticRegression()
cancer_model.fit(X_train_scaled, y_train)
y_pred = cancer_model.predict(X_test_scaled)

# Save trained model and scaler
joblib.dump(cancer_model, 'cancer_model.joblib')
joblib.dump(cancer_scaler, 'cancer_scaler.joblib')

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)

