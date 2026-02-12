import pandas as pd
from sklearn.tree import DecisionTreeClassifier
x=[[25,600,1],[30,650,1],[40,700,1],[50,720,1],[60,750,1],[35,680,1],[10,500,0],[15,520,0],]
y=[0,0,1,1,1,0,0,0]

model=DecisionTreeClassifier
model.fit(x,y)

x1=[[20,700,1],[20,700,0],[30,700,1],[30,700,0],[40,700,1],[70,700,0],[70,700,1]]
for i in range(len(x1)):
    prediction=model.predict([x1])
    
    if prediction==0:
        print("credit card approved")
    else:
        print("credit card not approved")
        

