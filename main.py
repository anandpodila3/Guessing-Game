import random

someWords = '''apple banana mango strawberry orange grape pineapple apricot 
lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split()
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    guessed = ['_' for _ in word]
    letterGuessed = []

    chances = len(word) + 2
    while chances > 0:
        print(' '.join(guessed))
        if '_' not in guessed:
            print('Congratulations, You won!')
            break
        
        try:
            guess = input('Enter a letter to guess: ').lower()
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Enter only a single letter")
        except ValueError as ve:
            print(ve)
            continue
        
        if guess in letterGuessed:
            print('You have already guessed that letter')
            continue
        
        letterGuessed.append(guess)
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            chances -= 1
            print(f'Wrong guess! You have {chances} chances left.')

    if chances <= 0:
        print('You lost! Try again..')
        print(f'The word was {word}')
