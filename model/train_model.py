import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split




heart_data=pd.read_csv('datasets/heart.csv')
data = pd.DataFrame(heart_data)
print(data.head())

X, Y = data.drop('target', axis=1), data['target']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


#save the model to a joblib file
joblib.dump(model, 'model/heart_disease_model.joblib')

print("Model trained and saved successfully.")
