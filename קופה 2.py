def koopa():         

    Items=["Popcorn","Lemonade","Hot dogs"]
    amounts = [35,5,15]
    total=0

    for i in range(3):

        amount=int(input(f"How many {Items[i]}?\n"))
        amounts[i] *= amount

    return amounts

def pay(give, need):  

    while(give<need):

        print(f"Not enough, need {need - give } more")

        more = int(input("Give more money\n"))
        give+=more

    if give>need:

        change = give - need
        print(f"Your change is {change}")
    
    print("Good day")

print("Popcorn is 35, Lemonade is 5 and Hot dogs are 15")

amounts = koopa()

total = sum(amounts)

print(f"{amounts[0]} for popcorn, {amounts[1]} for lemonade and {amounts[2]} for hot dogs.\n{total} in total.\n")

num = int(input("How much money do you have?\n"))
pay(num, total)
