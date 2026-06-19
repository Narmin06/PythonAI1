import pandas as pd

df = pd.read_csv("Preview__houses_day1__first_20_rows_.csv")
#print(df)

# Task1
#print(df.head(5))
#print(df.tail(5))
#print(df.sample(3))

# Task2
#print(df.info())
#print(df.isnull().sum())
#print(df.dtypes)

# Task 3
#print(df.describe())

#print("Area_m2  → Mean:", df["Area_m2"].mean(),  " Median:", df["Area_m2"].median(),  " Std:", df["Area_m2"].std())
#print("Price_AZN → Mean:", df["Price_AZN"].mean(), " Median:", df["Price_AZN"].median(), " Std:", df["Price_AZN"].std())

# Task 4
#print(df["Price_AZN"].dtype)
#print(df["Price_AZN"])

df["Price_AZN"] = pd.to_numeric(df["Price_AZN"], errors="coerce")
#print(df["Price_AZN"])
# Evvel ve sonra eynidir.

# Task 5
#print(df.sort_values(by="Price_AZN",ascending=False))
# Birinci 1500000 outlier-dir

# Task 6
#print(df["District"].value_counts())
# Çox təmsil olunan: Nasimi        Az təmsil olunan: Khatai

# Task 7
#print(df["Rooms"].value_counts().sort_index())

# Task 8
#print("Mean:  ", df["Price_AZN"].mean())
#print("Median:", df["Price_AZN"].median())

# Task 9
#print("Rooms mode:        ", df["Rooms"].mode()[0])
#print("Price_AZN variance:", df["Price_AZN"].var())
#print("Price_AZN std:     ", df["Price_AZN"].std())

# Task 10
filtered = df[(df["Rooms"] >= 3) & (df["Area_m2"] >= 100)]
#print(filtered)
#print(filtered["Price_AZN"].mean())

# Task 11
#print(df.groupby("District")["Price_AZN"].agg(["mean", "median", "count"]))
#Sabayil — Cunki burda outlier var

#Task 12
#print(df["Price_AZN"].describe())

# Task 13
from scipy import stats

df["zscore"] = stats.zscore(df["Price_AZN"])
#print(df[abs(df["zscore"]) > 3][["District", "Price_AZN", "zscore"]])


# Task 14
df["IsOutlier"] = abs(stats.zscore(df["Price_AZN"])) > 3

expensive = df.sort_values("Price_AZN", ascending=False).head(10)[["District", "Area_m2", "Rooms", "Price_AZN", "IsOutlier"]]
cheap = df.sort_values("Price_AZN", ascending=True).head(10)[["District", "Area_m2", "Rooms", "Price_AZN", "IsOutlier"]]

#print(expensive)
#print()
#print(cheap)

# Task 15
#print(df.groupby("Rooms")["Price_AZN"].median())


# Task 16
df["ppm"] = df["Price_AZN"] / df["Area_m2"].replace(0, pd.NA)

top10 = df.nlargest(10, "ppm")
print(top10[["District", "Area_m2", "Price_AZN", "ppm"]])

# Task 17
region = {
    "Sabayil": "Prime",
    "Yasamal": "Central",
    "Nizami": "Central",
    "Nasimi": "Central",
    "Nerimanov": "Central",
    "Khatai": "Outer",
    "Binagadi": "Outer"
}

df["region"] = df["District"].map(region)
#print(df.groupby("region")["Price_AZN"].median())


# Task 18
nan_rows = df[df["Price_AZN"].isna()]
#print(nan_rows[["District", "Rooms", "Area_m2", "Price_AZN"]])


# Task 19
Q1 = df["Price_AZN"].quantile(0.25)
Q3 = df["Price_AZN"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[(df["Price_AZN"] >= lower) & (df["Price_AZN"] <= upper)]

#print("Təmiz median:", df_clean["Price_AZN"].median())
#print("Orijinal median:    ", df["Price_AZN"].median())



# Task 20
#print(df.shape)
#print(df.isnull().sum())
#print(df.describe())
#print(df["District"].value_counts())
#print("Mean:", df["Price_AZN"].mean(), "Median:", df["Price_AZN"].median())

df["ppm"] = df["Price_AZN"] / df["Area_m2"]
top5 = df.nlargest(5, "ppm")
#print(top5[["District", "Area_m2", "Price_AZN", "ppm"]])























