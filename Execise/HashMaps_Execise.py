# nyc_weather.csv contains new york city weather for first few days in the month of January.
# Write a program that can answer following,
#      What was the average temperature in first week of Jan
#      What was the maximum temperature in first 10 days of Jan
#
# 2.  nyc_weather.csv contains new york city weather for first few days in the month of January.
# Write a program that can answer following,
#     What was the temperature on Jan 4?

# Figure out data structure that is best for this problem
class Exercise:
    def __init__(self):
        self.temperature = 0
        self.weather_array = []

    def calc_average_temp(self):
        with open("nyc_weather.csv", "r") as f:
            for line in f:
                tokens = line.split(',')
                try:
                    temperature = int(tokens[1])
                    self.weather_array.append(temperature)
                except:
                    print("Invalid temperature.Ignore the row")


if __name__ == '__main__':
    eg = Exercise()
    eg.calc_average_temp()
