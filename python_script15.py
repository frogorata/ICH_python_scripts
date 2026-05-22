# --- 1:

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

result = [text.lower() for text in text_list if len(text.split()) == 1]
print("Обработанный список:", result)

# --- 2:

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

discount_percent = int(input("Введите скидку (в процентах): "))
discount = 1 - discount_percent / 100

for product in products:
    old_price = product[1]
    new_price = old_price * discount
    product.append(new_price)

print(f"{'Товар':<12} {'Старая цена':>12} {'Новая цена':>12}")

for name, old_price, new_price in products:
    print(f"{name:<12} {old_price:>10.2f}$ {new_price:>10.2f}$")
