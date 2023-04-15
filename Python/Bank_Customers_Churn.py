print("Bank Customers Churn")
# import data
import pandas as pd
df = pd.read_csv("Churn Modeling.csv")

# preview top 5 rows
df.head()

# see data frame information using .info()
df.info()

#Drop missing value
df = df.dropna()
df.info()

#How many columns, rows in this dataset
df.shape

print("Data Analysis Part")
#01 - What is the proportion and percentage of bank accounts for each geography?
df1 = df['Geography'].value_counts()

df2 = (df['Geography'].value_counts(normalize=True)
                .mul(100)
                .rename_axis('Geography')
                .reset_index(name='percentage'))

#preview data
print(df1 , df2)

# this is bar chart to show geography distribution
df['Geography'].value_counts().plot(kind='bar', color=['salmon', 'orange', 'gold'])

#02 - What is the distribution of bank accounts by age?
result_age = df[ ['Age'] ].value_counts().reset_index()
result_age.columns = ['Age', 'count']
result_age.dropna().sort_values(['Age'])

# this is histogram to show age distribution
df['Age'].plot(kind='hist', bins=30, color="#4B8BBE");

# 03 - What is the distribution of age within the Exited category?
result = df[ ['Exited', 'Age'] ].value_counts().reset_index()
result.columns = ['Exited', 'Age', 'count']
result.dropna().sort_values(['Exited', 'Age'])

#04 - How much total Estimated Salary, average Estimated Salary, and standard deviation of Estimated Salary group by Gender
df.groupby(['Gender'])['EstimatedSalary']\
    .agg(['sum', 'mean', 'std'])\
    .reset_index()

#05 - How many active members are there in the Exited category?
Exited_data = df[ df['Exited'] == 1 ]
Exited_data1 = Exited_data['IsActiveMember'].value_counts()
Exited_data1

#06 - What is the minimum, average, standard deviation, and maximum credit score for each group in the Exited category?
df3 = df.groupby(['Exited'])['CreditScore']\
    .agg(['min', 'mean', 'median', 'std', 'max'])\
    .reset_index()

# transpose data
df3.T

#07 - What are the average and standard deviation values for tenure, balance, number of products, and estimated salary for each group within the Exited category?
df4 = df.groupby(['Exited'])['Tenure','Balance','NumOfProducts','EstimatedSalary']\
    .agg(['mean', 'std'])\
    .reset_index()

# transpose data
df4.T
