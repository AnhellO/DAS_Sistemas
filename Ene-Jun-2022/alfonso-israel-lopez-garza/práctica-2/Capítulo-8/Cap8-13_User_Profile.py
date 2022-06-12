def build_profile(first, last, **user_info):
    """Constuye un diccionario que contenga todo lo que sabemos acerca del usuario."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Alfonso','López',age = '26', favorite_color='Negro',hobbies='Jugar')

print(user_profile)