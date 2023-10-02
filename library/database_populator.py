import sqlite3 as sqlite

def create_connection(db_file):
    try:
        conn = sqlite.connect(db_file)
        print("Connected")
        return conn
    except sqlite.Error as e:
        print(e)
    
def execute_sql(conn: sqlite.Connection, sql_statement: str):
    try: 
        c = conn.cursor()
        c.execute(sql_statement)
    except sqlite.Error as e:
        print(e)

def main():
    database = r"assets\Database\magic_cards.db"

    sql_create_creature_table = """CREATE TABLE IF NOT EXISTS creatures (
        name text PRIMARY KEY, 
        type_line text NOT NULL, 
        mana_cost text NOT NULL, 
        cmc int NOT_NULL, 
        colors text, 
        color_id text, 
        set_abbr text, 
        set_name text, 
        power text NOT NULL, 
        toughness text NOT NULL,
        rules_text text, 
        flavor_text text, 
        rarity text,
        released text
    );"""

    conn = create_connection(database)
    if conn is not None:
        execute_sql(conn, sql_create_creature_table)

if __name__ == "__main__":
    main()