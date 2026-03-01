import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("placement.csv")

# Convert Yes/No to 1/0
data['Internships(Y/N)'] = data['Internships(Y/N)'].map({'Yes':1,'No':0})
data['Innovative Project(Y/N)'] = data['Innovative Project(Y/N)'].map({'Yes':1,'No':0})
data['Technical Course(Y/N)'] = data['Technical Course(Y/N)'].map({'Yes':1,'No':0})

# Convert Placement to 1/0
data['Placement(Y/N)?'] = data['Placement(Y/N)?'].map({'Placed':1,'Not Placed':0})

# Select Features
X = data[['Cgpa','Internships(Y/N)','Innovative Project(Y/N)',
          'Technical Course(Y/N)','Communication level']]

# Target
y = data['Placement(Y/N)?']

# Train-Test Split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Train Model
model = RandomForestClassifier()
model.fit(X_train,y_train)

# Accuracy Check
accuracy = model.score(X_test,y_test)
print("Model Accuracy:",accuracy)

# Save Model
pickle.dump(model,open("model.pkl","wb"))

print("AI Model Saved Successfully!")