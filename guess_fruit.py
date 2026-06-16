import random

def start_game():
    while True:
        fruits = [
            "apple",
            "banana",
            "orange",
            "grape",
            "strawberry",
            "watermelon",
            "lemon",
            "peach",
            "pear",
            "cherry",
            "mango",
            "kiwi",
            "plum",
            "coconut",
            "grapefruit",
            "raspberry",
            "blackberry",
            "blueberry",
            "pineapple",
            "melon",
        ]
        fruit = random.choice(fruits)
        lives = 6
        guessed_letters = []

        print("Welcome to this game!")
        print(f"The fruit has {len(fruit)} letters.")
        print("-" * 10)

        while lives > 0:
            display = ""
            for letter in fruit:
                if letter in guessed_letters:
                    display += letter + " "
                else:
                    display += "_ "
            
            print(f"Fruit name: {display}")

            if "_" not in display:
                print("Congratulations! You won!")
                print(f"Your lives: {lives}")
                break

            guess = input("Guess one letter: ").lower()

            
            if guess in guessed_letters:
                print("Guess another letter. This letter has already guessed")
                lives -= 1
            elif guess in fruit:
                print("Correct!")
                guessed_letters.append(guess)
            else:
                print("Wrong")
                guessed_letters.append(guess)
                lives -= 1

            if lives == 0:
                print("Ohhh! You lost!")
                print(f"The fruit was {fruit}")

        play_again = input("Play again? (y/n) ").lower()
        if play_again == "n":
            break
    

start_game()