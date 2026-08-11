# Main program for Functions and Modules assignment

from module_utils import greet_user, calculate_area, get_birth_year

if __name__ == "__main__":
    print(greet_user("Student"))

    width = 5
    height = 3
    area = calculate_area(width, height)
    print(f"The area of a {width}x{height} rectangle is {area}.")

    current_year = int(input("Enter the current year: "))
    age = int(input("Enter your age: "))
    birth_year = get_birth_year(current_year, age)
    print(f"You were born in {birth_year}.")
