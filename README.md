# Solver utility for Wordle... in python

I was trying to make an auto quordle solver, ended up making a simplest game :)


## Usage

```
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
```


## Authors

- [@hiukongDan](https://www.github.com/hiukongDan)


## Acknowledgements

- [english-words-py](https://github.com/mwiens91/english-words-py) as game dictionary
- wordle game implementation from [nytimes](https://www.nytimes.com/games/wordle/index.html) as reference