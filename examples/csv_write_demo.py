import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Marks"])
    writer.writerow([101, "Ravi", 85])
    writer.writerow([102, "Priya", 92])

print("CSV File Created Successfully!")