n = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(n))
print('É um número? ', n.isnumeric())
print('Só tem espaços? ', n.isspace())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('É caracteres ASCII? ', n.isascii())
print('É decimal? ', n.isdecimal())
print('É dígito? ', n.isdigit())
print('É em carecteres minúsculos? ', n.islower())
print('É imprimível? ', n.isprintable())
print('Todas as palavras em um texto começam com uma letra maiúscula? ', n.istitle())
print('É em carecteres maiúsculos? ', n.isupper())
