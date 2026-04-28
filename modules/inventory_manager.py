#Coded by @nmurthydev 

# inventory_manager.py
# modules/inventory_manager.py
import sqlite3
from datetime import datetime

DB_NAME = "inventory.db"

class InventoryManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            quantity INTEGER,
            price REAL,
            category TEXT,
            last_update TEXT,
            sold INTEGER DEFAULT 0
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_item(self, name, quantity, price, category):
        query = """INSERT INTO inventory (name, quantity, price, category, last_update)
                   VALUES (?, ?, ?, ?, ?)"""
        self.conn.execute(query, (name, quantity, price, category, datetime.now()))
        self.conn.commit()
        return True

    def update_item(self, item_id, name, quantity, price, category):
        query = """UPDATE inventory
                   SET name=?, quantity=?, price=?, category=?, last_update=?
                   WHERE id=?"""
        self.conn.execute(query, (name, quantity, price, category, datetime.now(), item_id))
        self.conn.commit()
        return True

    def delete_item(self, item_id):
        query = "DELETE FROM inventory WHERE id=?"
        self.conn.execute(query, (item_id,))
        self.conn.commit()
        return True

    def get_all_items(self):
        query = "SELECT * FROM inventory"
        rows = self.conn.execute(query).fetchall()
        return [list(row) for row in rows]

    def search_item(self, keyword):
        keyword = f"%{keyword}%"
        query = "SELECT * FROM inventory WHERE name LIKE ? OR category LIKE ?"
        rows = self.conn.execute(query, (keyword, keyword)).fetchall()
        return [list(row) for row in rows]

    def reset_inventory(self):
        self.conn.execute("DELETE FROM inventory")
        self.conn.commit()

    def record_sale(self, item_id, qty_sold):
        query = "SELECT quantity, sold FROM inventory WHERE id=?"
        row = self.conn.execute(query, (item_id,)).fetchone()
        if not row:
            return False

        new_qty = row[0] - qty_sold
        if new_qty < 0:
            return False

        new_sold = row[1] + qty_sold
        query = """UPDATE inventory 
                   SET quantity=?, sold=?, last_update=? 
                   WHERE id=?"""
        self.conn.execute(query, (new_qty, new_sold, datetime.now(), item_id))
        self.conn.commit()
        return True

    def low_stock_alerts(self, threshold=5):
        query = "SELECT * FROM inventory WHERE quantity <= ?"
        rows = self.conn.execute(query, (threshold,)).fetchall()
        return [list(row) for row in rows]
