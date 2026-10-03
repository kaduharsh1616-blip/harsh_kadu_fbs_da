#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students

num_students = int(input("Enter number of students: "))
percentages = []

for i in range(num_students):
    print(f"Enter marks for student {i + 1}:")
    total_marks = 0
    for j in range(5):
        marks = float(input(f"Subject {j + 1}: "))
        total_marks += marks
    percentage = (total_marks / 500) * 100
    percentages.append(percentage)

print("\nIndividual Percentages:")
for i, percentage in enumerate(percentages, start=1):
    print(f"Student {i}: {percentage:.2f}%")

average_percentage = sum(percentages) / len(percentages)
print(f"\nAverage Percentage: {average_percentage:.2f}%")
