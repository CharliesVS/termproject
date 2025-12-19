import random

    

words = {
    "Movies": ["Inception", "Transformers", "Avatar", "TRON" "Legacy", "Interstellar", "The Dark Knight", "Pulp Fiction", "The Matrix", "Gladiator", "Jurassic Park", 
               "Star Wars", "Avengers: Infinity War", "Spiderman: Into the Spider-Verse", "Ghost in the Shell", "Bumblebee", "Back to the Future", "The Batman" "Superman" "Aquaman", "Dune", "Top Gun: Maverick", 
               "John Wick", "Mission Impossible: Fallout", "The Thing (1982)", "Chronicle", "The Hurt Locker", "Sonic the Hedgehog", "Spiderman 2", "Guardians of the Galaxy", "Deadpool", 
               "Edge of Tomorrow", "Baby Driver", "Pacific Rim", "Good Will Hunting", "Whiplash", "21 Jump Street", "Skyfall", "Hellraiser (2022)" "Alien: Romulus" "Halloween (1978)",
               "Saw" "Die Hard With a Vengeance" "Bad Boys" "Ford v Ferrari" "Shrek", "The Incredibles", "Big Hero 6", "Cars", "Wall E", "Toy Story", "Puss in Boots"],
    
    "Video Games": ["The Legend of Zelda", "Minecraft", "Valorant", "Portal", "CS:GO", "Fortnite", "Overwatch 2", "Battlefield 1", "Spiderman", "skate", "Star Wars: Jedi Fallen Order", "Marvel Rivals", 
                    "Risk of Rain 2", "Stardew Valley", "Alien: Isolation", "Titanfall 2", "Terraria", "Five Nights at Freddys", "Subnautica", "Elden Ring", "Dead Space", "Call of Duty: Modern Warfare (2019)",
                    "Until Dawn", "Tomb Raider", "Forza Horizon 4", "Payday 2", "Hollow Knight", "Mirrors Edge", "Star Wars: Battlefront 2", "Ghost of Tsushima", "God of War", "Mortal Kombat 1", 
                    "Tom Clancys Rainbow 6 Seige", "Rocket League", "Roblox", "Party Animals", "GTA 5"],
    
    "Anime": ["Jujutsu Kaisen", "Attack on Titan", "My Hero Academia", "Bleach", "Soul Eater", "Neon Genesis Evangelion", "Gundam", "Mob Psycho 100", "DanDaDan", "Gachiakuta", "Fullmetal Alchemist: Brotherhood", 
              "Demon Slayer", "Naruto", "One Piece", "Dragon Ball Z" "Your Name", "Konosuba", "Chainsaw Man" "Trigun" "Samurai Champloo" "Cowboy Bebop" "Frieren: Beyond Journeys End", 
              "Yu Yu Hakusho", "Sailor Moon", "Akira", "Gintama", "Space Dandy", "The Melancholy of Haruhi Suzumiya", "Black Clover", "My Dress Up Darling"],
    
    "Music Artists": ["Between Friends", "Tyler, The Creator", "Paramore", "Twenty One Pilots", "THE DRIVER ERA", "Malcom Todd", "Troy Javelona", "MarQ", "Maroon 5", "Childish Gambino",
                      "Cafune", "Dua Lipa", "Charlie Puth", "The Weeknd", "Wallows", "spill tab", "BENEE", "Dominic Fike", "Billie Eilish", "Fall Out Boy", "Kendrick Lamar",],
    
    "Sports Athletes": ["Lebron James", "Zebb Powell", "Cristiano Ronaldo", "Lionel Messi", "Wayne Gretzky", "Tom Brady", "Tony Hawk", "Shawn White", "Steph Curry", "Novak Djokovic", 
                        "Michael Phelps", "Micheal Jordan", "LaMelo Ball", "Usain Bolt",]
}


def select_word_by_topic():
    print("Available topics: " + ", ".join(words.keys()))
    while True:
        topic = input("Choose a topic to play: ")
    
        if topic in words:
            return random.choice(words[topic])
        else:
            print("Invalid topic. Please try again.")


def display_hangman(incorrect_guesses):
    """Displays the hangman figure based on the number of incorrect guesses."""
    stages = [
        # Stage 0: No incorrect guesses
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        # Stage 1: Head
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        # Stage 2: Body
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        # Stage 3: One arm
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        # Stage 4: Both arms
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        # Stage 5: One leg
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        # Stage 6: Both legs (Game Over)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
    ]
    print(stages[incorrect_guesses])




def play_hangman():
    """Main function to run the Hangman game."""
    word = select_word_by_topic()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
   
    
    

    print("Welcome to Hangman!. You have 6 guesses, good luck!")
    display_hangman(incorrect_guesses)

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        if "_" not in display_word:
            print("\nCongratulations! You guessed the word!")
            break
        

        guess = input("Guess a letter: ").upper()


        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1
            display_hangman(incorrect_guesses)

    if incorrect_guesses == max_incorrect_guesses:
        print("\nGame Over! You ran out of guesses.")
        print(f"The word was: {word}")
        
        return 

if __name__ == "__main__":
    play_hangman()