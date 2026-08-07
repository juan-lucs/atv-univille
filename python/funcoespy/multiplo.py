def eh_multiplo(a, b):
    if b == 0:
        return False
    return a % b == 0

print(eh_multiplo(10, 2))
print(eh_multiplo(10, 3))
