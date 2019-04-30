def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
#print(user_profile)



def build_profile_yo(nombre, apellido, **info):
    perfil = {}
    perfil['Nombres'] = nombre
    perfil['Apellidos'] = apellido
    for key, value in info.items():
        perfil[key] = value
    return perfil
info = build_profile_yo('Luis Alberto', 'Ornelas Hinojosa', Escuela='UAdeC', Altura=1.85, Edad=21)
print(info)