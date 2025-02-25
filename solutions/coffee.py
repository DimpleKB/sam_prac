import pandas as pd
import matplotlib.pyplot as plt

### (a) Best Coffee Seeds Supplier Based on Sales & Quality ###


df = pd.read_excel("C://Users//DIMPLE K B//Documents//coffee.xlsx",parse_dates=["date"])
supplier_analysis = df.groupby("supplier_name")[["quantity_purchased","price_per_kg"]].mean()
best_supplier = supplier_analysis.sort_values(by=['quantity_purchased','price_per_kg'],ascending=[False,True]).index[0]
print(f'best coffee seed supplier : {best_supplier}')

### (b) Compare Instant Coffee vs. Filter Coffee Sales ###

coffee_sales = df.groupby("coffee_type")["quantity_sold"].sum()
plt.figure(figsize=(6,4))
coffee_sales.plot(kind="bar",color=['brown','green'])
plt.xlabel("coffee type")
plt.ylabel("total sales")
plt.title("instant coffee vs filter coffee sales")
plt.show()

### (c) Water Quantity Analysis from Customer Feedback ###


water_feedback = df["water feedback"].value_counts()
plt.figure(figsize=(6,4))
water_feedback.plot(kind='pie',autopct="%1.1f%%",colors=['red','yellow','green'],labels=['reduce','increase','same'])
plt.title("customer feedback on water quantity")
plt.show()

### (d) Compare Sales Based on Sweetener Type ###

sweetener_sales = df.groupby('sweetener')['quantity_sold'].sum()
plt.figure(figsize=(6,4))
sweetener_sales.plot(kind="bar",color=['blue','orange','purple'])
plt.xlabel("sweetener type")
plt.ylabel("total sales")
plt.title("sales of coffee with sugar , jaggery , and sugar-free")
plt.show()