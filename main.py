import random  # This imports random tools for making booking references.
import string  # This imports letter and number sets.


def create_seat_map():  # This function creates all seats.
    seats = {}  # This dictionary stores seat status.

    for column in range(1, 81):  # This loop creates seat numbers from 1 to 80.
        seats[str(column) + "A"] = "F"  # Seat A is free at first.
        seats[str(column) + "B"] = "F"  # Seat B is free at first.
        seats[str(column) + "C"] = "F"  # Seat C is free at first.
        seats[str(column) + "D"] = "F"  # Seat D is free at first.
        seats[str(column) + "E"] = "F"  # Seat E is free at first.
        seats[str(column) + "F"] = "F"  # Seat F is free at first.

    seats["10D"] = "S"  # This seat is used for storage.
    seats["10E"] = "S"  # This seat is used for storage.
    seats["10F"] = "S"  # This seat is used for storage.

    return seats


def create_booking_database():  # This function creates the booking database.
    return {}


def is_valid_seat_code(seat_code):  # This function checks if a seat code is valid.
    if len(seat_code) < 2:  # A seat code must have at least 2 characters.
        return False

    row = seat_code[:-1]  # This gets the seat number part.
    column = seat_code[-1]  # This gets the seat letter part.

    if not row.isdigit():  # This checks if the number part is really a number.
        return False

    if int(row) < 1 or int(row) > 80:  # This checks if the seat number is between 1 and 80.
        return False

    if column not in ["A", "B", "C", "D", "E", "F"]:  # This checks if the seat letter is allowed.
        return False

    return True


def generate_booking_reference(bookings):  # This function makes a unique booking reference.
    characters = string.ascii_uppercase + string.digits  # This creates a list of letters and numbers.

    while True:  # This repeats until a unique reference is made.
        reference = "".join(random.choice(characters) for _ in range(8))  # This creates 8 random characters.
        if reference not in bookings:  # This checks if the reference is already used.
            return reference


def check_availability(seats, seat_code):  # This function checks the status of one seat.
    if not is_valid_seat_code(seat_code):  # This checks if the input seat code is correct.
        print("Invalid seat code.")  # This shows an error message.
        return

    status = seats[seat_code]  # This gets the current value of the seat.

    if status == "F":  # This checks if the seat is free.
        print(f"Seat {seat_code} is available.")  # This tells the user the seat is free.
    elif status == "S":  # This checks if the seat is a storage seat.
        print(f"Seat {seat_code} is a storage area and cannot be booked.")  # This tells the user it cannot be booked.
    else:  # This means the seat has a booking reference.
        print(f"Seat {seat_code} is already reserved.")  # This tells the user the seat is reserved.


def book_seat(seats, bookings, seat_code):  # This function books a seat.
    if not is_valid_seat_code(seat_code):  # This checks if the seat code is valid.
        print("Invalid seat code.")  # This shows an error message.
        return

    status = seats[seat_code]  # This gets the current seat status.

    if status == "S":  # This checks if the seat is for storage.
        print(f"Seat {seat_code} is a storage area and cannot be booked.")  # This tells the user it cannot be booked.
    elif status != "F":  # This checks if the seat is not free.
        print(f"Seat {seat_code} is already reserved.")  # This tells the user the seat is already booked.
    else:  # This means the seat is free.
        passport_number = input("Enter passport number: ").strip()  # This gets the passport number.
        first_name = input("Enter first name: ").strip()  # This gets the first name.
        last_name = input("Enter last name: ").strip()  # This gets the last name.

        booking_reference = generate_booking_reference(bookings)  # This makes a unique booking reference.
        seat_row = seat_code[:-1]  # This gets the seat number part.
        seat_column = seat_code[-1]  # This gets the seat letter part.

        seats[seat_code] = booking_reference  # This stores the booking reference in the seat map.

        bookings[booking_reference] = {  # This creates a new booking record.
            "passport_number": passport_number,  # This stores the passport number.
            "first_name": first_name,  # This stores the first name.
            "last_name": last_name,  # This stores the last name.
            "seat_row": seat_row,  # This stores the seat row.
            "seat_column": seat_column,  # This stores the seat column.
        }

        print(f"Seat {seat_code} has been booked successfully.")  # This shows a success message.
        print(f"Booking reference: {booking_reference}")  # This shows the booking reference.


def free_seat(seats, bookings, seat_code):  # This function frees a booked seat.
    if not is_valid_seat_code(seat_code):  # This checks if the seat code is valid.
        print("Invalid seat code.")  # This shows an error message.
        return

    status = seats[seat_code]  # This gets the current seat status.

    if status == "S":  # This checks if the seat is a storage seat.
        print(f"Seat {seat_code} is a storage area and cannot be freed.")  # This tells the user it cannot be changed.
    elif status == "F":  # This checks if the seat is already free.
        print(f"Seat {seat_code} is already free.")  # This tells the user it is already free.
    else:  # This means the seat is booked.
        booking_reference = seats[seat_code]  # This gets the booking reference from the seat.

        seats[seat_code] = "F"  # This changes the seat back to free.

        if booking_reference in bookings:  # This checks if the booking exists in the database.
            del bookings[booking_reference]  # This removes the booking details.

        print(f"Seat {seat_code} is now free.")  # This shows a success message.


