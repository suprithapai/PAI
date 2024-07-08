def nim_game():
    heaps = [3, 4, 5]
    player = 1 
    while True:
        print("Current state of heaps:", heaps)
        if sum(heaps) == 0:
            print("Player", player, "wins!")
            break
        while True:
            i = int(input("Player " + str(player) + ", choose a heap (0-2): "))
            if i >= 0 and i < len(heaps) and heaps[i] > 0:
                break
            else:
                print("INVALID MOVE")
        while True:
            n = int(input("Player " + str(player) + ", choose the number of objects to remove: "))
            if n > 0 and n <= heaps[i]:
                break
            else:
                print("INVALID MOVE")
        heaps[i] -= n
        player = 3 - player

if __name__ == "__main__":
    nim_game()
