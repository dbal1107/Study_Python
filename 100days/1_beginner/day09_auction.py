from replit import clear
add = clear()

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

bid_list = list()
person = {}

def auction(name, bid):

    person["name"] = name
    person["bid"] = bid
    
    bid_list.append(person)

while clear = True:
    print("Welcome to the secret auction program.")
    name = input('What is your name?: \n')
    bid = int(input("What's your bid?: $"))
    auction(name, bid)

    add_person = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if add_person == 'yes':
        print(clear)
    else:
        # for i in bid_list:
        bid = person["bid"].max()

        print(f"The winner is {name} with a bid of ${bid}")




