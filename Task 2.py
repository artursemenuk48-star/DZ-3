class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} — {self.price:.2f} грн (На складі: {self.stock} шт.)"


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if quantity <= 0:
            print("Помилка: Кількість має бути більшою за нуль.")
            return

        if product.stock < quantity:
            print(f"Помилка: Недостатньо товару '{product.name}' на складі.")
            return

        if product in self.items:
            self.items[product] += quantity

        if product not in self.items:
            self.items[product] = quantity

        product.stock -= quantity
        print(f"Додано до кошика: {product.name} ({quantity} шт.)")

    def remove_product(self, product, quantity):
        if product not in self.items:
            print(f"Помилка: Товар '{product.name}' відсутній у кошику.")
            return

        if quantity <= 0:
            print("Помилка: Кількість для видалення має бути більшою за нуль.")
            return

        if self.items[product] <= quantity:
            actual_qty = self.items[product]
            del self.items[product]
            product.stock += actual_qty
            print(f"Повністю видалено з кошика: {product.name}")
            return

        self.items[product] -= quantity
        product.stock += quantity
        print(f"Зменшено кількість товару '{product.name}' у кошику на {quantity} шт.")

    def calculate_total(self):
        total = 0.0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def show_cart(self):
        print("--- Вміст кошика ---")
        for product, quantity in self.items.items():
            print(f"{product.name} — {quantity} шт. по {product.price:.2f} грн")
        print(f"Загальна вартість: {self.calculate_total():.2f} грн")


if __name__ == "__main__":
    p1 = Product("Смартфон", 12500.0, 10)
    p2 = Product("Навушники", 1800.0, 15)
    p3 = Product("Чохол", 350.0, 30)

    cart = Cart()

    cart.add_product(p1, 1)
    cart.add_product(p2, 2)
    cart.add_product(p3, 3)

    cart.show_cart()

    cart.remove_product(p2, 1)
    cart.show_cart()

    print("Залишок товару на складі після покупок:")
    print(p1)
    print(p2)
    print(p3)