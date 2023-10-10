import sqlite3 as sqlite
import settings
import json

class MagicDBInterface(object):
    """A custom class for executing SQLite queries on a local database of Magic cards """

    def __init__(self):
        
        try:
            self.db = sqlite.connect(settings.DB)

        except:
            raise
        
        
    def select_random_card(self):
        conn = sqlite.connect(settings.DB)
        select_statement = f"SELECT id from {settings.CARD_TABLE} ORDER BY RANDOM() LIMIT 1;"
        with (conn):
            return conn.execute(select_statement).fetchone()

    def add_card_to_db(self, card_dict):
        """Takes a given JSON dict from scryfall and populates the proper tables"""
        card_table_statement = """INSERT INTO cards """
        col_substatement = "("
        val_substatement = "VALUES ("
        values = []
        if "creature" in card_dict["type_line"]: #Check if this bad boy is a creature
            self.add_creature_info(card_dict)
        self.add_legalities(card_dict)
        for key in card_dict:
            if key not in settings.JSON_TO_CARD_COL_NAMES:
                continue
            col_substatement += f"{settings.JSON_TO_CARD_COL_NAMES[key]}, "
            val_substatement += "?, "
            if isinstance(card_dict[key], list):
                values.append("".join(card_dict[key]))
            else:
                values.append(card_dict[key])

        #Remove the final comma and space
        col_substatement = col_substatement[:-2] + ")"
        val_substatement = val_substatement[:-2] + ");"
        card_table_statement += col_substatement + val_substatement
        self.db.execute(card_table_statement, values)
        self.db.commit()

    
    def add_creature_info(self, card_dict):
        sql_stmt = "INSERT INTO creatures "
        col_statement = "("
        

    def add_legalities(self, card_dict):
        pass

    def add_cards_in_bulk(self, card_data_list):
        for card in card_data_list:
            self.add_card_to_db(card)
        


if __name__ == "__main__":
    interface = MagicDBInterface()
    with open("assets\JSON Files\oracle-cards-20231009210206.json", 'r', encoding='utf8') as f:
        card_list = json.load(f)
    interface.add_cards_in_bulk(card_list)
    