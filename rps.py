from Check import check
random_que = [
    "Rock | Paper | Scissor ? \n",
    "Rock | Paper | Scissor ? \n",
    "Rock | Paper | Scissor ? \n"
]

random_check = [
    check(random_que[0], 'scissor'),
    check(random_que[1], 'rock'),
    check(random_que[2], 'paper')
]

def run_game(random_check):
    score = 0
    for check in random_check:
        answer = input(check.prompt)
        if answer == check.choose:
            score += 1
            print('Matched!\n')
        else:
            print('Not Matched!\n')

    winorlose = int(len(random_check))/2
    if winorlose < int(score):
        print("Congrates! You Won.  (Your score is " + str(score) + " out of " + str(len(random_check))+')')
    else:
        print("Bad Luck! You lost.  (Your score is " + str(score) + " out of " + str(len(random_check))+')')



run_game(random_check)


