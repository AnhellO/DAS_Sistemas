try:

    file = 'Frankestein.txt'

    with open(file) as fo:
        lines = fo.readlines()

    count = 0
    
    for line in lines:
        count += line.lower().count('the')

    print(count)

except FileNotFoundError:
        print('File is missing')