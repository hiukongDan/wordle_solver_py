# Implement user interaction and game logic delegation
from controller import Controller
from word_maker import WordMaker
from guess_engine import GuessEngine, GuessStatus
from wordle_solver import WordleSolver
from message import *
import sys

class Wordle:
    def print_help(self):
        print(HELP_MSG)
        
    def print_exit(self):
        print(EXIT_MSG)
        
    def print_restart(self):
        print(RESTART_MSG)
    
    def __init__(self, wordLen=5):
        self.wordLen = wordLen
        self.wordMaker = WordMaker(wordLen)
        self.wordleSolver = WordleSolver(wordLen, self.wordMaker.get_words())
        self.controller = Controller(self, self.wordleSolver, self.wordMaker)
    
    def start(self):
        self.print_help()
        self.print_restart()
        self.gameloop()
    
    def gameloop(self):
        while(True):
            user_input = input(PROMPT)
            self.controller.process_input(user_input)
            
    def help(self):
        self.print_help()
        
    def exit(self):
        self.print_exit()
        sys.exit(0)
    
    def hint(self, suggestion_word):
        print("Hint suggestion: %s" % suggestion_word)
        
        
    def restart(self):
        self.wordleSolver.reset()
        self.print_restart()
