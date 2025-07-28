
while True:
 a=str(input("start(y/n):").lower())
 if(a!="y"):
   break
 import random as r
 comp=['Rock','Paper','Scissors']
 player=input("Enter:Rock,Paper or Scissor:").capitalize()
 matrix=[
    ['Draw','Victory','Defeat'],
    ['Defeat','Draw','Victory'],
    ['Victory','Defeat','Draw']
 ]
 if player not in comp:
    print("Invalid Input")
 else:
    c=r.choice(comp)
    print(f'Computer Selected:{c}')
    m=comp.index(c)
    p=comp.index(player)
    r=matrix[m][p]
    print(r)