#1 Implement a hierarchy of shapes using classes. Create a superclass called Shape
# and subclasses for different shapes such as Circle, Rectangle, and Triangle.
# Include methods to calculate area and perimeter for each shape.

# import math
# from abc import ABC, abstractmethod
#
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
# class rectangle(shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# class triangle(shape):
#     def __init__(self, s1, s2, s3):
#         self.s1 = s1
#         self.s2 = s2
#         self.s3 = s3
#
#     def area(self):
#         s= (self.s1 + self.s2 + self.s3) / 2
#         return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
#
#     def perimeter(self):
#         return self.s1+self.s2+self.s3
#
# circle = circle(10)
# print(f"Circle: Area = {circle.area()}, Perimeter = {circle.perimeter()}")
#
# rectangle = rectangle(5, 10)
# print(f"Rectangle: Area = {rectangle.area()}, Perimeter = {rectangle.perimeter()}")
#
# triangle = triangle(3, 3, 3)
# print(f"Triangle: Area = {triangle.area()}, Perimeter = {triangle.perimeter()}")

#2 Design a Python program to manage student records. Implement c
# lasses for Student, Course, and Grade. Include methods for
# enrolling students in courses, recording grades, and generating
# transcripts.

# class Course:
#     def __init__(self, course_code, course_name):
#         self.course_code = course_code
#         self.course_name = course_name
#         self.enrolled_students = []
#
#     def enroll_student(self, student):
#         if student not in self.enrolled_students:
#             self.enrolled_students.append(student)
#             student.enroll_in_course(self)
#             print(f"{student.name} has been enrolled in {self.course_name}.")
#         else:
#             print(f"{student.name} is already enrolled in {self.course_name}.")
#
#     def record_grade(self, student, grade):
#         if student in self.enrolled_students:
#             student.add_grade(self, grade)
#             print(f"grade {grade} has been recorded in {student.name} in {self.course_name}.")
#         else:
#             print(f"{student.name} is not enrolled in {self.course_name}.")
#
# class Grade:
#     def __init__(self, course, grade):
#         self.course = course
#         self.garde = grade
#
#     def __str__(self):
#         return f"{self.course.course_name}: {self.garde}"
#
# class Student:
#     def __init__(self, student_id, name):
#         self.student_id =student_id
#         self.name = name
#         self.enrolled_courses = []
#         self.grades = {}
#
#     def enroll_in_courses(self, course):
#         self.enrolled_courses.append(course)
#
#     def add_grade(self, course, grade):
#         if course in self.enrolled_courses:
#             self.grades[course] = Grade(course, grade)
#         else:
#             print(f"{self.name} is not enrolled in {course.course_name}, so grade cannot be recorded.")
#
#     def generate_transcript(self):
#         print(f"\n Transcript for {self.name}:")
#         for course in self.enrolled_courses:
#             grade = self.grades.get(course)
#             if grade:
#                 print(grade)
#             else:
#                 print(f"{course.course_name}: No grade recorded.")
#
# course1 = Course("CS101", "Computer Science 101")
# course2 = Course("MATH101", "Calculus I")
# course3 = Course("PHY101", "Physics I")
#
# student1 = Student(1, "Alice")
# student2 = Student(2, "Bob")
#
# # Enroll students in courses
# course1.enroll_student(student1)
# course1.enroll_student(student2)
# course2.enroll_student(student1)
# course3.enroll_student(student1)
#
# # Record grades
# course1.record_grade(student1, "A")
# course1.record_grade(student2, "B")
# course2.record_grade(student1, "A")
#
# # Generate transcripts
# student1.generate_transcript()
# student2.generate_transcript()

#3 Implement a Python class FileUtility with methods
# for reading and writing files. Include methods for reading
# text files, writing to text files, and copying files.

# import shutil
#
#
# class FileUtility:
#
#     def read_text_file(self, file_path):
#         try:
#             with open(file_path, 'r') as file:
#                 content = file.read()
#             return content
#         except FileNotFoundError:
#             print(f"Error: The file at {file_path} does not exist.")
#         except Exception as e:
#             print(f"An error occurred while reading the file: {e}")
#
#     def write_text_file(self, file_path, content):
#         try:
#             with open(file_path, 'w') as file:
#                 file.write(content)
#             print(f"content has been written to {file_path}")
#         except Exception as e:
#             print(f"An error occurred while reading the file: {e}")
#
#     def append_to_text_file(self, file_path, content):
#         try:
#             with open(file_path, 'a') as file:
#                 file.write(content)
#             print(f"content has been written to {file_path}")
#         except Exception as e:
#             print(f"An error occurred while reading the file: {e}")
#
#     def copy_file(self, source_path, destination_path):
#         try:
#             shutil.copy(source_path, destination_path)
#             print(f"file has been copied from {source_path} to {destination_path}")
#         except FileNotFoundError:
#             print(f"Error: The source file at {source_path} does not exist.")
#         except Exception as e:
#             print(f"An error occurred while copying the file: {e}")
#
#
# file_util = FileUtility()
# file_util.write_text_file('exm.txt', 'Hello, this is test file.')
# file_util.append_to_text_file('exm.txt', '\n this is appended line.')
# content = file_util.read_text_file('exm.txt')
# print(content)
# file_util.copy_file('exm.txt', 'exm_copy.txt')

