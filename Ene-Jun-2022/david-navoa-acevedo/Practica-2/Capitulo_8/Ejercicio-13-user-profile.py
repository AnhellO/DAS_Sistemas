
from multiprocessing import Value


def build_profile(first, last, **user_info):
    
    profile = {}
    profile['first name'] = first
    profile['last'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("David", "Navoa Acevedo",age='26', experience='phyton, java', leguages='spanish, english')
print(user_profile)