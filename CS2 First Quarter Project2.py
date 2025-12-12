# Random mod for the random choosing of questions.
import random

# Questions for each topic
spanish_questions = [
    ["Who established the first permanent Spanish settlement in Cebu in 1565?",
     ["A. Ferdinand Magellan", "B. Miguel López de Legazpi", "C. Andres de Urdaneta", "D. Diego Silang"], "B"],

    ["Which event in 1896 marked the beginning of the Philippine Revolution?",
     ["A. Cry of Balintawak", "B. Declaration of Independence", "C. Treaty of Tordesillas", "D. Battle of Manila Bay"],
     "A"],

    ["Who was executed on December 30, 1896?",
     ["A. Andres Bonifacio", "B. Emilio Aguinaldo", "C. Jose Rizal", "D. Apolinario Mabini"], "C"],

    ["What was the system granting Spaniards land and labor from natives called?",
     ["A. Encomienda", "B. Feudalism", "C. Zemstvo", "D. Padrino system"], "A"],

    ["Which movement included Rizal and Marcelo H. del Pilar?",
     ["A. Katipunan", "B. Propaganda Movement", "C. Hukbalahap", "D. Kilusang Bagong Lipunan"], "B"],

    ["Which Filipino priest was NOT part of the GOMBURZA trio executed in 1872?",
     ["A. Gomez", "B. Burgos", "C. Zamora", "D. Pelaez"], "D"],

    ["Which Filipino reformist founded the La Solidaridad and advocated peaceful reforms in Spain?",
     ["A. Marcelo H. del Pilar", "B. Graciano Lopez Jaena", "C. Jose Rizal", "D. Mariano Ponce"], "B"]
]

american_questions = [
    ["Which event ended Spanish rule and gave control to the U.S. in 1898?",
     ["A. Treaty of Paris", "B. Spanish Civil War", "C. Battle of Waterloo", "D. Boxer Rebellion"], "A"],

    ["Who was the first President of the Philippine Republic?",
     ["A. Jose P. Laurel", "B. Emilio Aguinaldo", "C. Manuel Quezon", "D. Sergio Osmeña"], "B"],

    ["Which education policy did Americans bring?",
     ["A. Free-market universities", "B. Public schools with English", "C. Expansion of Spanish colleges",
      "D. Military schools"], "B"],

    ["What 1935 political milestone created the Commonwealth?",
     ["A. Jones Act", "B. Tydings–McDuffie Act", "C. 1935 Constitution", "D. Bataan Proclamation"], "C"],

    ["Which naval battle ended Spanish naval power in the Pacific?",
     ["A. Midway", "B. Manila Bay", "C. Leyte Gulf", "D. Trafalgar"], "B"],

    ["Which American governor-general established the Philippine Assembly in 1907?",
     ["A. William Howard Taft", "B. Leonard Wood", "C. Francis Burton Harrison", "D. Dwight Davis"], "A"],

    ["Which program sent Filipino scholars to study in the US during the American period?",
     ["A. Pensionado Program", "B. Filipinization Program", "C. Commonwealth Scholarship", "D. OsRox Mission"], "A"]
]

japanese_questions = [
    ["When did Japan occupy Manila in WWII?",
     ["A. 1942", "B. 1939", "C. 1950", "D. 1914"], "A"],

    ["What was the forced transfer of Filipino & American soldiers after Bataan?",
     ["A. Cebu March", "B. Bataan Death March", "C. Leyte Exodus", "D. Davao Walk"], "B"],

    ["Which operation liberated the Philippines?",
     ["A. Overlord", "B. Leyte Campaign 1944", "C. Torch", "D. Iwo Jima"], "B"],

    ["Who led the Japanese-sponsored government?",
     ["A. Manuel Quezon", "B. Jose P. Laurel", "C. Sergio Osmeña", "D. Corazon Aquino"], "B"],

    ["Which 1945 battle devastated Manila?",
     ["A. Battle of Manila", "B. Taal Eruption", "C. Mindoro Invasion", "D. Bataan"], "A"],

    ["Which battle in 1945 caused massive destruction of Intramuros and central Manila?",
     ["A. Battle of Manila", "B. Battle of Leyte Gulf", "C. Battle of Bataan", "D. Battle of Corregidor"], "A"],

    ["What was the primary role of the Kempeitai in the Philippines during the Japanese occupation?",
     ["A. Administering civilian education programs",
      "B. Serving as military police for intelligence, enforcement, suppression",
      "C. Managing Agricultural production and food distribution", "D.Training Filipino Soldiers for the Japanese"],
     "B"]
]


# Functions

def ask_questions(question_list):
    # Ask 5 random questions from the list and return score
    questions = random.sample(question_list, 5)
    score = 0
    for q in questions:
        print("\n" + q[0])
        for choice in q[1]:
            print(choice)
        answer = input("Your answer: ").upper()
        if answer == q[2]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was", q[2])
    return score


def convert_rank(score):
    # Convert score (0-5) to a rank
    if score == 5:
        return "S"
    elif score == 4:
        return "A"
    elif score == 3:
        return "B"
    elif score == 2:
        return "C"
    elif score == 1:
        return "D"
    else:
        return "F"


