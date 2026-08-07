def classifica_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

print(classifica_idade(10))
print(classifica_idade(15))
print(classifica_idade(30))
print(classifica_idade(70))
