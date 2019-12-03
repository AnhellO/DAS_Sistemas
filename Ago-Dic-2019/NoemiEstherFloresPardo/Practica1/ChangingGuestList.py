"""3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list."""

invitados = ['Teresa', 'Guadalupe', 'Rosendo']

name = invitados[0].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[1].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[2].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[1].title()
print("\nLo siento, " + name + " no puede llegar a cenar.")

# Cuando Guadalupe no puede.
del(invitados[1])
invitados.insert(1, 'Samuel')

# Imprimir las invitaciones de nuevo.
name = invitados[0].title()
print("\n" + name + ", te invito a cenar unos ricos taquitos!")

name = invitados[1].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[2].title()
print(name + ", te invito a cenar unos ricos taquitos!")