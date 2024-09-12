

# tower breaker
# 2 players
# tower x height, remove certain number of height, so that remaining height y evenly divides x
# If the current player is unable to make a move, they lose the game.

def towerBreakers(n, m):
    # change the question to reduce all tower height to 1 
    # calculate the steps needed
    # if steps is odd, player 2 loose, vice versa 

    # declare variable 
    winner = int()

    if m == 1:
        winner = 2
        return winner

    # assume if even number of tower n, player 1 cannot win
    if n % 2 == 0:
        winner = 2
    # assume if odd number of tower n, player 2 cannot win
    else:
        winner = 1
    return winner

if __name__ == "__main__":
    n = 2
    m = 2
    print(towerBreakers(n,m))