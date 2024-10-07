graus_fahrenheit = int(input('Digite a temperatura em Fahrenheit: '))  

graus_celsius = (graus_fahrenheit - 32) * (5/9)

print(f'{graus_fahrenheit} graus Fahrenheit são {graus_celsius:.0f} graus celsius')