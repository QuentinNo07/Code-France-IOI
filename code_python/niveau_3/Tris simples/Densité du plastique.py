nb_block = int(input())
liste_block = set(map(int, input().split()))

nb_question = int(input())

for i in range(nb_question):
    question = int(input())
    if question in liste_block:
        print("1")
    else:
        print("0")