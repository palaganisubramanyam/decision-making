'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
'''

def calculate_age():
    birth_year_last_two = int(input("Enter your birth year (last 2 digits): "))
    current_year_last_two = int(input("Enter the current year (last 2 digits): "))
    birth_year = 1900 + birth_year_last_two if birth_year_last_two >= 20 else 2000 + birth_year_last_two
    current_year = 1900 + current_year_last_two if current_year_last_two >= 20 else 2000 + current_year_last_two
    age = current_year - birth_year
    print(age)
calculate_age()
