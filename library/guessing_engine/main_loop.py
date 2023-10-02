import sqlite3 as sqlite
import settings


class MagicDBInterface(object):
    """A custom class for executing SQLite queries on a local database of Magic cards """


    def __init__(self):
        
        try:
            self.db = sqlite.connect(settings.DB)
            self.card_selected : bool = False
            self.selected_card : str = None

        except:
            raise
        
    def select_random_creature_card(self):
        conn = sqlite.connect(settings.DB)
        select_statement = """SELECT name from creatures ORDER BY RANDOM() LIMIT 1;"""
        with conn:
            self.selected_card = conn.execute(select_statement).fetchone()[0]
        self.card_selected = True

    def __str__(self):
        return self.selected_card

if __name__ == "__main__":
    interface = MagicDBInterface()
    interface.select_random_creature_card()
    print(interface)
        


