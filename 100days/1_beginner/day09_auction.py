from replit import clear
clear()
logo = '''
        ___________
        \         /
        )_______(
        |"""""""|_.-._,.---------.,_.-._
        |       | | |               | | ''-.
        |       |_| |_             _| |_..-'
        |_______| '-' `'---------'` '-'
        )"""""""(
        /_________\\
    .-------------.
    /_______________\\
'''
print(logo)

person = {}

game = True
while game:
    print("Welcome to the secret auction program.")
    name = input('What is your name?: \n ')
    bid = int(input("What's your bid?: \n $"))
    person[name] = bid

    add_person = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear()

    money = list()
    if add_person == 'no':
        for i in person:
            money.append(person[i])
            if max(money) == person[i]:
                winner = max(money)
                name = i
        print(f"The winner is '{name}' with a bid of $ {winner} !\n")
        print(f"{person}\n")
        game = False





