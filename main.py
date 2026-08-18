import pandas as pd,numpy as np,matplotlib.pyplot as plt,seaborn as sns
from sqlalchemy import create_engine


df=pd.read_csv('Blinkit Grocery Data.csv')

# print(df.head())
# print(df.info())
# print(df["Item Weight"].isnull().sum())
# print(df.duplicated().sum())


''' data cleaning '''

df.columns = df.columns.str.lower().str.replace(' ', '_')  
# print(df.columns)

df["item_fat_content"] = df["item_fat_content"].replace({
    "LF": "Low Fat",
    "low fat": "Low Fat",
    "reg": "Regular"
})
# print(df["item_fat_content"].value_counts())

# print(df.dtypes)


''' feature engineering '''
df["outlet_age"] = 2026 - df["outlet_establishment_year"]

df["visibility_category"] = pd.cut(
    df["item_visibility"],
    bins=[-1, 0.05, 0.10, 1],
    labels=["Low", "Medium", "High"]
)

''' load data into database '''

# df.to_csv(r"C:\Users\mahes\OneDrive\Desktop\PROJECT\Sales Domain\E-commerce Sales Analysis\cleaned_data.csv",index=False)
# engine = create_engine("mysql+pymysql://root:admin@localhost:3306/ecommerce")

# df.to_sql("sales_data", con=engine, if_exists='replace', index=False)



'''analyse the data (EDA)/ answers to business questions'''

# question 1: Which item types generate the highest total sales?
# item_sales = (
#     df.groupby("item_type")["total_sales"]
#       .sum()
#       .reset_index()
#       .sort_values("total_sales", ascending=False)
# )

# plt.figure(figsize=(10,6))
# sns.barplot(
#     data=item_sales.head(10),
#     y="item_type",
#     x="total_sales"
# )

# plt.title("Total Sales by Item Type")
# plt.show()

# Question 2: Which item types have the highest average sales?
    # using sql
    # print("household in this category deliver stronger sales performance on average and may deserve greater promotional focus")

# Question 3: Which Outlet Type generates the highest total sales?
    # using sql
    # print("Supermarket Type1 generates the highest total sales, making it the strongest revenue-contributing outlet format. This indicates that this outlet type plays the most significant role in Blinkit's overall sales performance.")

# Question 4: Does Outlet Size affect sales performance?
# outlet_size_analysis = (
#     df.groupby("outlet_size")
#       .agg(
#           number_of_outlets=("outlet_identifier", "nunique"),
#           total_sales=("total_sales", "sum")
#       )
#       .reset_index()
# )

# outlet_size_analysis["sales_per_outlet"] = (
#     outlet_size_analysis["total_sales"] /
#     outlet_size_analysis["number_of_outlets"]
# ).round(2)


# plt.figure(figsize=(6,4))

# sns.barplot(
#     data=outlet_size_analysis,
#     x="outlet_size",
#     y="sales_per_outlet"
# )

# plt.title("Sales per Outlet by Outlet Size")
# plt.xlabel("Outlet Size")
# plt.ylabel("Sales per Outlet")

# plt.show()

# print("Medium-sized outlets generate the highest sales per outlet, indicating the strongest outlet productivity. This suggests that medium-sized outlets are the most effective outlet format for maximizing sales performance.")


# Question 5: Which Outlet Location Type performs the best?
    # solve in sql query
    # print("Tier 2 has the highest sales per outlet, indicating the strongest outlet productivity. Although another tier may generate higher total sales, Tier 2 performs better on an individual outlet basis.")

# Question 6: Does Item Visibility have a relationship with Total Sales?


# print(df.groupby("visibility_category")["total_sales"].agg(
#     total_products="count",
#     total_sales="sum",
#     average_sales="mean"
# )
# )

# sns.barplot(
#     data=df,
#     x="visibility_category",
#     y="total_sales",
#     estimator="mean"
# )

# plt.title("Average Sales by Visibility Category")
# plt.xlabel("Visibility Category")
# plt.ylabel("Average Sales")
# plt.show()

# print("Medium visibility products have the highest average sales. However, the difference between Low, Medium, and High visibility is relatively small, indicating that Item Visibility has only a weak relationship with Total Sales.")



# Question 7: Does Outlet Age influence sales performance?

# plt.figure(figsize=(8,4))

# sns.lineplot(
#     data=df.groupby("outlet_age").agg(
#         # number_of_outlets=("outlet_identifier", "nunique"),
#         # total_sales=("total_sales", "sum"),
#         average_sales=("total_sales", "mean")
#     ).reset_index(),
#     x="outlet_age",
#     y="average_sales",
#     marker="o"
# )

# plt.title("Average Sales by Outlet Age")
# plt.xlabel("Outlet Age (Years)")
# plt.ylabel("Average Sales")

# plt.show()

# print("Outlet age is not a significant predictor of sales performance, so Blinkit should prioritize operational factors rather than simply expanding older outlets.")


# Question 8: Which Outlet Types have the highest average customer ratings?
    # sql query use

    # print("Grocery Store outlets receive the highest average customer ratings, indicating stronger customer satisfaction compared to other outlet types. This suggests that their service quality or shopping experience may be contributing positively to customer perception.")


# Question 9: Which products/categories should Blinkit prioritize based on sales performance?

# plt.figure(figsize=(10,6))

# category_analysis = (
#     df.groupby("item_type")
#       .agg(
#           total_products=("item_identifier","count"),
#           total_sales=("total_sales","sum"),
#           average_sales=("total_sales","mean")
#       )
#       .reset_index()
# )

# category_analysis["sales_contribution"] = (
#     category_analysis["total_sales"] /
#     category_analysis["total_sales"].sum() * 100
# ).round(2)
# category_analysis = category_analysis.sort_values(
#     "total_sales",
#     ascending=False
# )

# sns.barplot(
#     data=category_analysis.head(10),
#     y="item_type",
#     x="total_sales"
# )

# plt.title("Top 10 Product Categories by Total Sales")
# plt.xlabel("Total Sales")
# plt.ylabel("Item Type")

# plt.show()


# Question 10: Which outlet format should Blinkit expand to maximize revenue?
    # using sql
        # insight 
        # small-sized Supermarket Type1 outlets in Tier 1 locations,high-sized Supermarket Type1 outlets in Tier 3 locations and Medium-sized Supermarket Type2 outlets in Tier 3 locations achieve the highest sales per outlet. Blinkit should prioritize expanding this outlet format because it combines strong revenue generation with high outlet productivity.