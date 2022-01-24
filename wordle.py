import random

def main():
    words = []

    with open('words.txt', 'r') as f:
        words = [ i.replace("\n", "") for i in f ]

    wordset = set(words)

    answer = random.choice(words)

    turn = 1

    while True:
        if turn > 6:
            print("Oops...")
            return

        print(f"What is the word? (turn {turn}/6):")
        i = input()

        if len(i) != 5:
            print("Enter a 5 letter word.\n")
            continue

        if i not in wordset:
            print("Please enter a word that exists in English.\n")
            continue

        res = []
        for j in range(5):
            if i[j] == answer[j]:
                res.append("🟩")
            elif i[j] in answer:
                res.append("🟨")
            else:
                res.append("⬜")

        print("\n")
        print(*res, sep=" ")
        print("\n")

        turn += 1

        if i == answer:
            print("Congrat!!")
            return

main()
