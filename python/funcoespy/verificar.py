def verificar_aprovacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    return "Reprovado"

print(verificar_aprovacao(8, 7, 9))
print(verificar_aprovacao(5, 5, 6))
print(verificar_aprovacao(3, 4, 5))

