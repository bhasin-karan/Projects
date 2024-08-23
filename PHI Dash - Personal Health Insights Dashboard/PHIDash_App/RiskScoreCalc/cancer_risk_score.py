# Referenced https://neptune.ai/blog/saving-trained-model-in-python for both risk_score scripts
import sys
import joblib

# Load model and scaler
model = joblib.load('RiskScoreCalc/cancer_model.joblib')
scaler = joblib.load('RiskScoreCalc/cancer_scaler.joblib')

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
