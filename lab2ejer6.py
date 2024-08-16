def calculate_ages():
    current_year = int(input("Introduzca el año actual: "))

    people = []
    for i in range(3):
        name = input(f"Introduzaca el nombre de la persona {i+1}: ")
        birth_year = int(input(f"Introduzca el año de nacimiento {name}: "))
        people.append({"name": name, "birth_year": birth_year})  

    for person in people:
        age = current_year - person["birth_year"]
        print(f"{person['name']} will turn {age} years old this year.")

calculate_ages()