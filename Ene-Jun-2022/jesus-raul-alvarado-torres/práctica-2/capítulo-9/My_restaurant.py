"""9-10. Imported Restaurant:

Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant . Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is work-
ing properly."""

from Restaurant import Restaurant

channel_club = Restaurant('Los compadres', 'Chicharrones de res')
channel_club.describe_restaurant()
channel_club.open_restaurant()