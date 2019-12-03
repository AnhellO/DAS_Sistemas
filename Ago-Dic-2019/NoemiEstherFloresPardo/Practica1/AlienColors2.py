"""5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block."""

#If block
alien_color = 'green'

if alien_color == 'green':
    print("Acabas de ganar 5 puntos!")
else:
    print("Acabas de ganar 10 puntos!")

#Else block
alien_color = 'yellow'

if alien_color == 'green':
    print("Acabas de ganar 5 puntos!")
else:
    print("Acabas de ganar 10 puntos!")