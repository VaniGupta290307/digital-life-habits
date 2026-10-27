import csv

with open(r"C:\Users\HP\Downloads\Data_Science\Digital_life_habbit\data\social_media_sleep_stress_productivity_11000.csv", "r") as file:
    reader = csv.reader(file)

    print("Column names:")  
    for row in reader:
        print(row)
        break 
    count = 0

    for row in reader:
        count += 1
    print("Total data records:", count)
