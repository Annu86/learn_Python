# Variable strings

cars = 100

used_car = 45

damaged_cars = 12

print('In the car center,there are total', cars,'cars.' 'Out of that', used_car, 'are used and', damaged_cars, 'are damaged.')
print('therefore, there are', cars - (used_car+damaged_cars),'new cars.')

passenger =120
car_seats = 5
car_pool_capacity = car_seats * cars - (used_car+damaged_cars)
average_passenger_per_car = passenger/ (cars - (used_car+damaged_cars))

print('average passenger per car will be', int(average_passenger_per_car))
print('car pool capacity is', car_pool_capacity)
