import sqlite3 as sqlite
import json
from library import settings

def create_connection(db_file):
    try:
        conn = sqlite.connect(db_file)
        print("Connected")
        return conn
    except sqlite.Error as e:
        print(e)
    
def create_table_sql(conn: sqlite.Connection, sql_statement: str):
    try: 
        c = conn.cursor()
        c.execute(sql_statement)
    except sqlite.Error as e:
        print(e)

def add_creature_sql(conn: sqlite.Connection, creature: tuple):
    sql = """INSERT INTO creatures(name,type_line, mana_cost, cmc, colors, color_id, set_abbr, set_name, power,"""\
    """toughness, rules_text, rarity, released, flavor_text)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    try:
        c = conn.cursor()
        c.execute(sql, creature)
        conn.commit()
    except sqlite.IntegrityError:
        return

def create_creature_tuple_from_json_entry(conn, entry):
    """Take the JSON data of a Magic creature card from Scryfall's format and populates the local database with this creature"""
    try:

        flavor_text = entry['flavor_text'] if 'flavor_text' in entry else ""
        oracle_text = entry['oracle_text'] if 'oracle_text' in entry else ""
        add_creature_sql(conn, (entry['name'], entry['type_line'], entry['mana_cost'], entry['cmc'], ",".join(entry['colors']), 
            ",".join(entry['color_identity']), entry['set'], entry['set_name'], entry['power'], entry['toughness'],
            oracle_text, entry['rarity'], entry['released_at'], flavor_text))
    except KeyError as e:
        print(e)
        raise
    
def parse_creatures(conn, contents):
    for card in contents:
        if "power" in card:
            create_creature_tuple_from_json_entry(conn, card)




def main():

    conn = create_connection(settings.DB)
    if conn is not None:
        with open("assets\JSON Files\oracle-cards-20231001210221.json", 'r', encoding='utf8') as f:
            contents = json.loads(f.read())
            parse_creatures(conn, contents)

if __name__ == "__main__":
    main()
    
        