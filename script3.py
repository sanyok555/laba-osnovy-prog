class Product:
    def __init__(self, id, name, price, count):
        self.id = id
        self.name = name
        self.price = price
        self.count = count


products = [
    Product(1, "Хліб", 25.50, 10),
    Product(2, "Молоко", 38.00, 8),
    Product(3, "Шоколад", 55.99, 5),
    Product(4, "Сік", 42.50, 7)
]

cart = []


def show_products():
    print("\n--- КАТАЛОГ ---")

    for product in products:
        print(
            product.id,
            product.name,
            f"{product.price:.2f}грн",
            "Залишок:", product.count
        )


def add_to_cart():
    show_products()

    id = int(input("Введіть ID товару: "))
    count = int(input("Введіть кількість: "))

    product = None

    for p in products:
        if p.id == id:
            product = p
            break

    if product is None:
        print("Товар не знайдено.")
        return

    if count > product.count:
        print("Недостатньо товару.")
        return

    cart.append({
        "product": product,
        "count": count
    })

    print("Товар додано в кошик.")


def show_cart():
    print("\n--- КОШИК ---")

    if len(cart) == 0:
        print("Кошик порожній.")
        return

    total = 0

    for item in cart:
        product = item["product"]
        count = item["count"]

        price = product.price * count
        total += price

        print(
            product.name,
            "x", count,
            f"{price:.2f}грн"
        )

    print("Всього:", f"{total:.2f}грн")


def remove_from_cart():
    show_cart()

    if len(cart) == 0:
        return

    id = int(input("Введіть ID товару: "))

    for item in cart:
        if item["product"].id == id:
            cart.remove(item)
            print("Товар видалено.")
            return

    print("Товар не знайдено.")


def buy():
    if len(cart) == 0:
        print("Кошик порожній.")
        return

    total = 0

    for item in cart:
        product = item["product"]
        count = item["count"]

        product.count -= count
        total += product.price * count

    cart.clear()

    print("Покупка успішна!")
    print("Сума:", f"{total:.2f}грн")


def admin():
    login = input("Логін: ")
    password = input("Пароль: ")

    if login == "admin" and password == "1234":
        print("\n--- ЗАЛИШКИ ---")

        # lambda
        sorted_products = sorted(
            products,
            key=lambda product: product.count
        )

        for product in sorted_products:
            print(
                product.name,
                "-",
                product.count,
                "шт."
            )

    else:
        print("Неправильний логін або пароль.")


while True:
    print("\n===== МАГАЗИН =====")
    print("1. Переглянути каталог")
    print("2. Додати товар у кошик")
    print("3. Видалити товар з кошика")
    print("4. Переглянути кошик")
    print("5. Купити товари")
    print("6. Увійти як адміністратор")
    print("0. Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        remove_from_cart()

    elif choice == "4":
        show_cart()

    elif choice == "5":
        buy()

    elif choice == "6":
        admin()

    elif choice == "0":
        print("До побачення!")
        break

    else:
        print("Неправильний вибір.")