
import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("what do you chose ? 0 for rock,1 for paper,2 for scissors")
l=[rock,paper,scissors]
k=int(input())
print(l[k])

print("Computer choice")
num=r.randint(0,len(l)-1)

print(l[num])

if k==num:
    print("It is a tie!")
elif k>=3 or k<0:
    print("you choice invalid number you lose")
elif k==0 and num==2:
    print("you win")
elif num==0 and k==2:
    print("you lose")
elif num > k:
    print("you lose")
elif k > num:
    print("you win")

