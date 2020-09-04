a = int(input('Tal vez un número: '))
print('El número es... ' + str(~((a & 0x04 | 8) << 4) ^ 0xFF01))