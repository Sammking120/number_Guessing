from random import randint

"""
lower_num, higher_num =1, 10

random_number: int =randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num}.')


while True:
    try:
        user_guess:int = int(input('Guess: '))
    except ValueError as e:
        print('please enter a valid number.')
        continue

    if user_guess > random_number:
        print ('The number is lower')
    elif user_guess< random_number:
        print('The number is higher')
    else:
        print('You Guessed it Right!')
        break
"""
#Homework Implementing maximum tries on the project
def guessing_game():
   lower_num, higher_num =1, 50
   random_number = randint(lower_num,higher_num)
   guess= None
   max_tries=5
   tries =0

   while guess != random_number and tries < max_tries:
      try:
        guess = int(input(f"guess a number between {lower_num} and {higher_num}: "))
      except ValueError as e:
        print('Please Enter a Valid Number')
        continue

      
      if guess > random_number:
         print('The number is lower')
      elif guess < random_number:
         print('The Number is higher')
      tries +=1
   if guess == random_number:
      print('Congraturation! You guessed the Number')
   else:
      print(f'Sorry, you ran out of tries. The number was {random_number}')
        

guessing_game()     
