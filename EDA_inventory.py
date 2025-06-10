import seaborn as sns
import pandas as pd

Inventory=pd.read_csv(r"C:\Users\bhagy\OneDrive\Desktop\project\healthcare.csv")

# Measures of Central Tendency / First moment business decision

# Numerical Data-Patient_ID,Quantity,ReturnQuantity,Final_Cost,Final_Sales,RtnMRP

# Catogorical data-Typeofsales, Specialisation,Dept,Formulation,DrugName,SubCat,SubCat1
#1st moment os buisseness
columns=['Quantity','ReturnQuantity','Final_Cost','Final_Sales','RtnMRP']

Means=Inventory[columns].mean()

print(Means)

Median=Inventory[columns].median()

print(Median)

Mode=Inventory[columns].mode()
print(Mode)
#2nd moment

variance=Inventory[columns].var()

print(variance)

STD=Inventory[columns].std()

print(STD)

Range=Inventory[columns].max()-Inventory[columns].min()

print(Range)
#3rd moment

Skewness=Inventory[columns].skew()
print(Skewness)

Kurtosis=Inventory[columns].kurt()
print(Kurtosis)











