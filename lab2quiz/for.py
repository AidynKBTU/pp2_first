#1 example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2 example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#3 example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#4 example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#5 example
for x in range(6):
  print(x)  