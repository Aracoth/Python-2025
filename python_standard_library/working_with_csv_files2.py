import csv

# I changed the write to a reader
with open("data.csv") as file:
    # reader initially at the start of file
    reader = csv.reader(file)
    # list moves reader to end of file
    # print(list(reader))
    for row in reader:
        print(row)
