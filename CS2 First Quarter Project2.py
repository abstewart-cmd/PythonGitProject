import random

# --- Questions for each topic ---
spanish_questions = [
    ["Who established the first permanent Spanish settlement in Cebu in 1565?",
     ["A. Ferdinand Magellan", "B. Miguel López de Legazpi", "C. Andres de Urdaneta", "D. Diego Silang"], "B"],

    ["Which event in 1896 marked the beginning of the Philippine Revolution?",
     ["A. Cry of Balintawak", "B. Declaration of Independence", "C. Treaty of Tordesillas", "D. Battle of Manila Bay"], "A"],

    ["Who was executed on December 30, 1896?",
     ["A. Andres Bonifacio", "B. Emilio Aguinaldo", "C. Jose Rizal", "D. Apolinario Mabini"], "C"],

    ["What was the system granting Spaniards land and labor from natives called?",
     ["A. Encomienda", "B. Feudalism", "C. Zemstvo", "D. Padrino system"], "A"],

    ["Which movement included Rizal and Marcelo H. del Pilar?",
     ["A. Katipunan", "B. Propaganda Movement", "C. Hukbalahap", "D. Kilusang Bagong Lipunan"], "B"]
]

american_questions = [
    ["Which event ended Spanish rule and gave control to the U.S. in 1898?",
     ["A. Treaty of Paris", "B. Spanish Civil War", "C. Battle of Waterloo", "D. Boxer Rebellion"], "A"],

    ["Who was the first President of the Philippine Republic?",
     ["A. Jose P. Laurel", "B. Emilio Aguinaldo", "C. Manuel Quezon", "D. Sergio Osmeña"], "B"],

    ["Which education policy did Americans bring?",
     ["A. Free-market universities", "B. Public schools with English", "C. Expansion of Spanish colleges", "D. Military schools"], "B"],

    ["What 1935 political milestone created the Commonwealth?",
     ["A. Jones Act", "B. Tydings–McDuffie Act", "C. 1935 Constitution", "D. Bataan Proclamation"], "C"],

    ["Which naval battle ended Spanish naval power in the Pacific?",
     ["A. Midway", "B. Manila Bay", "C. Leyte Gulf", "D. Trafalgar"], "B"]
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
     ["A. Battle of Manila", "B. Taal Eruption", "C. Mindoro Invasion", "D. Bataan"], "A"]
]

# --- Functions ---

def ask_questions(question_list):
    """Ask 3 random questions from the list and return score"""
    questions = random.sample(question_list, 3)
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

def convert_to_rank(score):
    """Convert score (0–3) to a rank"""
    if score == 3:
        return "S"
    elif score == 2:
        return "A"
    elif score == 1:
        return "C"
    else:
        return "F"

# --- Main game loop ---
def main():
    print("Welcome to the Philippine History Quiz Game!")
    print("Topics:\n1. Spanish Era\n2. American Era\n3. Japanese Era")

    choice = input("Pick a topic (1-3): ")

    if choice == "1":
        score = ask_questions(spanish_questions)
        rank = convert_to_rank(score)
        print("\nYou got", score, "out of 3. Rank:", rank)
    elif choice == "2":
        score = ask_questions(american_questions)
        rank = convert_to_rank(score)
        print("\nYou got", score, "out of 3. Rank:", rank)
    elif choice == "3":
        score = ask_questions(japanese_questions)
        rank = convert_to_rank(score)
        print("\nYou got", score, "out of 3. Rank:", rank)
    else:
        print("Invalid choice.")

# --- Run game ---
main()