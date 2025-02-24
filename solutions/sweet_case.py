import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
df=pd.read_excel("C://Users//DIMPLE K B//Documents//sweet.xlsx",parse_dates=["date"])
df["Year"] = df["date"].dt.year
df["Month"] = df["date"].dt.strftime("%Y-%m")

#Which sweet sells more in a specific month

specific_month = "2025-03"
monthly_sales = df[df["Month"] == specific_month].groupby("sweet_id")["quantity_sold"].sum()
best_selling_sweet = monthly_sales.idxmax()
print(f"sweet {best_selling_sweet} sold the most in {specific_month} with {monthly_sales.max()} units.")

#when the company revenues are highest during the year

df["revenue"] = df["quantity_sold"] * df["price_per_unit"]
monthly_revenue = df.groupby("Month")["revenue"].sum()
highest_revenue_month = monthly_revenue.idxmax()
print(f"highest revenue month : {highest_revenue_month} ,r revenue : {monthly_revenue.max()}")

#Yearly sales data comparision

yearly_sales=df.groupby("Year")["revenue"].sum()
plt.figure(figsize=(8,5))
yearly_sales.plot(kind="bar",color="blue",alpha=0.7)
plt.xlabel("Year")
plt.ylabel("total revenue")
plt.title("yearly sales comparison")
plt.show()

#which sweet was wasted the most (sold less) reading data in excel sheet 

least_selling_sweet = df.groupby("sweet_id")["quantity_sold"].sum().idxmin()
print(f"sweet {least_selling_sweet} was wasted the most (sold the least).")

plt.figure(figsize=(10,6))
monthly_revenue.plot(kind="line",marker='o',color="green")
plt.xlabel("Month")
plt.ylabel("total revenue")
plt.title("monthly revenue trend")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()