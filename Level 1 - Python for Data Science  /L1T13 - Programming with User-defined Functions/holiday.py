# Practical Task 1 - A program that calculates holiday costs
#
# This program will take user input and calculate the cost of their holidays.

print("This program helps you calculate your holiday costs.")
print("There are special offers for the following destinations. Please choose one:")

# This code block gets gets user info for their preferred city, hotel stay
# and car rental.
city_flight = input('''L - London
P - Paris
S - Stockholm
H - Ho Chi Minh City
T - Tokyo
M - Mexico City
B - Barranquilla
C - Cape Town
F - Fez
: ''').upper()
num_nights = int(input("How many nights would you like to stay at the hotel? "))
rental_days = int(input("How many days would you like to hire a car for? "))


# This code block creates functions that calculate the hotel cost, plane cost
# and car rental cost.
# The hotel costs per night and car rental cost have been predetermined.
def hotel_cost(num_nights):
    return 100 * num_nights


def plane_cost(city_flight):
    if city_flight == "L":
        return 500
    elif city_flight == "P":
        return 300
    elif city_flight == "S":
        return 600
    elif city_flight == "H":
        return 1500
    elif city_flight == "T":
        return 2000
    elif city_flight == "M":
        return 1400
    elif city_flight == "B":
        return 1200
    elif city_flight == "C":
        return 1700
    elif city_flight == "F":
        return 400
    else:
        print("Sorry, that is not a valid option. Please start again.")


def destination_city(city_flight):
    if city_flight == "L":
        return "London"
    elif city_flight == "P":
        return "Paris"
    elif city_flight == "S":
        return "Stockholm"
    elif city_flight == "H":
        return "Ho Chi Minh City"
    elif city_flight == "T":
        return "Tokyo"
    elif city_flight == "M":
        return "Mexico City"
    elif city_flight == "B":
        return "Barranquilla"
    elif city_flight == "C":
        return "Cape Town"
    elif city_flight == "F":
        return "Fez"


def car_rental(rental_days):
    return rental_days * 70


# This code creates a function that takes num_days, city_flight
# and rental_days as arguments.
# The function calls the previously defined functions
# and calculates the total cost.
def holiday_cost(num_nights, city_flight, rental_days):
    total_cost = hotel_cost(num_nights) 
    + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost


# This code prints the holiday details in a user-friendly way.
print("\n##### Holiday Summary #####")
print("\nYour destination:\t", destination_city(city_flight))
print("─"*45)
print("Flight costs:\t\t$", plane_cost(city_flight))
print("Hotel cost:\t\t$", hotel_cost(num_nights))
print("Car rental cost:\t$", car_rental(rental_days))
print("─"*45)
print("Total Costs:\t\t$", holiday_cost(num_nights, city_flight, rental_days))
print("─"*45)
