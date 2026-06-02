import random

# ==============================
# HANGMAN STAGES
# ==============================

HANGMAN_PICS = [
'''
 +---+
 |   |
     |
     |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
'''
]

# ==============================
# WORD CATEGORIES
# ==============================

categories = {

    "Technology": {
        "easy": [
            "mouse", "phone", "cable",
            "screen", "keyboard"
        ],

        "medium": [
            "python", "laptop",
            "network", "coding"
        ],

        "hard": [
            "algorithm",
            "database",
            "cybersecurity",
            "automation"
        ]
    },

    "Animals": {

        "easy": [
            "cat", "dog", "lion",
            "tiger", "bear"
        ],

        "medium": [
            "elephant",
            "giraffe",
            "monkey"
        ],

        "hard": [
            "chimpanzee",
            "hippopotamus",
            "crocodile"
        ]
    },

    "Sports": {

        "easy": [
            "bat", "ball",
            "goal", "run"
        ],

        "medium": [
            "cricket",
            "football",
            "hockey"
        ],

        "hard": [
            "badminton",
            "volleyball",
            "basketball"
        ]
    },

    "Science": {

        "easy": [
            "atom",
            "cell",
            "force"
        ],

        "medium": [
            "energy",
            "gravity",
            "motion"
        ],

        "hard": [
            "photosynthesis",
            "thermodynamics",
            "electricity"
        ]
    }
}

# ==============================
# HINTS
# ==============================

hints = {

    "python": "Programming Language",

    "database": "Stores Information",

    "football": "World Famous Sport",

    "lion": "King of Jungle",

    "gravity": "Force of Attraction",

    "algorithm": "Step by Step Solution"
}

# ==============================
# GLOBAL VARIABLES
# ==============================

leaderboard = []

games_played = 0
wins = 0
losses = 0

player_profile = {

    "name": "",
    "games_played": 0,
    "wins": 0,
    "losses": 0,
    "highest_score": 0
}
# ==============================
# RULES
# ==============================

def show_rules():

    print("\n" + "=" * 50)
    print("RULES")
    print("=" * 50)

    print("1. Guess one letter at a time")
    print("2. Wrong guesses reduce attempts")
    print("3. Hint can be used only once")
    print("4. Correct guess = +10 points")
    print("5. Wrong guess = -2 points")
    print("6. Hint use = -5 points")


# ==============================
# LEADERBOARD
# ==============================

def show_leaderboard():

    if len(leaderboard) == 0:
        print("\nNo Records Found")
        return

    print("\n" + "=" * 70)

    print("{:<5} {:<20} {:<10} {:<10}".format(
        "Rank",
        "Player",
        "Score",
        "Result"
    ))

    print("=" * 70)

    sorted_board = sorted(
        leaderboard,
        key=lambda x: x["score"],
        reverse=True
    )

    for i, row in enumerate(sorted_board, start=1):

        print("{:<5} {:<20} {:<10} {:<10}".format(
            i,
            row["name"],
            row["score"],
            row["result"]
        ))

    print("=" * 70)


# ==============================
# STATISTICS
# ==============================

def show_statistics():

    print("\nSTATISTICS")

    print("Games Played :", games_played)
    print("Wins         :", wins)
    print("Losses       :", losses)

    if games_played > 0:

        rate = (wins / games_played) * 100

        print("Win Rate     :", round(rate, 2), "%")


# ==============================
# PROFILE
# ==============================

def show_profile():

    print("\nPLAYER PROFILE")

    print("-" * 40)

    print("Name :", player_profile["name"])

    print("Games Played :",
          player_profile["games_played"])

    print("Wins :",
          player_profile["wins"])

    print("Losses :",
          player_profile["losses"])

    print("Highest Score :",
          player_profile["highest_score"])


# ==============================
# ACHIEVEMENTS
# ==============================

def achievement(score):

    if score >= 100:
        return "🏆 Expert"

    elif score >= 50:
        return "🥈 Intermediate"

    else:
        return "🥉 Beginner"


# ==============================
# PROJECT INFO
# ==============================

def project_info():

    print("\nPROJECT INFORMATION")

    print("-" * 50)

    print("Project : Hangman Game")

    print("Language : Python")

    print("Developer : Nitin Rajawat")

    print("Features")

    print("1. Categories")

    print("2. Difficulty Levels")

    print("3. Hint System")

    print("4. Score System")

    print("5. Leaderboard")

    print("6. Statistics")

    print("7. Achievements")

# ==============================
# START GAME
# ==============================

def start_game():

    global games_played
    global wins
    global losses

    print("\nSTART GAME")

    player_name = input("Enter Your Name: ")

    player_profile["name"] = player_name

    print("\nCategories:")

    categories_list = list(categories.keys())

    for i, item in enumerate(categories_list, start=1):
        print(i, item)

    cat_choice = int(input("Select Category: "))

    selected_category = categories_list[cat_choice - 1]

    print("\nDifficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    level_choice = input("Enter Choice: ")

    if level_choice == "1":
        level = "easy"
        max_attempts = 8

    elif level_choice == "2":
        level = "medium"
        max_attempts = 6

    else:
        level = "hard"
        max_attempts = 5

    word = random.choice(
        categories[selected_category][level]
    )

    guessed = []
    wrong = 0
    score = 0

    while wrong < max_attempts:

        print("\nWord: ", end="")

        display = ""

        for letter in word:

            if letter in guessed:
                display += letter + " "

            else:
                display += "_ "

        print(display)

        # Win when all unique letters in the word are guessed
        if all(ch in guessed for ch in set(word)):

            print("\n🎉 YOU WIN!")
            print("Word:", word)
            print("Score:", score)

            wins += 1
            games_played += 1

            leaderboard.append({
                "name": player_name,
                "score": score,
                "result": "Win"
            })

            return

        guess = input(
            "Enter Letter: "
        ).lower()

        if len(guess) != 1:

            print("Enter only one letter")
            continue

        if guess in guessed:

            print("Already guessed")
            continue

        guessed.append(guess)

        if guess in word:

            print("Correct")
            score += 10

        else:

            print("Wrong")
            wrong += 1
            score -= 2

    print("\n💀 GAME OVER")
    print("Correct Word:", word)

    losses += 1
    games_played += 1

    leaderboard.append({
        "name": player_name,
        "score": score,
        "result": "Loss"
    })

while True:

    print("\n" + "=" * 50)
    print("HANGMAN GAME")
    print("=" * 50)

    print("1 Start Game")
    print("2 Rules")
    print("3 Leaderboard")
    print("4 Statistics")
    print("5 Profile")
    print("6 Project Info")
    print("7 Exit")

    choice = input(
        "Enter Choice: "
    )

    if choice == "1":

        start_game()

    elif choice == "2":

        show_rules()

    elif choice == "3":

        show_leaderboard()

    elif choice == "4":

        show_statistics()

    elif choice == "5":

        show_profile()

    elif choice == "6":

        project_info()

    elif choice == "7":

        print("Thanks For Playing")

        break

    else:

        print("Invalid Choice")