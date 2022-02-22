def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
    
    
user_profile = build_profile('albert', 'einstein', location='princeton',
field='physics')
my_profile = build_profile('James', 'Bond', location = 'London', field = 'Math')
print(user_profile)
print(my_profile)
