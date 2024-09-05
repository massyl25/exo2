name=input("enter your name:")
def check_name(name):
    reversed=name[::-1]
    if (reversed==name):
        print("your name stay the same no matter what.")
    else:
        print("sorry your name isnt revesrable.")
check_name(name)