# Main game loop
def quiz_main():
    print("Welcome to the Main Game of LAKBAY KASAYSAYAN!")
    print("Topics:\n1. Spanish Era\n2. American Era\n3. Japanese Era")

    choice = input("Pick a topic (1-3): ")

    if choice == "1":
        score = ask_questions(spanish_questions)
        rank = convert_rank(score)
        print("\nYou got", score, "out of 5. Rank:", rank)
    elif choice == "2":
        score = ask_questions(american_questions)
        rank = convert_rank(score)
        print("\nYou got", score, "out of 5. Rank:", rank)
    elif choice == "3":
        score = ask_questions(japanese_questions)
        rank = convert_rank(score)
        print("\nYou got", score, "out of 5. Rank:", rank)
    else:
        print("Invalid choice.")


# Instruction Manual
def instructions():
    print("LAKBAY KASAYSAYAN")
    print("-" * 50)
    print("In LAKBAY KASAYSAYAN's main game, you will be quizzed!")
    print("> The topics range from the spanish era to the japanese occupation!")
    print("> These are ALL multiple choice questions, randomly taken from a list!")
    print("> Your choices range from A, B, C, or D. Remember to keep it Capital letters only!")
    print("-" * 50)
    print("SCORING SYSTEM")
    print("-" * 50)
    print("For every question you get right, you will be given a point!")
    print("> There are a total of three questions per era, the max score being 3.")
    print("> Depending on your score, you will get a Tier of S, A, B, C, D, E, or F.")
    print("> The highest Tier is S, corresponding to 3 points, lowest being F, which is 0 points.")
    print("> When playing multiple eras, your score will instead be the average score of all!")
    print("-" * 50)
    print("MAIN MENU")
    print("-" * 50)
    print("The main menu is the first thing you see when playing the game!")
    print("> Three choices, New Entry, Instructions Manual, and Leave!")
    print("> To start the main game, type in 1 for New entry!")
    print("> To see the Instructions manual, type in 2 for Instructions!")
    print("> To quit the game, type 3 for leave!")


# Run game

print("-" * 150)

print(r""" 
              _               _  ______      __     __  _  __           _____     __     _______     __     __      _   _ 
             | |        /\   | |/ /  _ \   /\\ \   / / | |/ /    /\    / ____|  /\\ \   / / ____|  /\\ \   / //\   | \ | |
             | |       /  \  | ' /| |_) | /  \\ \_/ /  | ' /    /  \  | (___   /  \\ \_/ / (___   /  \\ \_/ //  \  |  \| |
             | |      / /\ \ |  < |  _ < / /\ \\   /   |  <    / /\ \  \___ \ / /\ \\   / \___ \ / /\ \\   // /\ \ | . ` |
             | |____ / ____ \| . \| |_) / ____ \| |    | . \  / ____ \ ____) / ____ \| |  ____) / ____ \| |/ ____ \| |\  |
             |______/_/    \_\_|\_\____/_/    \_\_|    |_|\_\/_/    \_\_____/_/    \_\_| |_____/_/    \_\_/_/    \_\_| \_|

""")

print("-" * 150)

print(r""" 
      _______ _                           _       _____  _     _ _ _             _              _    _ _     _                   
     |__   __| |                         | |     |  __ \| |   (_) (_)           (_)            | |  | (_)   | |                  
        | |  | |__  _ __ ___  _   _  __ _| |__   | |__) | |__  _| |_ _ __  _ __  _ _ __   ___  | |__| |_ ___| |_ ___  _ __ _   _ 
        | |  | '_ \| '__/ _ \| | | |/ _` | '_ \  |  ___/| '_ \| | | | '_ \| '_ \| | '_ \ / _ \ |  __  | / __| __/ _ \| '__| | | |
        | |  | | | | | | (_) | |_| | (_| | | | | | |    | | | | | | | |_) | |_) | | | | |  __/ | |  | | \__ \ || (_) | |  | |_| |
        |_|  |_| |_|_|  \___/ \__,_|\__, |_| |_| |_|    |_| |_|_|_|_| .__/| .__/|_|_| |_|\___| |_|  |_|_|___/\__\___/|_|   \__, |
                                     __/ |                          | |   | |                                               __/ |
                                    |___/                           |_|   |_|                                              |___/ 
""")

print("-" * 150)

print("Welcome to LAKBAY KASAYSAYAN, a Philippine history quiz game!")
print(
    "\nIn this game, your knowledge of the Philippines throughout the occupation eras of the Spaniards, Americans, and Japanese, will be tested!")
print("\nAre you a beginner? Or will you prove yourself as an Expert Historian?")
print("-" * 100)
user_name = input("Tell me your name, historian! ")

print("-" * 100)

user_leave_choice = "N"

while user_leave_choice == "N":

    print("Hello,", user_name + "!")

    print("1. New Entry")
    print("2. Instruction Manual")
    print("3. Leave")

    user_choice = input("What would you like to do, Historian? ")

    user_leave_choice = "N"

    if user_choice == "1":
        proceed_choice = "Y"
        while proceed_choice == "Y":
            quiz_main()
            proceed_choice = input("Do you want to start another Entry? (Y for Yes, N for No): ")
        print("Thank you for playing! Returning to main menu:")

    elif user_choice == "2":
        instructions()
        print("Thank you for reading! Returning to main menu:")

    elif user_choice == "3":
        user_leave_choice = str(input("Do you want to leave? (Y for Yes, N for No): "))

    else:
        print("Invalid choice!")

user_confirmation_leave = str(input("Are you sure you want to leave? (Y/N) "))
if user_leave_choice == "Y":
    print("Thank you for playing! See you next time,", user_name + "!")

else:
    print("Thank you for staying! Returning to main menu:")