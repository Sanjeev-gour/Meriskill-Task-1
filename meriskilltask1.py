import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 




df = pd.read_csv("Sales_Data.csv")
#print(df.head(5))

df.drop(df.columns[0],axis=1,inplace=True)

#print(df.head(5))


#maximum sales of the 
print(df.Sales.sum()/1000,"K")

#total sales quantity 
print(df.Quantity_Ordered.sum()/1000,"K")
'''
plt.figure(figsize=(12,6))



sns.lineplot(data=df,x='Month',y='Sales')

sns.lineplot(df["Sales"])
plt.xlabel('Month')
plt.ylabel('Sales')

plt.show()

plt.figure(figsize=(100, 3))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
'''
#to find the top 5 best selling products 

print('Top 5 products by sales')

top_selling_products = df.groupby('Product')['Sales'].sum()

top_products = top_selling_products.sort_values(ascending=False).head(5)

other_sales = top_selling_products.sort_values(ascending=False).iloc[5:].sum()

top_products['Others'] = other_sales


print(top_selling_products.head(5))

plt.figure(figsize=(10,6))
top_products.plot(kind='pie', autopct='%1.1f%%',startangle=140,colormap='viridis')
plt.title('Top 5 best selling products of the market')
plt.ylabel(" ")
plt.show()


#top 5 cities by sales 
print('Top 5 cities by sales ')

top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_cities.head(5))

sns.barplot(top_cities)
plt.xticks(rotation=45)
plt.ylabel('Sales')
plt.xlabel('City')
plt.title('Top 5 cities based on sales')
plt.show()


#newyork city data of top 5 products 





# Assuming df is your DataFrame with the provided dataset

# Filter data for New York City
df_ny = df[df['City'] == ' New York City']

# Calculate sales for each product in New York
product_sales_ny = df_ny.groupby('Product')['Sales'].sum()

# Check if there are any data in product_sales_ny
if product_sales_ny.empty:
    print("No data available for New York City")
else:
    # Select top 5 products by sales in New York
    top_products_ny = product_sales_ny.sort_values(ascending=False).head(5)

    # Plotting bar chart for top 5 products in New York
    plt.figure(figsize=(10, 6))
    top_products_ny.plot(kind='bar', color='skyblue')
    plt.title('Top 5 Products in New York City by Sales')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.show()

#to calculate total profit 

print("Count of Total Sales")

print(df.Sales.count)




