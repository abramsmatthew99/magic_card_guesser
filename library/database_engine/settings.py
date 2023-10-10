#Just a file of constant values related to the local database and the JSON format of scryfall cards
DB = r"assets\Database\magic_cards.db"
CREATURE_TABLE = "creatures"
CARD_TABLE = "cards"

JSON_TO_CARD_COL_NAMES = {"id": "id", "card_back_id": "card_back_id", "name": "name", "colors": "colors", 
                     "color_identity": "clr_id", "mana_cost": "mana_cost", "cmc": "cmc", "type_line": "type_line",
                     "oracle_text": "rules_text", "keywords": "keywords", "flavor_text": "flavor", 
                     "released_at": "released", "rarity": "rarity", "collector_number": "coll_no",
                     "set": "set_abbr", "set_name": "set_name"}