#4
# Create a Python class MathOperations with static methods for
# basic mathematical operations such as addition, subtraction,
# multiplication, and division. Also, include a class variable PI
# for the value of pi

# class MathOperations:
#     PI = 3.14159
#
#     @staticmethod
#     def add(a,b):
#         return a + b
#
#     @staticmethod
#     def sub(a, b):
#         return a - b
#
#     @staticmethod
#     def mul(a, b):
#         return a * b
#
#     @staticmethod
#     def divide(a,b):
#         if b == 0:
#             return "error"
#         return a / b
#
# # Accessing the PI class variable
# print("Value of PI:", MathOperations.PI)
#
# # Performing basic math operations
# sum_result = MathOperations.add(10, 5)
# print("Addition (10 + 5):", sum_result)
#
# diff_result = MathOperations.sub(10, 5)
# print("Subtraction (10 - 5):", diff_result)
#
# product_result = MathOperations.mul(10, 5)
# print("Multiplication (10 * 5):", product_result)
#
# division_result = MathOperations.divide(10, 5)
# print("Division (10 / 5):", division_result)
#
# # Handling division by zero
# error_result = MathOperations.divide(10, 0)
# print("Division by zero:", error_result)

#5
# Design a Python class ConfigParser with static methods
# for parsing configuration files in different formats
# (e.g., JSON, YAML). Include class variables for default
# configuration file paths and formats

# import json
# import yaml
# import os
#
# class ConfigParser:
#     DEFAULT_JSON_PATH = 'config.json'
#     DEFAULT_YAML_PATH = 'config.yaml'
#     DEFAULT_FORMAT = 'json'
#
#     @staticmethod
#     def parse_json(file_path=None):
#         if file_path is None:
#             file_path = ConfigParser.DEFAULT_JSON_PATH
#
#         if not os.path.exists(file_path):
#             raise FileNotFoundError(f"Configuration file not found: {file_path}")
#
#         with open(file_path, 'r') as file:
#             try:
#                 config_data = json.load(file)
#                 print(f"JSON config parsed from {file_path}:")
#                 return config_data
#             except json.JSONDecodeError as e:
#                 print(f"Error decoding JSON file: {e}")
#                 return None
#
#     @staticmethod
#     def parse_yaml(file_path = None):
#         if file_path is None:
#             file_path = ConfigParser.DEFAULT_YAML_PATH
#
#         if not os.path.exists(file_path):
#             raise FileNotFoundError(f"Configuration file not found: {file_path}")
#
#         with open(file_path, 'r') as file:
#             try:
#                 config_data = yaml.safe_load(file)
#                 print(f"YAML Config parsed from {file_path}:")
#                 return config_data
#             except yaml.YAMLError as e:
#                 print(f"error decoding YAML file: {e}")
#                 return None
#
#     @staticmethod
#     def load_config(format=None, file_path=None):
#         if format is None:
#             format = ConfigParser.DEFAULT_FORMAT
#
#             if format == 'json':
#                 return ConfigParser.parse_json(file_path)
#             elif format == 'yaml':
#                 return ConfigParser.parse_yaml(file_path)
#             else:
#                 print(f"Unsupported format: {format}")
#                 return None
#
#
# import json
#
# # Data to be written to the config.json
# # config_data = {
# #     "host": "localhost",
# #     "port": 8080,
# #     "debug": True
# # }
# #
# # # Writing data to config.json
# # with open('config.json', 'w') as json_file:
# #     json.dump(config_data, json_file, indent=4)
# #
# # print("config.json has been created and written.")
#
# json_config = ConfigParser.load_config(format='json')
# print(json_config)
#
# yaml_config = ConfigParser.load_config(format='yaml')
# print(yaml_config)
#
# custom_json_config = ConfigParser.load_config(format='json', file_path='custom_config.json')
# print(custom_json_config)

#6
# Design a Python class GeometryHelper with static methods
# for calculating the area and perimeter of common geometric shapes
# such as circles, rectangles, and triangles. Include class
# variables for default values such as the value of pi and
# standard lengths.

