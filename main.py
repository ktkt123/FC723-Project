def create_seat_map():  # This function makes the first seat map.
    seats = {}  # This dictionary stores all seat data.
    columns = ["A", "B", "C", "D", "E", "F"]  # These are the seat letters.

    for row in range(1, 81):  # This loop goes from row 1 to row 80.
        for col in columns:  # This loop goes through each seat letter.
            seat_code = str(row) + col  # This makes a seat code like 12C.
            seats[seat_code] = "F"  # All normal seats start as free.

    storage_seats = ["77D", "77E", "77F", "78D", "78E", "78F"]  # These seats are storage areas.

    for seat_code in storage_seats:  # This loop changes storage seats.
        seats[seat_code] = "S"  # Storage seats cannot be booked.

    return seats  # This gives the finished seat map back.


def is_valid_seat_code(seat_code):  # This function checks the seat code.
    if len(seat_code) < 2:  # A seat code must have at least 2 characters.
        return False  # This seat code is not valid.

    row_text = seat_code[:-1]  # This gets the row number part.
    column = seat_code[-1]  # This gets the seat letter part.

    if not row_text.isdigit():  # The row part must be a number.
        return False  # This seat code is not valid.

    row_number = int(row_text)  # This changes the row part into a number.

    if row_number < 1 or row_number > 80:  # The row must be between 1 and 80.
        return False  # This seat code is not valid.

    if column not in ["A", "B", "C", "D", "E", "F"]:  # The letter must be A to F.
        return False  # This seat code is not valid.

    return True  # This seat code is valid.


def check_availability(seats, seat_code):  # This function checks one seat.
    if not is_valid_seat_code(seat_code):  # First it checks the input.
        print("Invalid seat code.")  # This shows an error message.
        return  # This stops the function.

    status = seats[seat_code]  # This gets the seat status.

    if status == "F":  # This checks if the seat is free.
        print(f"Seat {seat_code} is available.")  # This shows the seat is free.
    elif status == "R":  # This checks if the seat is reserved.
        print(f"Seat {seat_code} is already reserved.")  # This shows the seat is booked.
    elif status == "S":  # This checks if the seat is storage.
        print(f"Seat {seat_code} is a storage area and cannot be booked.")  # This shows it is not a real seat.


def book_seat(seats, seat_code):  # This function books one seat.
    if not is_valid_seat_code(seat_code):  # First it checks the input.
        print("Invalid seat code.")  # This shows an error message.
        return  # This stops the function.

    status = seats[seat_code]  # This gets the seat status.

    if status == "S":  # This checks if the seat is storage.
        print(f"Seat {seat_code} is a storage area and cannot be booked.")  # This shows booking is not possible.
    elif status == "R":  # This checks if the seat is already booked.
        print(f"Seat {seat_code} is already reserved.")  # This shows the seat is taken.
    else:  # This means the seat is free.
        seats[seat_code] = "R"  # This changes the seat to reserved.
        print(f"Seat {seat_code} has been booked successfully.")  # This shows success.


def free_seat(seats, seat_code):  # This function frees one seat.
    if not is_valid_seat_code(seat_code):  # First it checks the input.
        print("Invalid seat code.")  # This shows an error message.
        return  # This stops the function.

    status = seats[seat_code]  # This gets the seat status.

    if status == "S":  # This checks if the seat is storage.
        print(f"Seat {seat_code} is a storage area and cannot be freed.")  # This shows it is not a normal seat.
    elif status == "F":  # This checks if the seat is already free.
        print(f"Seat {seat_code} is already free.")  # This shows nothing changed.
    else:  # This means the seat is reserved.
        seats[seat_code] = "F"  # This changes the seat to free.
        print(f"Seat {seat_code} is now free.")  # This shows success.


def show_booking_status(seats):  # This function prints the full seat table.
    print("\nApache Airlines Booking Status")  # This prints the title.
    print("Legend: F = Free, R = Reserved, S = Storage, X = Aisle")  # This explains symbols.
    print("-" * 242)  # This prints a line.

    print(" " + "".join(f"{i:>3}" for i in range(1, 81)))  # This prints seat numbers.

    print("A" + "".join(f"{seats[str(i) + 'A']:>3}" for i in range(1, 81)))  # This prints row A.
    print("B" + "".join(f"{seats[str(i) + 'B']:>3}" for i in range(1, 81)))  # This prints row B.
    print("C" + "".join(f"{seats[str(i) + 'C']:>3}" for i in range(1, 81)))  # This prints row C.
    print(" " + "".join(f"{'X':>3}" for i in range(1, 81)))  # This prints the aisle.
    print("D" + "".join(f"{seats[str(i) + 'D']:>3}" for i in range(1, 81)))  # This prints row D.
    print("E" + "".join(f"{seats[str(i) + 'E']:>3}" for i in range(1, 81)))  # This prints row E.
    print("F" + "".join(f"{seats[str(i) + 'F']:>3}" for i in range(1, 81)))  # This prints row F.

    print("-" * 242)  # This prints the end line.


def find_first_available_seat(seats):  # This function finds the first free seat.
    for row in range(1, 81):  # This loop checks rows from front to back.
        for col in ["A", "B", "C", "D", "E", "F"]:  # This loop checks seats in order.
            seat_code = str(row) + col  # This makes a seat code.
            if seats[seat_code] == "F":  # This checks if the seat is free.
                print(f"The first available seat is {seat_code}.")  # This shows the result.
                return  # This stops after the first free seat.

    print("There are no available seats.")  # This shows all seats are full.


def main():  # This is the main menu function.
    seats = create_seat_map()  # This makes the first seat map.

    while True:  # This keeps the menu running.
        print("\nApache Airlines Seat Booking System")  # This prints the menu title.
        print("1. Check availability of seat")  # This prints menu option 1.
        print("2. Book a seat")  # This prints menu option 2.
        print("3. Free a seat")  # This prints menu option 3.
        print("4. Show booking status")  # This prints menu option 4.
        print("5. Exit program")  # This prints menu option 5.
        print("6. Find first available seat")  # This prints the extra function.

        choice = input("Enter your choice: ").strip()  # This gets the menu choice.

        if choice == "1":  # This runs the check function.
            seat_code = input("Enter seat code (for example 12C): ").strip().upper()  # This gets the seat code.
            check_availability(seats, seat_code)  # This checks the seat.
        elif choice == "2":  # This runs the booking function.
            seat_code = input("Enter the seat code to book: ").strip().upper()  # This gets the seat code.
            book_seat(seats, seat_code)  # This books the seat.
        elif choice == "3":  # This runs the free function.
            seat_code = input("Enter the seat code to free: ").strip().upper()  # This gets the seat code.
            free_seat(seats, seat_code)  # This frees the seat.
        elif choice == "4":  # This runs the display function.
            show_booking_status(seats)  # This shows the seat map.
        elif choice == "5":  # This stops the program.
            print("Program terminated.")  # This shows the end message.
            break  # This ends the loop.
        elif choice == "6":  # This runs the extra function.
            find_first_available_seat(seats)  # This finds the first free seat.
        else:  # This handles wrong input.
            print("Invalid menu option. Please try again.")  # This shows an error message.


if __name__ == "__main__":  # This starts the program file.
    main()  # This runs the main function.