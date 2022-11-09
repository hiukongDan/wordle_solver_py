HELP_MSG = """
Hello! Welcome to WordleSolver!
Wordle is game in which you guess a word six times,
each time we give feedback about the correctness of
each letter in the word. You can guess with the knowledge
of previous feedback.
This utility helps you with solving wordle game in other
third party website or app. Good luck!\n

Usage:
    /help       -- to print this help message
    /exit       -- to exit the game
    /hint       -- to get next hint based on current guesses and results
    /restart    -- to empty wordle solver history stack
    <5 letters> <result> -- your guess and the result
        e.g. I have entered "world" in the game and the result is
             vvx??, so I type world vvx??
Result:
    v -- correct letter
    x -- not in this word
    ? -- in this word but not correct position
"""

EXIT_MSG = """
Goodbye! See you next time!!!
"""

RESTART_MSG = """
WordleSolver Clear History Stack!
"""

PROMPT = ">>> "