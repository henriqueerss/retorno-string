def caracteres_sem_par(texto):
    # Contar ocorrências de cada caractere
    contagem = {}
    for char in texto:
        contagem[char] = contagem.get(char, 0) + 1

    # Filtrar apenas os caracteres com contagem ímpar
    sem_par = [char for char, qtd in contagem.items() if qtd % 2 != 0]

    # Retorna resultado ou None
    return "".join(sem_par) if sem_par else None


# Exemplos de uso
print(caracteres_sem_par("aabcc"))              # b
print(caracteres_sem_par("aabbccaaffbbaacaa"))  # fc
print(caracteres_sem_par("aabbcc"))             # None
