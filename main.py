from colorama import Fore as color 
import os, requests, json, asyncio, random, string
#########################################
print(color.YELLOW + "TKN Gen - Discord Authorization Generator | By github.com/pacity")
quantity = input(color.RESET + "How many tokens do you want to generate? ")
q = str(quantity)
while int(quantity) >= 0:
  p1 = str("OD")
  x = 0
  while x <= 23:
    r = random.randint(1, 2)
    f = open(".temp", "a")
    if r == 1:
      f.write(random.choice(string.ascii_letters))
    elif r == 2:
      f.write(str(random.randint(0, 9)))
    x = int(x) + 1
  f = open(".temp", "r")
  p2 = f.read()
  os.remove(".temp")
  tkn1 = f"{p1}{p2}."
  x = 0
  while x <= 7:
    r = random.randint(1, 2)
    f = open(".temp", "a")
    if r == 1:
      f.write(random.choice(string.ascii_letters))
    elif r == 2:
      f.write(str(random.randint(0, 9)))
    x = int(x) + 1
  f = open(".temp", "r")
  p2 = f.read()
  os.remove(".temp")
  x = 0
  while x <= 16:
    r = random.randint(1, 2)
    f = open(".temp", "a")
    if r == 1:
      f.write(random.choice(string.ascii_letters))
    elif r == 2:
      f.write(str(random.randint(0, 9)))
    x = int(x) + 1
  f = open(".temp", "r")
  p3 = f.read()
  os.remove(".temp")
  x = 0
  while x <= 11:
    r = random.randint(1, 2)
    f = open(".temp", "a")
    if r == 1:
      f.write(random.choice(string.ascii_letters))
    elif r == 2:
      f.write(str(random.randint(0, 9)))
    x = int(x) + 1
  f = open(".temp", "r")
  p4 = f.read()
  os.remove(".temp")
  tkn2 = f"{tkn1}{p2}.{p3}-{p4}"
  print(str(tkn2))
  quantity = int(quantity) - 1
print(color.GREEN + f"Successfully generated {q} tokens!")
