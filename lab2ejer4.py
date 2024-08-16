def count_uppercase_letters():
    while True:
        user_input = input("Ingrese una cadena: ")
        if user_input:
            break
    uppercase_count = 0
    for char in user_input:
        if char.isupper():
            uppercase_count += 1
    print(f"La cadena tiene {uppercase_count} mayúsculas.")

count_uppercase_letters()

    