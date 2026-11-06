# Day 01 - Introduction to AapleSeva Project

# Project Card Variables
product = "AapleSeva Citizen Services Assistant"
user = "Citizens of Maharashtra, students, and farmers"
problem = "Difficulty in understanding required documents and eligibility rules for government certificates like Income, Caste, and Domicile"
data_source = "Official Aaple Sarkar Portal (https://aaplesarkar.mahaonline.gov.in)"

# Printing Project Card using variables and f-strings
print("=" * 60)
print(f"Product     : {product}")
print(f"Target User : {user}")
print(f"Problem     : {problem}")
print(f"Data Source : {data_source}")
print("=" * 60)

# Taking input from the user
name = input("\nEnter your name: ")
question = input("Enter your question about AapleSeva: ")

# Printing output with f-strings
print(f"\nHello {name}!")
print(f"Your question: '{question}'")
print("Thank you for reaching out, we will assist you soon.")
