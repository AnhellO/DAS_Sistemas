def build_profile(first, last, **user_info):
    #8.13
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('Andrea', 'Garcia',
                             signo_sodiacal='Escorpio',
                             ciudad='Saltillo',
                             )
print(user_profile)
