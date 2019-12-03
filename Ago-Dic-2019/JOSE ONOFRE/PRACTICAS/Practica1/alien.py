alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])


new_points = alien_0['points']
print("Acabas de ganar "+str(new_points)+" puntos!")

print("////////////////////////////")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("////////////////////////////")
print()

alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

print("////////////////////////////")
print()

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_2['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
     x_increment = 3
# The new position is the old position plus the increment.
alien_2['x_position'] = alien_2['x_position'] + x_increment
print("New x-position: " + str(alien_2['x_position']))