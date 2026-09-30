users = {
    "ivan": {
        "password": "1234",
        "grades": [12, 10, 8, 11, 5, 4, 9]
    },
    "anna": {
        "password": "qwerty",
        "grades": [7, 9, 12, 6, 10, 3, 8]
    },
    "petro": {
        "password": "1111",
        "grades": [4, 5, 6, 8, 2, 10, 12]
    },
    "olena": {
        "password": "abcd",
        "grades": [11, 12, 9, 10, 7, 1, 5]
    }
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

# Перевірка логіна та пароля
if login in users and users[login]["password"] == password:
    grades = users[login]["grades"]

    print("\nВхід успішний!")
    print("Ваші оцінки:", grades)

    # Підрахунок оцінок
    satisfactory = sum(5 <= grade <= 12 for grade in grades)
    unsatisfactory = sum(1 <= grade <= 4 for grade in grades)

    print("Кількість задовільних оцінок (5-12):", satisfactory)
    print("Кількість незадовільних оцінок (1-4):", unsatisfactory)

else:
    print("\nПомилка: неправильний логін або пароль.")