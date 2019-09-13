"""
8-13. User Profile: Start with a copy of user_profile.py from page 153.
Build a profile of yourself by calling build_profile(), using your first
and last names and three other key-value pairs that describe you.
"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}  # create empty dictionary
    profile['first_name'] = first  # add first name to dictionary
    profile['last_name'] = last  # add last name to dictionary
    for key, value in user_info.items():
        profile[key] = value  # store values in dictionary
    return profile

# butild my profile
user_profile = build_profile('Angelica', 'Rodriguez',
                            country = 'Mexico',
                            field = 'Computer Science',
                            age = '20 years')
print(user_profile)  # print profile
