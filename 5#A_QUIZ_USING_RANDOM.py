#Addition quiz for a first grader using random module

import random

ans='Y'

while ans=='Y':

      x=random.randint(1,100)
      y=random.randint(1,100)

      print('What is' ,x ,'+',y,'?')
      
      ans=int(input('Your answer:'))
      if ans== (x+y):
            print('you got the correct answer!!')
      else:
          print('Please try again..')

      ans=input('Do you wanna play again(Y/N)?')
      ans=ans.capitalize()
      print('\n')

