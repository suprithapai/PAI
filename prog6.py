
def nim_game():
    # Initial heap configuration
    heaps = [3, 4, 5]
    
    def display_heaps():
        print(f"Heaps: {heaps}")
    
    def player_turn(player):
        while True:
            try:
                heap = int(input(f"Player {player}, choose a heap (1, 2, or 3): ")) - 1
                if heap < 0 or heap >= len(heaps):
                    print("Invalid heap number. Please try again.")
                    continue
                
                if heaps[heap] == 0:
                    print("Selected heap is empty. Choose another heap.")
                    continue
                
                count = int(input(f"Player {player}, choose number of objects to remove from heap {heap + 1}: "))
                if count <= 0 or count > heaps[heap]:
                    print("Invalid number of objects. Please try again.")
                    continue
                
                heaps[heap] -= count
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    
    player = 1
    while sum(heaps) > 0:
        display_heaps()
        player_turn(player)
        if sum(heaps) == 0:
            print(f"Player {player} wins!")
            break
        player = 2 if player == 1 else 1

nim_game()
