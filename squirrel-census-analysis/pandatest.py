import pandas

total_temp = 0
avg_temp = 0
data = pandas.read_csv("weather_data.csv", sep=";", header=0)
print(type(data))
print(data.head())
print(type(data["day"]))
print(data.columns)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)
# print(type(temp_list))
# print(len(temp_list))
# print(data["temp"].mean())
#
# avg_temp = sum(temp_list) / len(temp_list)
# print("maximum temp is:" + str(data["temp"].max()))
#
# for temp in temp_list:
#     total_temp = int(temp) + total_temp
# avg_temp = int(total_temp) / len(temp_list)
# print(int(avg_temp))

print(data[data.temp == data["temp"].max()])


