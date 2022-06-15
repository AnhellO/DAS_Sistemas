""" Practica 8-13 - User Profile

Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you."""

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Raúl', 'Alvarado',
                            location='Saltillo',
                            field='Ingeniería de sistemas')
print(user_profile)