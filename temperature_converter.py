tem=float(input('Enter temperature ='))
if tem < -150 or tem > 150:
  print('Invalid temperature, please enter a temperature between -150 and 150')
  tem=float(input('Enter temperature ='))
choice=input('Enter your choice: \n1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius \n')
if choice=='1':
  fahrenheit=(tem*9/5)+32
  print('Temperature in Fahrenheit =',fahrenheit)
if choice=='2':
  celsius=(tem-32)*5/9
  print('Temperature in Celsius =',celsius)



















# while tem < -273.15:
#     print('Invalid temperature, please enter a temperature above -273.15')
#     tem=float(input('Enter temperature ='))
# if;
