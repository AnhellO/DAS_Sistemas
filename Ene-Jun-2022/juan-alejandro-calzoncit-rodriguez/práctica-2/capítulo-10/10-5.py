file_name = 'reasons.txt'

x = 0
while x < 5:
    reason = input('Hi!, why do you like programming? : ')    

    if reason:

        with open(file_name, 'a') as file_object:
            file_object.write(reason + '\n')

        x += 1