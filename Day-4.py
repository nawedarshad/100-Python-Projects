import random
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

#Write your code below this line 👇
rps=[rock,paper,scissors]
input_number = input("What would you choose? 0 for rock, 1 for paper, 2 for scissors")
rand_no = random.randint(0,2)
input_number=int(input_number)
if input_number == 0 and rand_no == 2:
  print(f"YOU: \n{rps[input_number]}\nCPU: \n{rps[rand_no]}")
  print("You won")
elif input_number == 1 and rand_no == 0:
  print(f"YOU: \n{rps[input_number]}\nCPU: \n{rps[rand_no]}")
  print("You won")
elif input_number == 2 and rand_no == 1:
  print(f"YOU: \n{rps[input_number]}\nCPU: \n{rps[rand_no]}")
  print("You won")
elif input_number == rand_no:
  print(f"YOU: \n{rps[input_number]}\nCPU: \n{rps[rand_no]}")
  print("Draw")
else:
  print(f"YOU: \n{rps[input_number]}\nCPU: \n{rps[rand_no]}")
  print("You loose")
