from enum import Enum

class InputType(Enum):
    GUESS           = 1
    COMMAND_HELP    = 2
    COMMAND_EXIT    = 3
    COMMAND_HINT    = 4
    COMMAND_RESTART = 5
    INVALID         = 8
    


class InputProcessor:
    """
    Actually this is an input syntax varifier
    """

    def __init__(self):
        pass
    
    def process_input(self, input):
        if len(input) == 0: return InputType.INVALID
        if input[0] == '/': return self.process_command(input[1:])
        else: return self.process_guess(input)
        
    def process_command(self, cmd):
        if (cmd == "help"): return InputType.COMMAND_HELP
        if (cmd == "exit"): return InputType.COMMAND_EXIT
        if (cmd == "hint"): return InputType.COMMAND_HINT
        if (cmd == "restart"): return InputType.COMMAND_RESTART
        
        return InputType.INVALID
        
        
    def process_guess(self, input):
        guesses = input.strip().split()
        if (len(guesses) != 2): return InputType.INVALID
        word = guesses[0]
        result = guesses[1]
        if not word.isalpha(): return InputType.INVALID
        for c in result:
            if c not in ['v', 'x', '?']: return InputType.INVALID
        
        return InputType.GUESS
    
    