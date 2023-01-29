class Car:
    def __init__(self, the_model, the_year, the_color, penalties=0):
        self.model = the_model
        self.year = the_year
        self.color = the_color
        self.penalties = penalties


bmw_car = Car("X7", 2020, "blue")
print(Car)
print(f"Car: {bmw_car.model} year: {bmw_car.year} color: {bmw_car.color}")

honda_car = Car ("Fit", 2018, "red")
print(f"Car: {honda_car.model} year: {honda_car.year} color: {honda_car.color}")
