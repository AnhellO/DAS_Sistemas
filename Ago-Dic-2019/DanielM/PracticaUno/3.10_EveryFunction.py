# 3-10. Every Function: Think of something you could store in a list.
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
# Write a program that creates a list containing these items and then uses each function introduced
# in this chapter at least once.

countries = ['Mexico', 'United States', 'Canada', 'Germany', 'Russia']
# --------------------------------------------------------------------------
print(countries[2])
# --------------------------------------------------------------------------
message = "I live in " + countries[0] + "."
print(message)
# --------------------------------------------------------------------------
print(countries)
del (countries[1])
countries.insert(1, 'Japan')
print(countries)
# --------------------------------------------------------------------------
countries.append('Chile')
print(countries)
# --------------------------------------------------------------------------
print(countries.pop())
print(countries)
# --------------------------------------------------------------------------
print(sorted(countries))
# --------------------------------------------------------------------------
print(sorted(countries, reverse=True))
# --------------------------------------------------------------------------
countries.reverse()
print(countries)
# --------------------------------------------------------------------------
countries.sort()
print(countries)
# --------------------------------------------------------------------------
countries.sort(reverse=True)
print(countries)