def main():
    path = input()
    with open(path, 'r') as f:
        words = [ i for i in f if len(i.replace("\n", "")) == 5 ]

    with open("words.txt", 'w') as f:
        for w in words:
            f.write(w)

main()
