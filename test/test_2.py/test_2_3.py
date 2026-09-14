#A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
#for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
#length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
#cost of fencing the field.

import math
radius = 20
length = 50
breadth = 40
cost_per_meter = 35
fencing_times = 5

circular_perimeter = math.pi * radius

rectangular_perimeter = 2 * (length + breadth)

total_perimeter = circular_perimeter + rectangular_perimeter

total_wire_length = total_perimeter * fencing_times
total_cost = total_wire_length * cost_per_meter

print("Total cost of fencing the field: Rs.", total_cost)