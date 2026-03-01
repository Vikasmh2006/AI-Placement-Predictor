import pandas as pd

data = pd.read_csv("placement.csv")

# Convert Yes/No to 1/0
data['Internships(Y/N)'] = data['Internships(Y/N)'].map({'Yes':1,'No':0})
data['Innovative Project(Y/N)'] = data['Innovative Project(Y/N)'].map({'Yes':1,'No':0})
data['Technical Course(Y/N)'] = data['Technical Course(Y/N)'].map({'Yes':1,'No':0})

# Convert Placement to 1/0
data['Placement(Y/N)?'] = data['Placement(Y/N)?'].map({'Placed':1,'Not Placed':0})

# Select Important Features
X = data[['Cgpa','Internships(Y/N)','Innovative Project(Y/N)',
          'Technical Course(Y/N)','Communication level']]

# Target Output
y = data['Placement(Y/N)?']

print("INPUT FEATURES:\n")
print(X.head())

print("\nTARGET OUTPUT:\n")
print(y.head())