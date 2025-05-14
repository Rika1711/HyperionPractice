# Python: `holiday.py`

This program calculates the total holiday cost for a user, incorporating expenses for flights, hotel stays, and car rentals.

## Code Description

1.  Creates a Python file named `holiday.py`.
2.  Prompts the user for the following inputs:
    * `city_flight`: The destination city for the flight. The program provides a set of city options with corresponding flight costs.
    * `num_nights`: The number of nights for the hotel stay.
    * `rental_days`: The number of days for car rental.
3.  Defines four functions:
    * `hotel_cost(num_nights)`:
        * Calculates the total hotel cost by multiplying the number of nights by a fixed nightly rate.
        * Returns the total hotel cost.
    * `plane_cost(city_flight)`:
        * Determines the flight cost based on the destination city using `if`/`elif`/`else` statements.
        * Returns the flight cost.
    * `car_rental(rental_days)`:
        * Calculates the total car rental cost by multiplying the rental days by a fixed daily rate.
        * Returns the total car rental cost.
    * `holiday_cost(num_nights, city_flight, rental_days)`:
        * Calculates the total holiday cost by calling the `hotel_cost()`, `plane_cost()`, and `car_rental()` functions.
        * Returns the sum of the returned costs.
4.  Calls the `holiday_cost()` function with the user's input values.
5.  Displays a formatted summary of the holiday details, including the destination city, number of nights, rental days, and the breakdown of costs (flight, hotel, car rental, and total).

## How to Run the Program

1.  Ensure Python is installed on your system.
2.  Save the Python code as `holiday.py`.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved `holiday.py` using the `cd` command.
5.  Execute the program by running the command: `python holiday.py`
