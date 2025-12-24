import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/WIN10/Downloads/WA_Fn-UseC_-Telco-Customer-Churn.csv")

df.head()
df.columns
df.describe()
df.duplicated().sum()
df.info()
df.shape


# Converted 0 and 1 values to yes/no for better understanding
     
def conv(value):
    if value ==1:
        return "yes"
    else:
        return "no"
    
df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv)
df.head(10)    

## Head
![Head](df.head(10).png)



df["Churn"].value_counts()

#Univariate Analysis 
#Monthly Charges"""
plt.hist(df['MonthlyCharges'])
plt.title("Monthly Charges Distribution")
plt.xlabel("Monthly Charges")
plt.ylabel("Customers")
plt.show()



#Tenure
plt.hist(df['tenure'])
plt.title("Customer Tenure Distribution")
plt.xlabel("tenure (Months)")
plt.ylabel("Customers")
plt.show()


#ivariate Analysis (Churn vs Features)
#Churn vs Monthly Charges
df.groupby("Churn")["MonthlyCharges"].mean().plot(kind="bar")
plt.title("Churn vs Average Monthly Charges")
plt.ylabel("Avg Monthly Charges")
plt.show()



#Churn vs Tenure
df.groupby("Churn")["tenure"].mean().plot(kind="bar")
plt.title("Churn vs Average Tenure")
plt.ylabel("Avg Tenure")
plt.show()


#Categorical Analysis
#Contract Type
df['Contract'].value_counts().plot(kind='bar')
plt.title("Contract Type Distribution")
plt.show()


#Internet Service
df['InternetService'].value_counts().plot(kind='bar')
plt.title("Internet Service Distribution")
plt.show()


#Churn Distribution
ax = sns.countplot(x ="Churn", data = df)
ax.bar_label(ax.containers [0])
plt.title("Churn Distribution by Count")
plt.show()

df["Churn"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Customer Churn Distribution")
plt.show()



### From the above pie chart we can see that 26.54% of the customers churned out
### Now lets understand the reason behind it.

ay = sns.countplot(x = "gender", data = df, hue = "Churn")
ay.bar_label(ay.containers [0])

plt.title("Gender Distribution by Churn")
plt.show()
## The above graph shows that the Churn is not affect by the gender.

#Gender Distribution by Senior Citizen
sns.countplot(x = "SeniorCitizen", data = df, hue = "Churn")
plt.title("Gender Distribution by Senior Citizen")
plt.show()

ct = pd.crosstab(df["SeniorCitizen"], df["Churn"], normalize='index') * 100

# 2. Plot the stacked bar chart
ax = ct.plot(kind='bar', stacked=True)

# 3. Add title and labels
plt.title("Senior Citizen vs Churn (%)")
plt.xlabel("Senior Citizen")
plt.ylabel("Percentage")

# 4. Add percentage labels on the bars
for idx, row in ct.iterrows():
    cumulative = 0
    for churn_value in ct.columns:
        value = row[churn_value]
        if value > 0:
            # Use the numerical location of the index for x-position
            x_pos = ct.index.get_loc(idx)
            plt.text(
                x_pos,                       # x-position
                cumulative + (value / 2),  # y-position
                f'{value:.1f}%',           # label text
                ha='center', va='center'
            )
        cumulative += value

plt.legend(title="Churn")
plt.show()
   

#Tenure Distribution by Churn
plt.figure(figsize = (10, 5))
sns.histplot(x = "tenure", data = df, bins = 72, hue = "Churn")
plt.title("Tenure Distribution by Churn")
plt.show()    

#Count Of Customers by Contract
ax = sns.countplot(x = "Contract", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
plt.title("Count Of Customers by Contract")
plt.show()

#Count Of Customers by PaymentMethod
plt.figure(figsize = (10, 5))
ax = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
plt.title("Count Of Customers by PaymentMethod")
plt.show()
     



#Countplot of {col} by Churn
cols = [
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies'
]

plt.figure(figsize=(15, 15))

for i, col in enumerate(cols, 1):
    plt.subplot(3, 3, i)   # 3 rows, 3 columns
    sns.countplot(data=df, x=col, hue="Churn")
    plt.title(f"Countplot of {col} by Churn")
    plt.xticks(rotation=45)
    plt.xlabel('')
    plt.ylabel('Count')

plt.tight_layout()
plt.show()



#Correlation Analysis (Heatmap using matplotlib)
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols]

corr = df[num_cols].corr()

plt.imshow(corr)
plt.colorbar()
plt.title("Correlation Heatmap")
plt.xticks(range(len(num_cols)), num_cols, rotation=90)
plt.yticks(range(len(num_cols)), num_cols)
plt.show()
















