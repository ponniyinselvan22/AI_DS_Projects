import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("student_data.csv")

X = data[["StudyHours"]]
y = data["Marks"]

model = LinearRegression()
model.fit(X, y)

predicted = model.predict([[6]])

print("Predicted Marks:", predicted[0])

plt.scatter(data["StudyHours"], data["Marks"])
plt.plot(data["StudyHours"], model.predict(X))
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Performance Prediction")
plt.show()