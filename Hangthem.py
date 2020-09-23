HANGMANPICS = ['''
    +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

#Words 

# Add ASCII art to visualize lives left.
# The game state display is accompanied by an ASCII art depending on the lives left
# The art sequence is adapted to the starting value of the lives parameter (at least between 3 and 7) - this means that the loosing picture is always the same


def getArtForLives(lives):
  return HANGMANPICS[lives]
