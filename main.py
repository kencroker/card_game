import BlackjackGame


if __name__ == '__main__':
    for i in range(1, 10):
        try:
            num_players = int(input("How many players?"))
            break
        except:
            print("Please enter a valid integer")
            continue

    bj_game = BlackjackGame.BlackjackGame(num_players=num_players)

    bj_game.pregame_display()
    bj_game.play_game()
