def func(n):
  for i in range(1, n+1):
    for j in range(n-i):
      print(" ", end="")
    print(i*"* ", end="")
    print()
user_input = input("enter natural number as user input: ")
if user_input == "":
  n = 5
else:
  try:
    n = int(user_input)
  except ValueError:
    print("Invalid input! Using default value as 5")
    n = 5
func(n)
