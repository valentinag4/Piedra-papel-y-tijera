#proyecto piedra papel o tijera
import random

contador = 0

punto_bot = 0
punto_user = 0

bot = ['piedra', 'papel', 'tijera']

while (contador <= 2):

  num = random.randint(0, 2)
  print(bot[num])

  User_input = input("ingrese piedra papel o tijera: ")

  if (bot[num] == User_input):
    print(User_input, bot[num], "empate")

  elif ((bot[num] == 'papel' and User_input == 'piedra')
        or (bot[num] == 'piedra' and User_input == 'tijera')
        or (bot[num] == 'tijera' and User_input == 'papel')):
    punto_bot += 1
    contador+=1
          

    print(User_input, bot[num], "PERDISTE usuario")

  elif ((bot[num] == 'piedra' and User_input == 'papel')
        or (bot[num] == 'tijera' and User_input == 'piedra')
        or (bot[num] == 'papel' and User_input == 'tijera')):
    punto_user += 1
    contador+=1

    print(User_input, bot[num], "PERDISTE bot")

  else:
    print("ganaste ")
    print(User_input, bot[num])

  
  print(punto_user, "usuario")
  print(punto_bot, "bot")
