def build_profile(first, last, **user_info):

    profile = {}

    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    
    return profile


user_profile = build_profile('Juan', 'Calzoncit', location = 'Saltillo', field = 'Systems Engineering', semester = 7)
print(user_profile)