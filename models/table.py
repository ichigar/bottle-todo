import sqlite3
from abc import ABC
 
class Table(ABC):
    def __init__(self, db_name, table_name):
        self._table_name = table_name
        self._db_name = db_name

    def _connect(self):
        conn = sqlite3.connect(self._db_name)
        return conn
    
    def insert(self, data):
        data_keys = list(data.keys())
        data_values = list(data.values())
        
        query = f"INSERT INTO {self._table_name} ({', '.join(data_keys)}) VALUES ({', '.join(['?'] * len(data_values))})"
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, data_values)
            conn.commit()
        except Exception as e:
            print(e)
            return False
        finally:
            if conn:
                conn.close()
            return True
        
    def select(self):
        rows = None
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table_name}")
            rows = cursor.fetchall()
            conn.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()
            return rows
    
    def update(self, data, where):
        data_keys = list(data.keys())
        data_values = list(data.values())
        where_key = list(where.keys())[0] 
        query = f"UPDATE {self._table_name} SET {', '.join([f'{key} = ?' for key in data_keys])} WHERE {where_key} LIKE ?"
        
        values = data_values + [where[where_key]]
        values = tuple(values)        
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()
            return True
        
    def delete(self, where):
        clave = list(where.keys())[0] 
        value = where[clave]
        where_clause = f"{clave} LIKE ?"
        query = f"DELETE FROM {self._table_name} WHERE {where_clause}"
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, (value,))
            conn.commit()
            conn.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()
            return True
        
    def get_field(self, field, where):
        clave = list(where.keys())[0] 
        value = where[clave]
        where_clause = f"{clave} LIKE ?"
        query = f"SELECT {field} FROM {self._table_name} WHERE {where_clause}"
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, (value,))
            data = cursor.fetchone()
            conn.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()
            return data
        
    def update_field(self, field, value, where):
        clave = list(where.keys())[0] 
        where_value = where[clave]
        where_clause = f"{clave} LIKE ?"
        query = f"UPDATE {self._table_name} SET {field} = ? WHERE {where_clause}"
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, (value, where_value))
            conn.commit()
            conn.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()
            return True