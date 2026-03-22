### Read the data file
### Try catch vary colors of squirrels
# Create a new file named squirrel_count.csv
# New file should have Fur Color, Count columns

import pandas as pd

fur_color_dict  ={}
count_of_color_type =0

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250915.csv", sep=",", header=0)
fur_colors = data["Primary Fur Color"].unique().tolist()

# dropna=False → “NaN’leri atma, onları da ayrı bir kategori gibi say.”
fur_color_list = data["Primary Fur Color"].value_counts(dropna=False)
print(fur_colors, fur_color_list)

# reset_index() → index’i alıp normal bir kolon haline getirdi.
# Artık tablonun içinde “index” diye bir kolon var.
fur_color_counts_df = fur_color_list.reset_index()
fur_color_counts_df.columns = ["Fur Color", "Count"]

print(fur_color_counts_df)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
fur_color_counts = data["Primary Fur Color"].value_counts().to_dict()
print(fur_color_counts)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
# Her bir rengin sayısını bul
fur_color_counts = data["Primary Fur Color"].value_counts()

# Dict listesine dönüştür
fur_color_dict_list = [
    {"Fur Color": color, "Count": count}
    for color, count in fur_color_counts.items()
]

print(fur_color_dict_list)

# NaN değerlerini "NaN" ile değiştir
fur_color_counts_df = fur_color_counts_df.fillna("NaN")

# Write data into a new csv file
fur_color_counts_df.to_csv("squirrel_count.csv", index=True)

# Write data into a new excel file
fur_color_counts_df.to_excel("fur_color_summary.xlsx", index=False)


print("The new csv file is saved successfully 🎉")







