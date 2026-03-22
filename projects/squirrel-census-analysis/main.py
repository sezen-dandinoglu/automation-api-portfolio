
import csv

class Main:
    def __init__(self):
        self.data = []
        self.temperatures = []
        self.temp1 = ''
        # print(str(self.data))
        # with open("weather_data.csv","r",encoding="utf-8") as data_file:
        #     self.data.append(data_file.readlines())
        #     print(self.data)
        #     for items in self.data:
        #         print(items)

        with open("weather_data.csv") as data_file:
            data = csv.reader(data_file)
            for row in data:
                row_string = "".join(row)
                print(f"row_string: {row_string}")
                self.temp1 = ''
                for temp in row_string:
                    if temp.isnumeric():
                        self.temp1 += temp
                    else: pass
                if self.temp1 == '': pass
                else: self.temperatures.append(int(self.temp1))
            print(f"Week temperatures: {self.temperatures}")

















if __name__ == "__main__":
    main = Main()