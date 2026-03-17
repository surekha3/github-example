def func(n):
  for i in range(1, n+1):
    for j in range(n-i):
      print(" ", end="")
    print(i*"* ", end="")
    print()
n = int(input("enter natural number as user input: "))
func(n)
