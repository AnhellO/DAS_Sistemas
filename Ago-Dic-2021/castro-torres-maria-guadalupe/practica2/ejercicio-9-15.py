from random import choice

def get_winning_ticket(possibilities):
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []

    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False


max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("Tenemos un boleto ganador!")
    print(f"Su boleto: {new_ticket}")
    print(f"Boleto ganador:  {winning_ticket}")
    print(f"Solo se necesitaron {plays} intentos para ganar!")
else:
    print(f"Intenté  {plays} veces, sin sacar un ganador :(")
    print(f"Tu boleto: {new_ticket}")
    print(f"Boleto ganador: {winning_ticket}")