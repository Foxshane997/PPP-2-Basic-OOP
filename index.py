# Question 1 Getting Started
class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')
    print("Getting started section ----------------------")

myCar = Car('Kitt', 180)
myOtherCar = Car('Speedy', 55)

myCar.talk('Michael')

# Question 2 Race Class -
class Race:
    def __init__(self, name, driver_limit):
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = []

    def add_driver(self, driver):

# Adding drivers to the Race
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)
        else:
            print("Driver limit reached. Cannot add more drivers.")

    def get_average_ranking(self):

# Getting the Average Drivers
        if not self.drivers:
            return None
        total_ranking = sum(driver.ranking for driver in self.drivers)
        return total_ranking / len(self.drivers)

# Question 3 Driver Class -
class Driver:
    number_of_drivers = 0

# Defining the Class for the Racers
    def __init__(self, name, age, ranking):
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1 

# Instantiating the Race
race = Race("Cobalt 400", 4)

# Instantiating the Drivers
driver1 = Driver("Lewis Hamilton", 46, 83)
driver2 = Driver("Eliud Kipchoge", 36, 95)
driver3 = Driver("Sebastian Vettel", 34, 76)
driver4 = Driver("Ayrton Senna", 34, 99)

# Adding each racer to average_ranking
race.add_driver(driver1)
race.add_driver(driver2)
race.add_driver(driver3)
race.add_driver(driver4)

print(f"Driver 1: {driver1.name}, Age: {driver1.age}, Ranking: {driver1.ranking}")
print(f"Driver 2: {driver2.name}, Age: {driver2.age}, Ranking: {driver2.ranking}")
print(f"Total amount of drivers: {Driver.number_of_drivers}")

# Calling the function to ge the average of the drivers
average_ranking = race.get_average_ranking()
print(f"Average Ranking: {average_ranking}")