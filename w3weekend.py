class Parkinggarage:
    def __init__(self, num_tickets=10, num_parking_space=10):
        self.tickets = [i for i in range(1, num_tickets + 1)]
        self.num_parking_space = [i for i in range(1, num_parking_space + 1)]
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets:
            ticket = self.tickets.pop()
            parking_space = self.num_parking_space.pop()
            self.current_ticket[ticket] = {'paid': False, 'parking space': parking_space}
            print(f'you have taken ticket {ticket} and parking space {parking_space}.')
        else:
            print('Sorry, no more spcae in the parking garqage.')

    def pay_for_parking(self):
        ticket_num = int(input('please enter ticket number you want to pay for parking:'))
        if self.current_ticket(ticket_num):
            if not self.current_ticket[ticket_num]['paid']:
                payment = input('please enter payment amount:')
                self.current_ticket[ticket_num]['paid'] = True
                print(f'you have paid {payment} for ticket {ticket_num}.')
            else:
                print('Sorry, ticket already paid.')
        else:
            print('sorry, ticket not found.')

    def leave_garage(self):
        ticket_num = int(input('please enter ticket number you want to leave:'))
        if self.current_ticket(ticket_num):
            if self.current_ticket[ticket_num]['paid']:
                print('Thank you for your payment. have a nice day.')
                parking_space = self.current_ticket[ticket_num]['parking space']
                self.num_parking_space.append(parking_space)
                del self.current_ticket[ticket_num]
            else:
                print('sorry, ticket not found.')



my_garage = Parkinggarage()
my_garage.take_ticket()
my_garage.pay_for_parking()
my_garage.leave_garage()


print(my_garage.current_ticket)

# print(my_garage.parkingspace)

print(my_garage.num_parking_space)





    
        

        