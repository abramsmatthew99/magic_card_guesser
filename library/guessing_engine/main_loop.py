from database_engine.database_interface import MagicDBInterface
from enum import Enum


#TODO: remember that apostrophes in column names and text fields should be escaped with a second apostrophe
#TODO: remember that assembly-worker is assembly_worker



class GuessingGame(object):
    """A class that initalizes and represents a game for guessing randomly queried Magic cards"""

    def __init__(self):
        self.interface : MagicDBInterface = MagicDBInterface()
        self.game_state = GameState.SELECTING_MODE.value
        self.selected_card : int = None #The ID of the selected card
        self.running : bool = False
        self.begin_game_loop()

    def begin_game_loop(self):
        """Constantly presents the menu until the game is no longer running. present_
        menu() prompts for input and so the game will not continue without player action"""
        self.running = True
        while self.running:
            self.present_menu()
    
    def present_menu(self):
        match self.game_state:
            case 1:
                self.present_guessing_options()
            case 2:
                self.present_card_pool_options()
            case 3:
                self.present_game_over_menu()
            case _: #The default case
                raise ValueError
    
    def present_card_pool_options(self):
        menu_dict = {1: {"message": "Guess a random card", 
                         "function":self.interface.select_random_card}}
        for key in menu_dict: #Print each option
            print(f'{key}. {menu_dict[key]["message"]}')
        #Get User Input
        chosen_option = 0
        while chosen_option not in menu_dict:
            try:
                chosen_option = int(input("Please enter the numer of the game mode to play: "))
            except:
                pass
        self.selected_card = menu_dict[chosen_option]["function"]()
        self.game_state = GameState.GUESSING.value

    def present_guessing_options(self):
        print(self.selected_card)
        exit()

class GameState(Enum):
        GUESSING = 1
        SELECTING_MODE = 2
        GAMEOVER = 3

if __name__ == "__main__":
    game = GuessingGame()
        


