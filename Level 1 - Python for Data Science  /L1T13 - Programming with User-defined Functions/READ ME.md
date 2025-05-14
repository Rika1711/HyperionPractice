# Python: `holiday.py`

This program calculates a user's total holiday cost, including plane cost, hotel cost, and car rental cost.

## Code Description

1.  Creates a new Python file named `holiday.py`.
2.  Gets the following user inputs:
    * `city_flight`: The city they will be flying to.  The program provides some city options with associated costs.
    * `num_nights`: The number of nights they will be staying at a hotel.
    * `rental_days`: The number of days for which they will be hiring a car.
3.  Defines the following four functions:
    * `hotel_cost(num_nights)`:
        * Takes `num_nights` as an argument.
        * Calculates the total hotel cost by multiplying `num_nights` by a fixed price per night.
        * Returns the total hotel cost.
    * `plane_cost(city_flight)`:
        * Takes `city_flight` as an argument.
        * Uses `if`/`elif`/`else` statements to determine the flight cost based on the selected city.
        * Returns the flight cost.
    * `car_rental(rental_days)`:
        * Takes `rental_days` as an argument.
        * Calculates the total car rental cost by multiplying `rental_days` by a fixed daily rate.
        * Returns the total car rental cost.
    * `holiday_cost(num_nights, city_flight, rental_days)`:
        * Takes `num_nights`, `city_flight`, and `rental_days` as arguments.
        * Calls the `hotel_cost()`, `plane_cost()`, and `car_rental()` functions with their respective arguments.
        * Calculates the total holiday cost by summing the results of the function calls.
        * Returns the total holiday cost.
4.  Calls the `holiday_cost()` function with the user-provided inputs.
5.  Prints out all the details about the holiday in a user-friendly format, including the chosen city, number of nights, rental days, and the cost breakdown (hotel, flight, car rental, and total).

## How to Run the Program

1.  Ensure you have Python installed.
2.  Save the Python file as `holiday.py`.
3.  Open a command prompt or terminal.
4.  Navigate to the directory where you saved the file using the `cd` command.
5.  Run the program using the command: `python holiday.py`
