cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90 
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print(cars)
print(drivers)
print(cars_not_driven)
print(carpool_capacity)
print(passengers)
print(average_passengers_per_car)
