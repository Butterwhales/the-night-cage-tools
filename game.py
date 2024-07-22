from dataclasses import dataclass, field
from typing import List
import random

@dataclass
class TileType:
    name: str

@dataclass
class Tile:
    type: TileType

@dataclass
class GameBoard:
    tiles: List[Tile] = field(default_factory=list)

    def create_board(self, keeper_count):
        self.tiles = []
        self.tiles.extend([Tile(TileType("Start"))] * 5)
        self.tiles.extend([Tile(TileType("Key"))] * 8)
        self.tiles.extend([Tile(TileType("Gate"))] * 4)
        self.tiles.extend([Tile(TileType("Wax Eater Monster"))] * 13)
        self.tiles.extend([Tile(TileType("Straight Passage"))] * 10)
        self.tiles.extend([Tile(TileType("\"T\" Passage"))] * 32)
        self.tiles.extend([Tile(TileType("4-Way Passage"))] * 12)
        self.tiles.extend([Tile(TileType("Keeper"))] * keeper_count)
    
    def shuffle_tiles(self):
        random.shuffle(self.tiles)

    def draw(self):
        if not self.tiles:
            return None
        return self.tiles.pop()
    
    def view_tiles(self):
        return [tile.type.name for tile in self.tiles]

def main():
    print("Welcome to the Tile Drawing Game!")
    keeper_count = int(input("Enter the number of Keeper tiles: "))
    
    board = GameBoard()
    board.create_board(keeper_count)
    board.shuffle_tiles()
    
    while True:
        print("\nCommands:")
        print("1. Draw a tile (type 'draw')")
        print("2. View remaining tiles (type 'view')")
        print("3. Exit (type 'exit')")

        command = input("Enter command: ").strip().lower()
        
        if command == 'draw':
            tile = board.draw()
            if tile:
                print(f"You drew a {tile.type.name} tile.")
            else:
                print("No more tiles to draw!")
        elif command == 'view':
            remaining_tiles = board.view_tiles()
            if remaining_tiles:
                print("Remaining tiles:")
                for tile in remaining_tiles:
                    print(f"- {tile}")
            else:
                print("No tiles remaining.")
        elif command == 'exit':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