# import math
#
# class GeometryHelper:
#     # Class variables for default values
#     PI = 3.14159
#     DEFAULT_RADIUS = 5
#     DEFAULT_LENGTH = 10
#     DEFAULT_WIDTH = 6
#     DEFAULT_HEIGHT = 8
#
#     @staticmethod
#     def circle_area(radius=None):
#         """Calculate the area of a circle."""
#         if radius is None:
#             radius = GeometryHelper.DEFAULT_RADIUS
#         return GeometryHelper.PI * radius ** 2
#
#     @staticmethod
#     def circle_perimeter(radius=None):
#         """Calculate the perimeter (circumference) of a circle."""
#         if radius is None:
#             radius = GeometryHelper.DEFAULT_RADIUS
#         return 2 * GeometryHelper.PI * radius
#
#     @staticmethod
#     def rectangle_area(length=None, width=None):
#         """Calculate the area of a rectangle."""
#         if length is None:
#             length = GeometryHelper.DEFAULT_LENGTH
#         if width is None:
#             width = GeometryHelper.DEFAULT_WIDTH
#         return length * width
#
#     @staticmethod
#     def rectangle_perimeter(length=None, width=None):
#         """Calculate the perimeter of a rectangle."""
#         if length is None:
#             length = GeometryHelper.DEFAULT_LENGTH
#         if width is None:
#             width = GeometryHelper.DEFAULT_WIDTH
#         return 2 * (length + width)
#
#     @staticmethod
#     def triangle_area(base=None, height=None):
#         """Calculate the area of a triangle."""
#         if base is None:
#             base = GeometryHelper.DEFAULT_LENGTH
#         if height is None:
#             height = GeometryHelper.DEFAULT_HEIGHT
#         return 0.5 * base * height
#
#     @staticmethod
#     def triangle_perimeter(a=None, b=None, c=None):
#         """Calculate the perimeter of a triangle."""
#         if a is None:
#             a = GeometryHelper.DEFAULT_LENGTH
#         if b is None:
#             b = GeometryHelper.DEFAULT_WIDTH
#         if c is None:
#             c = GeometryHelper.DEFAULT_HEIGHT
#         return a + b + c
#
# # Circle calculations (using default radius)
# circle_area = GeometryHelper.circle_area()
# circle_perimeter = GeometryHelper.circle_perimeter()
#
# print(f"Circle Area (default radius): {circle_area}")
# print(f"Circle Perimeter (default radius): {circle_perimeter}")
#
# # Rectangle calculations (using default length and width)
# rectangle_area = GeometryHelper.rectangle_area()
# rectangle_perimeter = GeometryHelper.rectangle_perimeter()
#
# print(f"Rectangle Area (default dimensions): {rectangle_area}")
# print(f"Rectangle Perimeter (default dimensions): {rectangle_perimeter}")
#
# # Triangle calculations (using default base and height)
# triangle_area = GeometryHelper.triangle_area()
# triangle_perimeter = GeometryHelper.triangle_perimeter()
#
# print(f"Triangle Area (default dimensions): {triangle_area}")
# print(f"Triangle Perimeter (default dimensions): {triangle_perimeter}")
#
# # Custom Circle calculations (using custom radius)
# custom_circle_area = GeometryHelper.circle_area(radius=7)
# custom_circle_perimeter = GeometryHelper.circle_perimeter(radius=7)
#
# print(f"Custom Circle Area (radius 7): {custom_circle_area}")
# print(f"Custom Circle Perimeter (radius 7): {custom_circle_perimeter}")
#
# # Custom Rectangle calculations (using custom length and width)
# custom_rectangle_area = GeometryHelper.rectangle_area(length=12, width=8)
# custom_rectangle_perimeter = GeometryHelper.rectangle_perimeter(length=12, width=8)
#
# print(f"Custom Rectangle Area (12x8): {custom_rectangle_area}")
# print(f"Custom Rectangle Perimeter (12x8): {custom_rectangle_perimeter}")

'''
7
# Write a python program which hits the API and checks the response
'''
#
# import requests
#
# def check_api_response(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             print("Request was successful")
#             print("Response COntent:")
#             print(response.json())
#         else:
#             print(f"Request failed with status code: {response.status_code}")
#
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#
# api_url = "https://jsonplaceholder.typicode.com/posts"
#
# check_api_response(api_url)

'''
8
 Write a program which explains method overriding and overloading
'''

# class Animal:
#     def sound(self):
#         print("animal makes sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
#
# class Cat(Animal):
#     def sound(self):
#         print("cat meows")
#
# #method overloading
#
# class MathOperations:
#     def add(self, a, b=0, c=0):
#         return a + b + c
#
# print("Method Overriding Demonstration:")
# animal = Animal()
# animal.sound()  # Calls the parent class method
#
# dog = Dog()
# dog.sound()  # Calls the overridden method in Dog class
#
# cat = Cat()
# cat.sound()  # Calls the overridden method in Cat class
#
# print("\nMethod Overloading Demonstration:")
#
# # Demonstrating Method Overloading
# math = MathOperations()
#
# # Calling the add method with two arguments (overloading)
# print("Addition with two arguments:", math.add(5, 3))
#
# # Calling the add method with three arguments (overloading)
# print("Addition with three arguments:", math.add(5, 3, 2))
#
# # Calling the add method with one argument (overloading)
# print("Addition with one argument:", math.add(5))

'''
9
Create a package folder with two module1.py & module2.py files 
containing 4 functions and import the package with two specific 
functions
'''
# main.py
from my_package import add, multiply

# Using the imported functions
result_add = add(10, 5)  # This will call the 'add' function from module1
result_multiply = multiply(3, 7)  # This will call the 'multiply' function from module2

# Print the results
print(f"Addition Result: {result_add}")
print(f"Multiplication Result: {result_multiply}")
