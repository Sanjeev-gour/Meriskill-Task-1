import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np

df = pd.read_csv("HR-Employee-Attrition.csv")
print(df.head(5))

employee_count = df.EmployeeCount.sum()

print(employee_count)

print(df.EducationField.unique())

#grouping the education field on the basis of employee count 
group_edu = df.groupby('EducationField')['EmployeeCount'].sum().sort_values(ascending=False)

print(group_edu)


#printing the barchart of education field and employee count in that education field.
plt.figure(figsize=(10, 6))
bars = plt.bar(group_edu.index, group_edu.values, color='skyblue')
plt.xlabel('Education Field')
plt.ylabel('Employee Count')
plt.title('Employee Count by Education Field')
plt.xticks(rotation=45)  

# Adding annotations (numbers) on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,yval,round(yval), ha='center', va='bottom')

plt.tight_layout()
plt.show()

count=0
for x in df['Attrition']:
    if x=='Yes':
       count = count+1



#Calculating number of yes and no attritions 
print("Number of Yes attritions: ",count)
print("Number of No attritions: ",employee_count-count)


#grouping worklife balance on the basis of attrirtions 

wlb_group = df[df['Attrition'] == 'Yes'].groupby('WorkLifeBalance')['Attrition'].count().sort_index(ascending=False).sort_values(ascending=False)

wlb_group.index = wlb_group.index.map({1: 'Bad',2: 'Average',3: 'Good',4: 'Excellent'})

print(wlb_group)

# Plotting the bar chart
plt.figure(figsize=(8, 6))
plt.bar(wlb_group.index, wlb_group.values, color='blue')
plt.xlabel('Work Life Balance')
plt.ylabel('Attrition Count')
plt.title('Attrition Count by Work Life Balance')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Group by 'Distance_home' and count occurrences of 'Yes' in 'Attrition'


bins = [0,10, 20, 30]
labels = ['1-10', '11-20', '21-30']

# Create a new column with distance groups
df['Distance_home'] = pd.cut(df['DistanceFromHome'], bins=bins, labels=labels, right=False)


dfh_group = df[df['Attrition'] == 'Yes'].groupby('Distance_home')['Attrition'].count().sort_values(ascending=False)

print(dfh_group)

plt.figure(figsize=(8, 6))
plt.bar(dfh_group.index, dfh_group.values, color='red')
plt.xlabel('Distance From Home')
plt.ylabel('Attrition Count')
plt.title('Attrition Count by Distance From Home')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


#grouping by age

binss = [18,30,45,60]
labelss = ['18-30', '31-45', '46-60']

df['Age_of_emp']= pd.cut(df['Age'],bins=binss,labels=labelss,right=False)

age_grouped=df[df['Attrition'] == 'Yes'].groupby('Age_of_emp')['Attrition'].count().sort_values(ascending=False)

print(age_grouped)

plt.bar(age_grouped.index,age_grouped.values)
plt.xlabel('Age')
plt.ylabel('Attrition Count')
plt.title('Attrition Count by Age')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


#Total attrition by martial status usign stacked column chart 
df_attrition = df[df['Attrition']=='Yes']


marital_status_grouped = df_attrition.groupby(['MaritalStatus', 'Gender']).size().unstack().fillna(0)

print(marital_status_grouped)


marital_status_grouped.plot(kind='bar', stacked=True)

plt.xlabel('Marital Status')
plt.ylabel('Attrition Count')
plt.title('Attrition Count by Marital Status and Gender')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


#Total attrition by Job role

job_role_grouped = df_attrition.groupby(['JobRole','Gender']).size().unstack().fillna(0)
print(job_role_grouped)

job_role_grouped.plot(kind='bar',stacked = True)

plt.xlabel('Job Role')
plt.ylabel('Attrition Count')
plt.title('Attrition Count by Job role')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Total attrition by Travell

Travel_grouped = df_attrition.groupby(['BusinessTravel','Gender']).size().unstack().fillna(0)
print(Travel_grouped)

Travel_grouped.plot(kind='bar',stacked = True)

plt.xlabel('Travel')
plt.ylabel('Attrition Count')
plt.title('Attrition Count by Travell')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Total attrition by Department

Department_grouped = df_attrition.groupby(['Department','Gender']).size().unstack().fillna(0)
print(Department_grouped)

Department_grouped.plot(kind='bar',stacked = True)

plt.xlabel('Department')
plt.ylabel('Attrition Count')
plt.title('Attrition Count by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


total_attrition_by_department = df_attrition.groupby('Department').size()
labels = total_attrition_by_department.index
sizes = total_attrition_by_department.values

# Creating the donut chart of Department
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, startangle=90, wedgeprops={'width': 0.3})

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)


ax.axis('equal')  

plt.title('Attrition by Department')
plt.tight_layout()
plt.show()


#Total attrition by years

Years_grouped = df_attrition.groupby(['Department','Gender','YearsWithCurrManager']).size().unstack().fillna(0)
print(Years_grouped)

Years_grouped.plot(kind='bar',stacked = True)

plt.xlabel('Years')
plt.ylabel('Attrition Count')
plt.title('Attrition Count by Years')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

