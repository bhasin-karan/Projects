# Referenced https://towardsdatascience.com/build-your-own-synthetic-data-15d91389a37b
# and https://github.com/kurtklingensmith/SyntheticData/blob/main/SyntheticDataBook.ipynb for both generate_data scripts
import numpy as np
import pandas as pd

np.random.seed(1)

samples = 2500

# Generating age
age = np.random.randint(18, 90, samples)

# Generating initial samples for bmi from a normal distribution with a mean of 26.5 and sd of 8.6
bmi_normal = np.random.normal(26.5, 8.6, samples)
# Limiting values between BMI of 14.1 and 52.3
bmi = np.clip(bmi_normal, 14.1,52.3)
# Rounding to 2 decimal places
bmi = np.round(bmi, 2)

# Generating physical activity by basing likelihood on bmi
physical_activity = np.empty(samples, dtype=int)
for ind, val in enumerate(bmi):
    if val < 25:
        physical_activity[ind] = np.random.choice([0, 1, 2], p=[0.2, 0.5, 0.3])
    if 25 < val < 30:
        physical_activity[ind] = np.random.choice([0, 1, 2], p=[0.5, 0.3, 0.2])
    if val > 30:
        physical_activity[ind] = np.random.choice([0, 1, 2], p=[0.7, 0.2, 0.1])

sex = np.random.choice([0, 1], samples, p=[0.5, 0.5])
family_history = np.random.choice([0, 1], samples, p=[0.6, 0.4])

# Generating cancer occurrence by calculating a risk score based on above factors and then increasing probability of occurrence for higher risk scores
cancer_status = np.empty(samples, dtype=int)

for ind in range(samples):

    riskscore = 0

    if sex[ind] == 1:
        riskscore += 0.01
    if sex[ind] == 0:
        riskscore += 0

    if age[ind] <= 30:
        riskscore += 0.1
    elif 30 < age[ind] <= 50:
        riskscore += 0.5
    elif 50 < age[ind] <= 70:
        riskscore += 1
    else:
        riskscore += 2

    if bmi[ind] <= 25:
        riskscore += 0.1
    elif 25 < bmi[ind] <= 30:
        riskscore += 0.5
    else:
        riskscore += 1

    if physical_activity[ind] == 0:
        riskscore += 1
    elif physical_activity[ind] == 1:
        riskscore += 0.5
    else:
        riskscore += 0.1

    if family_history[ind] == 0:
        riskscore += 0.1
    else:
        riskscore += 0.5

    if riskscore > 3:
        cancer_status[ind] = np.random.choice([0, 1], p=[0.2, 0.8])
    elif 2 < riskscore <= 3:
        cancer_status[ind] = np.random.choice([0, 1], p=[0.5, 0.5])
    else:
        cancer_status[ind] = np.random.choice([0, 1], p=[0.7, 0.3])

df = pd.DataFrame({
    'Age': age,
    'BMI': bmi,
    'Sex': sex,
    'PhysicalActivity': physical_activity,
    'FamilyHistory': family_history,
    'CancerStatus': cancer_status
})


df.to_csv('generated_cancer_data.csv', index=False)
