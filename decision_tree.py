#-------------------------------------------------------------------------
# AUTHOR: Michael Tang
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
X = [0] * 4
for row in range(len(db)):
    for column in range(4):
        if 'Young' or 'Myope' or 'Yes' or 'Normal' in db[row][column]:
            X[row][column] = 1
        elif db[row][column] == 'Presbyopic' or 'Hypermetrope' or 'No' or 'Reduced':
            X[row][column] = 2
        else:
            X[row][column] = 3
#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
for row in range(len(db)):
    if db[row][4] == 'Yes':
        Y.append(1)
    else:
        Y.append(2)
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()