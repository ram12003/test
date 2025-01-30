# import os
# os.remove("input.txt")

#1Write a Python program to read the contents
# of a text file named input.txt and display them on the screen.
# with open('input.txt', 'w') as file:
#     file.write("Hi\n")
#     file.write("Hello")
# print("'input.txt' file was created and content written")
#
# try:
#     with open('input.txt', 'r') as file:
#         content = file.read()
#         print(content)
# except filenotfounderror:
#     print("'input.txt' file doesn't exist")

#2Write a Python program to take user input
# and write it to a new text file named output.txt.
# user_input = input("enter some text:")
# with open('output.txt', 'w') as file:
#     file.write(user_input)
# print("input written to output.txt")


# with open('output.txt', 'r') as file:
#       content = file.read()
#       print(content)

#3 Write a Python program to copy the contents of one text
# file named source.txt to another text file named destination.txt
# with open('source.txt', 'w') as file:
#     file.write("file handling")
#
# with open('source.txt', 'r') as source_file:
#     content = source_file.read()
#
# with open('destination.txt', 'w') as destination_file:
#     destination_file.write(content)
#
#
# print("data is copied")
# print(content)

#2method
# import shutil
# shutil.copy('source.txt', 'destination.txt')


#4Write a Python program to read data from a
# CSV file named data.csv and display it in tabular format.

# import csv
# with open('data.csv', 'w', newline='') as file:
#     csv_write = csv.writer(file)
#     csv_write.writerow(["Name", "Age", "City"])
#     csv_write.writerow(["John", 28, "New York"])
#     csv_write.writerow(["Alice", 34, "Los Angeles"])
#     csv_write.writerow(["Bob", 22, "Chicago"])
# print("CSV file 'data.csv' created")
#
# import csv
# with open('data.csv', 'r') as file:
#     csv_read = csv.reader(file)
#     header = next(csv_read)
#     print(f"{header[0]:<10} {header[1]:<10} {header[2]:<10}")
#
#     for row in csv_read:
#         print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10}")

#5 Write a Python program to take user input and
# write it to a new row in a CSV file named data.csv.
# import csv
# name = input("enter name:")
# age = input("enter age:")
# city = input("enter city:")
#
# with open('data.csv', 'a', newline='') as file:
#     csv_write = csv.writer(file)
#     csv_write.writerow([name, age, city])
# print("data written to 'data.csv'")

#6
# Write a Python program to read data from a json
# file named json.csv and display them on the screen
# import json
#
# data = {
#     "people": [
#         {"name": "John", "age":28, "city": "Dallas"},
#         {"name": "Alex", "age":26, "city": "Austin"},
#         {"name": "Bob", "age":23, "city": "San"}
#
#     ]
# }
#
# with open('json.csv', 'w') as file:
#     json.dump(data, file, indent=4)
# print("'json.csv' created")
#
# import json
# with open('json.csv', 'r') as file:
#     data = json.load(file)
#     print(json.dumps(data, indent=4))

#7 Write a Python program to read data
# from a json file named yaml and display them on the screen

import yaml
import json

data = {
    "people": [
        {"name": "John", "age":28, "city": "Dallas"},
        {"name": "Alex", "age":26, "city": "Austin"},
        {"name": "Bob", "age":23, "city": "San"}

    ]
}

with open('yaml', 'w') as file:
    json.dump(data, file, indent=2)
print("'yaml' created")

with open('yaml', 'r') as file:
    data = yaml.safe_load(file)
print(data)
