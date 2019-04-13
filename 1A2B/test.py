import Game_1A2B

game = Game_1A2B.Game1A2B()
while not game.isOver:
    ans = input('請輸入答案:')
    print(game.checkAns(ans))