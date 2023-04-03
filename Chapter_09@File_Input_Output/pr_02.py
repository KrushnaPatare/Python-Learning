def game(score=0):
    highscore=None
    if highscore==None:
        highscore=0
    if highscore<=score:
        highscore=score
        return highscore
    else:
        return highscore

totalscore=game()
print(totalscore)

totalscore=game(55)
print(totalscore)