# Implement delegate user input to game logic facility
from word_maker import WordMaker
from guess_engine import GuessEngine, GuessStatus
from input_processor import InputProcessor, InputType

class Controller:
    def __init__(self, wordle, wordleSolver, wordMaker):
        self.inputProcessor = InputProcessor()
        self.wordle = wordle
        self.wordleSolver = wordleSolver
        self.wordMaker = wordMaker
        
    def process_input(self, input):
        input = input.strip().lower()
        type = self.inputProcessor.process_input(input)
        if type == InputType.INVALID:
            print("invalid input: %s" % input)
        elif type == InputType.GUESS:
            data = input.split()
            word = data[0]
            res = data[1]
            
            if len(word) != self.wordMaker.get_wordLen() or \
            len(res) != self.wordMaker.get_wordLen():
                print("invalid input: %s" % input)
                return
            
            res = GuessEngine.parseResult(res)
            self.wordleSolver.record_guess(word, res)
            # update suggestion on gui
            suggestion_word = self.wordleSolver.next_suggestion()
            self.wordle.hint(suggestion_word)
        elif type == InputType.COMMAND_HELP:
            self.wordle.help()
        elif type == InputType.COMMAND_EXIT:
            self.wordle.exit()
        elif type == InputType.COMMAND_HINT:
            suggestion_word = self.wordleSolver.next_suggestion()
            self.wordle.hint(suggestion_word)
        elif type == InputType.COMMAND_RESTART:
            # do restart
            self.wordle.restart()