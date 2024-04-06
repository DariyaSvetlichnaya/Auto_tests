import sqlite3

sqllite_create_db = """
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    supplier_id INTEGER,
    category_id INTEGER,
    price INTEGER
);
"""

if __name__ == '__main__':

    conn = sqlite3.connect(database='products_db.db')
    cursor = conn.cursor()
    cursor.execute(sqllite_create_db)
    cursor.execute('insert into Products values (1, "Chais", 1, 1, 18)')
    conn.commit()
    print(cursor.execute('select * from Products').fetchall())
    cursor.close()
    conn.close()