def eh_palindromo(pal):
    if len(pal) <= 1 :
        return True

    if pal[0] != pal[-1]:
        return False

    return eh_palindromo(pal[1:-1])

print(eh_palindromo("aa"))