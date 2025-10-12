
# 1
import numpy as np
np.random.seed(42)
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))
C = A @ B
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A x B:\n", C)

# 2
def sum_secondary_diagonal(m):
    n = m.shape[0]
    return sum(m[i, n - 1 - i] for i in range(n))
sec_sum_A = sum_secondary_diagonal(A)
print("Secondary diagonal sum of A:", sec_sum_A)

# 3
import pandas as pd
rolls = 1000
dice1 = np.random.randint(1, 7, rolls)
dice2 = np.random.randint(1, 7, rolls)
sums = dice1 + dice2
distribution = pd.Series(sums).value_counts().sort_index()
dist_df = distribution.rename_axis("Sum").reset_index(name="Count")
print(dist_df)

# 4
students = pd.DataFrame({
    "Name": ["Alice", "Bob", "Carol", "David", "Eva", "Frank"],
    "Age": [20, 22, 19, 21, 23, 20],
    "Grade": [9.2, 4.8, 6.0, 7.5, 3.9, 5.0],
})
students["Result"] = np.where(students["Grade"] >= 5, "Admitted", "Rejected")
students.to_csv("students.csv", index=False)
print(students)

# 5
df = pd.read_excel("vanzari.xlsx")
regions = df["Regiune"].unique()[:2].tolist()
filtered = df[df["Regiune"].isin(regions)].copy()
sorted_desc = filtered.sort_values(by="Pret_Unitar", ascending=False)
print(sorted_desc)
print(sorted_desc.head(5))
print(sorted_desc.tail(5))

# 6
df["TotalSale"] = df["Pret_Unitar"] * df["Cantitate"]
mean_total_by_seller = df.groupby("Vanzator", as_index=False)["TotalSale"].mean().rename(columns={"TotalSale": "MeanTotalSale"})
print(mean_total_by_seller)

# 7
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 400)
y1 = x ** 2
plt.figure()
plt.plot(x, y1)
plt.title("y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

y2 = np.sin(x) + np.cos(x)
plt.figure()
plt.plot(x, y2)
plt.title("y = sin(x) + cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 8
plt.figure()
plt.bar(dist_df["Sum"], dist_df["Count"])
plt.title("Distribution of Sums (Two Dice, 1000 rolls)")
plt.xlabel("Sum")
plt.ylabel("Count")
plt.show()

plt.figure()
plt.boxplot(sums, vert=True)
plt.title("Box Plot of Dice Sums")
plt.ylabel("Sum")
plt.show()

# 9
total_sales_by_seller = df.groupby("Vanzator", as_index=False)["TotalSale"].sum().rename(columns={"TotalSale": "TotalSales"})
plt.figure()
plt.bar(total_sales_by_seller["Vanzator"], total_sales_by_seller["TotalSales"])
plt.title("Total Sales by Seller")
plt.xlabel("Seller")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

accessories_by_region = df[df["Categorie"] == "Accesorii"].groupby("Regiune", as_index=False)["Cantitate"].sum().rename(columns={"Cantitate": "TotalAccessories"})
plt.figure()
plt.bar(accessories_by_region["Regiune"], accessories_by_region["TotalAccessories"])
plt.title("Total Accessories Units by Region")
plt.xlabel("Region")
plt.ylabel("Total Accessories Units")
plt.tight_layout()
plt.show()
