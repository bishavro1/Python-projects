def print_centered(s):
    console_width = 80
    print(s.center(console_width))

class Ticket:
    def __init__(self, passenger_name, journey_date, destination, seat_number):
        self.passenger_name = passenger_name
        self.journey_date = journey_date
        self.destination = destination
        self.seat_number = seat_number

    def __str__(self):
        return f"Ticket for {self.passenger_name} on {self.journey_date} to {self.destination} with seat number {self.seat_number}"


class OnlineReservation:
    def __init__(self):
        self.accounts = {}
        self.last_seat_number = 0

    def create_account(self, mobile, name, pin):
        if mobile in self.accounts:
            print("\nAn account with this number already exists!\n")
        else:
            new_account = {"mobile": mobile, "name": name, "pin": pin, "tickets": []}
            self.accounts[mobile] = new_account
            print("\nAccount created successfully.\n")

    def login(self, mobile, pin):
        if mobile in self.accounts and self.accounts[mobile]['pin'] == pin:
            return self.accounts[mobile]
        else:
            print("\nIncorrect mobile or PIN.\n")
            return None

    def book_ticket(self, user):
        self.last_seat_number += 1
        passenger_name = input("Enter passenger name: ")
        journey_date = input("Enter journey date (e.g., DD-MM-YYYY): ")
        destination = input("Enter destination: ")
        ticket = Ticket(passenger_name, journey_date, destination, self.last_seat_number)
        user["tickets"].append(ticket)
        print(f"\n{ticket}\n")

    def cancel_reservation(self, user, seat_number):
        for ticket in user["tickets"]:
            if ticket.seat_number == int(seat_number):
                user["tickets"].remove(ticket)
                print(f"\nTicket with seat number {seat_number} cancelled.\n")
                return
        print("\nTicket not found.\n")

    def view_tickets(self, user):
        if not user["tickets"]:
            print("\nNo tickets found.\n")
            return

        print("\nYour Tickets:")
        for ticket in user["tickets"]:
            print(ticket)

    def delete_account(self, mobile, pin):
        if mobile in self.accounts and self.accounts[mobile]['pin'] == pin:
            del self.accounts[mobile]
            print("\nAccount deleted successfully.\n")
        else:
            print("\nIncorrect mobile or PIN.\n")


def main():
    registration = OnlineReservation()
    print_centered("Welcome to the Online Reservation System of BANGLADESH RAILWAY!")

    while True:
        print_centered("=" * 15 + " MENU " + "=" * 15)
        print_centered("1. Sign Up")
        print_centered("2. Log In")
        print_centered("3. Delete Account")
        print_centered("4. Exit")
        print_centered("=" * 33)

        choice = input("\nEnter your choice, Please: ")

        if choice == "1":
            mobile = input("Enter your mobile number: ")
            name = input("Enter your name: ")
            pin = input("Enter your new PIN: ")
            registration.create_account(mobile, name, pin)

        elif choice == "2":
            mobile = input("Enter mobile number: ")
            pin = input("Enter your PIN: ")
            user = registration.login(mobile, pin)
            if user:
                while True:
                    print_centered("=" * 12 + " USER MENU " + "=" * 12)
                    print_centered("1. Book Ticket")
                    print_centered("2. Cancel Ticket")
                    print_centered("3. View Tickets")
                    print_centered("4. Log Out")
                    print_centered("=" * 30)

                    user_choice = input("\nEnter your choice: ")

                    if user_choice == "1":
                        registration.book_ticket(user)

                    elif user_choice == "2":
                        seat_number = input("Enter seat number to cancel: ")
                        registration.cancel_reservation(user, seat_number)

                    elif user_choice == "3":
                        registration.view_tickets(user)

                    elif user_choice == "4":
                        print("\nLogged out successfully!\n")
                        break

                    else:
                        print("\nInvalid choice!\n")

        elif choice == "3":
            mobile = input("Enter mobile number: ")
            pin = input("Enter your PIN: ")
            registration.delete_account(mobile, pin)

        elif choice == "4":
            print("\nThank you for using the Online Reservation System!\n")
            break

        else:
            print("\nInvalid choice!\n")


if __name__ == '__main__':
    main()
