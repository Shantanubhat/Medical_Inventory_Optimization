import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

Inventory=pd.read_csv(r"C:\Users\bhagy\OneDrive\Desktop\project\healthcare.csv")

Inventory.dtypes
#typecasting

Inventory.Dateofbill=Inventory.Dateofbill.astype('datetime64[ns]')
Inventory.dtypes
#duplicated
help(Inventory.duplicated)
duplicate = Inventory.duplicated()
duplicate
sum(duplicate)
duplicate = Inventory.duplicated(keep = 'last')
duplicate

#column
Inventory.corr('Quantity')

###############################################
############## Outlier Treatment ###############

# Let's find outliers in Salaries
sns.boxplot(Inventory.Quantity)
# Detection of outliers (find limits based on IQR)
IQR = Inventory['Quantity'].quantile(0.75) - Inventory['Quantity'].quantile(0.25)

lower_limit = Inventory['Quantity'].quantile(0.25) - (IQR * 1.5)
upper_limit = Inventory['Quantity'].quantile(0.75) + (IQR * 1.5)
############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
Inventory['Quantity_rep'] = pd.DataFrame(np.where(Inventory['Quantity'] > upper_limit, upper_limit, np.where(Inventory['Quantity'] < lower_limit, lower_limit, Inventory['Quantity'])))
sns.boxplot(Inventory.Inven_replaced)
Inventory


############### 3. Winsorization ###############
# pip install feature_engine   # install the package

    
# Define the model with IQR method
winsor_iqr = Winsorizer(capping_method = 'iqr', 
                        # choose  IQR rule boundaries or gaussian for mean and std
                          tail = 'both', # cap left, right or both tails 
                          fold = 1.5, 
                          variables = ['Quantity'])

Inventory_out = winsor_iqr.fit_transform(Inventory[['Quantity']])

# Inspect the minimum caps and maximum caps
# winsor.left_tail_caps_, winsor.right_tail_caps_

# Let's see boxplot


sns.boxplot(Inventory.ReturnQuantity)
# Detection of outliers (find limits based on IQR)
IQR = Inventory['ReturnQuantity'].quantile(0.75) - Inventory['ReturnQuantity'].quantile(0.25)

lower_limit = Inventory['ReturnQuantity'].quantile(0.25) - (IQR * 1.5)
upper_limit = Inventory['ReturnQuantity'].quantile(0.75) + (IQR * 1.5)
lower_limit
upper_limit
############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
Inventory['ReturnQuantity_rep'] = pd.DataFrame(np.where(Inventory['ReturnQuantity'] > upper_limit, upper_limit, np.where(Inventory['ReturnQuantity'] < lower_limit, lower_limit, Inventory['ReturnQuantity'])))
sns.boxplot(Inventory.ReturnQuantity_rep)
Inventory

#final_cost

sns.boxplot(Inventory.Final_Cost)
# Detection of outliers (find limits based on IQR)
IQR = Inventory['Final_Cost'].quantile(0.75) - Inventory['Final_Cost'].quantile(0.25)

lower_limit = Inventory['Final_Cost'].quantile(0.25) - (IQR * 1.5)
upper_limit = Inventory['Final_Cost'].quantile(0.75) + (IQR * 1.5)
############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
Inventory['Final_Cost_rep'] = pd.DataFrame(np.where(Inventory['Final_Cost'] > upper_limit, upper_limit, np.where(Inventory['Final_Cost'] < lower_limit, lower_limit, Inventory['Final_Cost'])))
sns.boxplot(Inventory.Final_Cost_rep)
Inventory

#Final_sales
sns.boxplot(Inventory.Final_Sales)
# Detection of outliers (find limits based on IQR)
IQR = Inventory['Final_Sales'].quantile(0.75) - Inventory['Final_Sales'].quantile(0.25)

lower_limit = Inventory['Final_Sales'].quantile(0.25) - (IQR * 1.5)
upper_limit = Inventory['Final_Sales'].quantile(0.75) + (IQR * 1.5)
############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
Inventory['Final_Sales_rep'] = pd.DataFrame(np.where(Inventory['Final_Sales'] > upper_limit, upper_limit, np.where(Inventory['Final_Sales'] < lower_limit, lower_limit, Inventory['Final_Sales'])))
sns.boxplot(Inventory.Final_Sales_rep)
Inventory

#RtnMRP

sns.boxplot(Inventory.RtnMRP)
# Detection of outliers (find limits based on IQR)
IQR = Inventory['RtnMRP'].quantile(0.75) - Inventory['RtnMRP'].quantile(0.25)

lower_limit = Inventory['RtnMRP'].quantile(0.25) - (IQR * 1.5)
upper_limit = Inventory['RtnMRP'].quantile(0.75) + (IQR * 1.5)
############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
Inventory['RtnMRP_rep'] = pd.DataFrame(np.where(Inventory['RtnMRP'] > upper_limit, upper_limit, np.where(Inventory['RtnMRP'] < lower_limit, lower_limit, Inventory['RtnMRP'])))
sns.boxplot(Inventory.RtnMRP_rep)
Inventory
##############################################
#### zero variance and near zero variance ####
columns=['Quantity','ReturnQuantity','Final_Cost','Final_Sales','RtnMRP']
Inventory[columns].var() == 0
#################### Missing Values - Imputation ###########################
Inventory.isna().sum()
mode_imputer = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
Inventory["Formulation"] = pd.DataFrame(mode_imputer.fit_transform(Inventory[["Formulation"]]))
Inventory["DrugName"] = pd.DataFrame(mode_imputer.fit_transform(Inventory[["DrugName"]]))
Inventory["SubCat"] = pd.DataFrame(mode_imputer.fit_transform(Inventory[["SubCat"]]))
Inventory["SubCat1"] = pd.DataFrame(mode_imputer.fit_transform(Inventory[["SubCat1"]]))
Inventory.isna().sum()
Inventory
#normalizxation

a = Inventory.describe()
a
'''Robust Scaling
Scale features using statistics that are robust to outliers'''

from sklearn.preprocessing import RobustScaler

robust_model = RobustScaler()

inv_robust = robust_model.fit_transform(Inventory[columns])

dataset_robust = pd.DataFrame(inv_robust,columns=['qty','rtnqty','final_cost','final_sales','rtnmrp'])
inv_robust = dataset_robust.describe()

Scaling_Inv = pd.concat([Inventory,dataset_robust],axis=1)

#extract
Inventory.to_excel('output.xlsx', index=False)
Scaling_Inv.to_excel(r'C:\Users\bhagy\OneDrive\Desktop\project\project1.xlsx', index=False)
Inventory.to_excel(r'C:\Users\bhagy\OneDrive\Desktop\project\project1.xlsx', index=False)
Inventory.to_csv(r'C:\Users\bhagy\OneDrive\Desktop\project\project1.csv', index=False)
Scaling_Inv.to_csv(r'C:\Users\bhagy\OneDrive\Desktop\project\project1.csv', index=False)
import os
print(os.getcwd())
