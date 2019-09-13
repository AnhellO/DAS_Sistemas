"""7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready."""

mesa = input("¿Para cuantas personas quiere la mesa? ")
mesa = int(mesa)

if mesa > 8:
    print("Lo siento, deberá esperar por una mesa.")
else:
    print("Su mesa esta lista.")