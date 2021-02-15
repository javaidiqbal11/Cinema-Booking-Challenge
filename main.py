# Cinema Booking Challenge
seats = []
seats.append([0, 0, 1, 1, 0, 1, 1, 1])
seats.append([0, 1, 1, 0, 0, 1, 0, 1])
seats.append([1, 0, 0, 1, 0, 1, 1, 0])
seats.append([0, 1, 1, 1, 0, 0, 0, 1])
seats.append([0, 0, 1, 1, 0, 1, 0, 0])
seats.append([1, 0, 1, 1, 0, 0, 1, 1])


def displayBookings():
    # Display Bookings
    print("")
    print("======================================")
    print("")
    for row in seats:
        print(row)
    print("")
    print("======================================")


def checkSeat():
    row = int(input("Enter a row number (between 0 and 5)"))
    column = int(input("Enter a column number (between 0 and 7)"))

    if seats[row][column] == 1:
        print("This seat is already booked.")
    else:
        print("This seat is empty.")


# Main Program Starts Here
checkSeat()
