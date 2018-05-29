import random as r

def main():
    play()
    return 0

def play():
    keep_playing = 'y'
    cash = 100
    bet = 10
    while(keep_playing == 'y'):
        print_starting_balance(cash)
        cash = play_a_game(cash,bet)
        print_balance(cash)
        keep_playing = play_again()
def play_a_game(cash,bet):
    point = 0
    dicerolls = []
    # First Roll
    num = rolldice(1,6)
    dicerolls.append(num)

    if(automatic_win(num)):
        print_outcome(automatic_win(num),dicerolls)
        cash+=bet
    elif(automatic_loss(num)):
        print_outcome(not(automatic_loss(num)),dicerolls)
        cash-=bet
    else:
        # Next Turns Fall In Here
        while True:
            point = num
            num = rolldice(1,6)
            dicerolls.append(num)
            if(testfor_7(num)):
                print_outcome(not(testfor_7(num)),dicerolls)
                cash-=bet
                break
            elif(num == point):
                print_outcome((num==point),dicerolls)
                cash+=bet
                break
            else:
                pass
    return cash
def rolldice(min,max):
    return r.randint(min,max) + r.randint(min,max)
def testfor_2(number):
    return number==2
def testfor_3(number):
    return number==3
def testfor_7(number):
    return number==7
def testfor_11(number):
    return number==11
def testfor_12(number):
    return number==12
def automatic_win(number):
    return(testfor_7(number) or testfor_11(number))
def automatic_loss(number):
    return (testfor_2(number) or testfor_3(number) or testfor_12(number))
def print_outcome(outcome,dicerolls):
    for i in range(len(dicerolls)):
        print(dicerolls[i],end=" ")
    if(outcome):
        print("You Win!")
    else:
        print("You Lose!")
def print_starting_balance(cash):
    print("Beginning Balance = ${}".format(cash))
def print_balance(cash):
    print("Balance = ${}".format(cash),end=" ")
def play_again():
    print("- Play again? y/n: ",end="")
    return input()


if __name__== "__main__":
    main()