def show_booking_status(seats):  # This function shows the full seat map.
    print("\nApache Airlines Booking Status")  # This prints the title.
    print("Legend: F = Free, R = Reserved, S = Storage, X = Aisle")  # This explains the symbols.
    print("-" * 242)  # This prints a line.

    print(" " + "".join(f"{i:>3}" for i in range(1, 81)))  # This prints the seat numbers.

    def display_value(seat_code):  # This helper function changes display values.
        value = seats[seat_code]  # This gets the real value of the seat.
        if value == "F" or value == "S":  # This checks if the seat is free or storage.
            return value
        return "R"

    print("A" + "".join(f"{display_value(str(i) + 'A'):>3}" for i in range(1, 81)))  # This prints row A.
    print("B" + "".join(f"{display_value(str(i) + 'B'):>3}" for i in range(1, 81)))  # This prints row B.
    print("C" + "".join(f"{display_value(str(i) + 'C'):>3}" for i in range(1, 81)))  # This prints row C.
    print(" " + "".join(f"{'X':>3}" for i in range(1, 81)))  # This prints the aisle line.
    print("D" + "".join(f"{display_value(str(i) + 'D'):>3}" for i in range(1, 81)))  # This prints row D.
    print("E" + "".join(f"{display_value(str(i) + 'E'):>3}" for i in range(1, 81)))  # This prints row E.
    print("F" + "".join(f"{display_value(str(i) + 'F'):>3}" for i in range(1, 81)))  # This prints row F.

    print("-" * 242)  # This prints the bottom line.


def find_first_available_seat(seats):  # This function finds the first free seat.
    for column in range(1, 81):  # This checks seat numbers from 1 to 80.
        for row in ["A", "B", "C", "D", "E", "F"]:  # This checks each seat letter.
            seat_code = str(column) + row  # This builds the seat code.
            if seats[seat_code] == "F":  # This checks if the seat is free.
                print(f"The first available seat is {seat_code}.")  # This shows the first free seat.
                return

    print("No available seats found.")  # This runs if all seats are full.


def show_all_bookings(bookings):  # This function shows all booking records.
    if not bookings:  # This checks if the booking database is empty.
        print("No booking records found.")  # This shows a message if there are no bookings.
        return

    print("\nBooking Database Records")  # This prints the title.
    print("-" * 80)  # This prints a line.
    for reference, details in bookings.items():  # This goes through each booking record.
        print(  # This prints one full booking record.
            f"Reference: {reference}, Passport: {details['passport_number']}, "  # This prints the reference and passport.
            f"Name: {details['first_name']} {details['last_name']}, "  # This prints the traveller name.
            f"Seat: {details['seat_row']}{details['seat_column']}"  # This prints the seat code.
        )
    print("-" * 80)  # This prints the bottom line.


def main():  # This is the main function of the program.
    seats = create_seat_map()  # This creates the seat map.
    bookings = create_booking_database()  # This creates the booking database.

    while True:  # This keeps the menu running until the user exits.
        print("\nApache Airlines Seat Booking System")  # This prints the program title.
        print("1. Check availability of seat")  # This prints menu option 1.
        print("2. Book a seat")  # This prints menu option 2.
        print("3. Free a seat")  # This prints menu option 3.
        print("4. Show booking status")  # This prints menu option 4.
        print("5. Exit program")  # This prints menu option 5.
        print("6. Find first available seat")  # This prints menu option 6.
        print("7. Show booking database")  # This prints menu option 7.

        choice = input("Enter your choice: ").strip()  # This gets the user menu choice.

        if choice == "1":  # This runs option 1.
            seat_code = input("Enter seat code (for example 12C): ").strip().upper()  # This gets a seat code.
            check_availability(seats, seat_code)  # This checks the seat status.
        elif choice == "2":  # This runs option 2.
            seat_code = input("Enter the seat code to book: ").strip().upper()  # This gets a seat code.
            book_seat(seats, bookings, seat_code)  # This books the seat.
        elif choice == "3":  # This runs option 3.
            seat_code = input("Enter the seat code to free: ").strip().upper()  # This gets a seat code.
            free_seat(seats, bookings, seat_code)  # This frees the seat.
        elif choice == "4":  # This runs option 4.
            show_booking_status(seats)  # This shows the seat map.
        elif choice == "5":  # This runs option 5.
            print("Program terminated.")  # This shows the exit message.
            break  # This stops the program.
        elif choice == "6":  # This runs option 6.
            find_first_available_seat(seats)  # This finds the first free seat.
        elif choice == "7":  # This runs option 7.
            show_all_bookings(bookings)  # This shows all booking records.
        else:  # This runs when the input is not valid.
            print("Invalid menu option. Please try again.")  # This shows an error message.


main()  # This starts the program.