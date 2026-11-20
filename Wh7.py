import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")
conn.commit()


def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()
    print(f"Товар '{name}' успешно добавлен.")


def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print("\n--- Список товаров ---")
    for product in products:
        print(f"ID: {product[0]} | Название: {product[1]} | Цена: {product[2]} | Количество: {product[3]}")
    print("----------------------\n")


def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    conn.commit()
    print(f"Цена товара с ID {id} обновлена на {price}.")


def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    conn.commit()
    print(f"Товар с ID {id} удалён.")


if __name__ == "__main__":
    create_product("Ноутбук", 75000.0, 5)
    create_product("Мышка", 1500.0, 20)
    create_product("Клавиатура", 3500.0, 12)

    read_products()

    update_product(1, 72000.0)
    read_products()

    delete_product(2)
    read_products()

    conn.close()
