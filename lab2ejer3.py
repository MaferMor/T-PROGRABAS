def filtrar_palabras(words, n):
    return [word for word in words if len(word) > n]

words = ["hello", "world", "abc", "def", "ghi"]
n = 3
print(filtrar_palabras(words, n))

