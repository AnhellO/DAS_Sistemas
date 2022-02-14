# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *


import printing_sandwiches
from printing_sandwiches import make_sandwich
from printing_sandwiches import make_sandwich as ms
import printing_sandwiches as ps
from printing_sandwiches import *

make_sandwich("Jam", "Cheese slice", "Mayonnaise")
make_sandwich("Jam", "Extra Cheese slice", "Mayonnaise", "Mustard",)
make_sandwich("Jam", "Mayonnaise", "Mustard", "Lettuce", "Tomatoe")
# Making a sandwich with the following toppings:
# - Jam
# - Cheese slice
# - Mayonnaise

# Making a sandwich with the following toppings:
# - Jam
# - Extra Cheese slice
# - Mayonnaise
# - Mustard

# Making a sandwich with the following toppings:
# - Jam
# - Mayonnaise
# - Mustard
# - Lettuce
# - Tomatoe
