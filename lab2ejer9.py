def contar_vocales():
   
    word = input("Ingresa una palabra: ").lower()
    

    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0


    for letter in word:
        if letter == 'a':
            a_count += 1
        elif letter == 'e':
            e_count += 1
        elif letter == 'i':
            i_count += 1
        elif letter == 'o':
            o_count += 1
        elif letter == 'u':
            u_count += 1


    print(f"La palabra '{word}' tiene:")
    print(f"- {a_count} letras 'a'")
    print(f"- {e_count} letras 'e'")
    print(f"- {i_count} letras 'i'")
    print(f"- {o_count} letras 'o'")
    print(f"- {u_count} letras 'u'")

contar_vocales()

    