# 6-6. Polling: Use the code in favorite_languages.py (page 104).

# • Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have already taken the poll,
# print a message thanking them for responding. If they have not yet taken the poll, print a message
# inviting them to take the poll.

favorite_languages = {
    'Daniel': 'python',
    'Eduardo': 'c',
    'Juan': 'java',
    'Roberto': 'java',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

print("\n")

friends = ['Daniel', 'Luis', 'Carlos', 'Roberto', 'Horacio', 'Jorge']
for friend in friends:
    if friend in favorite_languages.keys():
        print("Thank you for taking the poll, " + friend.title() + "!")
    else:
        print(friend.title() + ", what's your favorite programming language?")

