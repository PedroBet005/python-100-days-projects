import random

# TODO-1: - Actualizar la lista de palabras para usar 'word_list' desde hangman_words.py
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

# TODO-3: - Importar el logo desde hangman_art.py e imprimirlo al inicio del juego.
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Actualizar el código para decirle al usuario cuántas vidas le quedan.
    print(
        f"****************************{lives}/6 LIVES LEFT****************************"
    )
    guess = input("Guess a letter: ").lower()

    # TODO-4: - Si el usuario ha ingresado una letra que ya adivinó,
    # imprimir la letra y avisarle.

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - Si la letra no está en chosen_word, imprimir la letra
    # y avisar que no está en la palabra.
    # Ej: Adivinaste d, no está en la palabra. Pierdes una vida.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            # TODO-7: - Actualizar el print para mostrar la palabra correcta
            # que el usuario estaba intentando adivinar.
            print(
                f"***********************IT WAS {chosen_word}! YOU LOSE**********************"
            )

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Actualizar el código para usar la lista stages
    # desde el archivo hangman_art.py
    print(stages[lives])
