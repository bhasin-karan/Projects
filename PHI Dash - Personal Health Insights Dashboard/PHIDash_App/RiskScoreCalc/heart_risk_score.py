import sys
import joblib

# Load model and scaler
model = joblib.load('RiskScoreCalc/heart_model.joblib')
scaler = joblib.load('RiskScoreCalc/heart_scaler.joblib')

# Convert user features to float
user_features = []
for feature in sys.argv[1:]:
    user_features.append(float(feature))

# Scale user features
user_features_scaled = scaler.transform([user_features])

# Get prediction
prediction = model.predict_proba(user_features_scaled)

if prediction[0][1] <= 0.47:
    print('Low')
if 0.47 < prediction[0][1] <= 0.53:
    print('Medium')
if prediction[0][1] > 0.53:
    print('High')
