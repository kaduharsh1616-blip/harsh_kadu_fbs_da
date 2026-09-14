# Write a program to calculate the total cost of painting. The interior of building with 3 rooms, 2 halls and 1 kitchen. The cost of painting per square foot is Rs. 18.50. The area of each room is 250 square feet, the area of each hall is 400 square feet and the area of the kitchen is 150 square feet.
room_area = 250
hall_area = 400
kitchen_area = 150
cost_per_square_foot = 18.50

total_cost = (3 * room_area + 2 * hall_area + kitchen_area) * cost_per_square_foot
print("Total cost of painting the interior of the building: Rs.", total_cost)
