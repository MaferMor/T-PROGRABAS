def mas_larga(words):
    return max(words, key=len)

words = ["hola", "mundo", "python", "es", "maravilloso"]
print(mas_larga(words))