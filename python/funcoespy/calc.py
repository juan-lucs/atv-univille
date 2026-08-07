def calculadora(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Divisão por zero"
        return num1 / num2
    return "Operação inválida"

print(calculadora(10, 2, "+"))
print(calculadora(10, 2, "/"))
print(calculadora(10, 0, "/"))
