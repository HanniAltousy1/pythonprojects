def main():
  num1 = float(input("Enter the first number: "))

  num2 = float(input("Enter the second number: "))

  op = input("Enter the operation (+, -, *, /): ")

  if op == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
  elif op == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
  elif op == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
  elif op == "/":
    result = num1 / num2
    print(num1, "/", num2, "=", result)

main()