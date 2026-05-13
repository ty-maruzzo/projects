from shutil import move

import cell

class BlueBot:
    """A robot that moves through an arena and paints its trail blue."""

    def __init__(self, row, col):
        self.cell = cell.Cell(row, col)
        self.color = "🔵"
        self.icon = "🤖"

    def pick_move(self, arena):
        """Returns a proposed Cell to move to on this turn."""
        
        def nearest_enemy_tile(arena):
            """Returns the nearest enemy tile to the bot."""
            nearest = None
            min_distance = float('inf')
            for row in range(arena.size):
                for col in range(arena.size):
                    cell_value = arena.get_symbol(cell.Cell(row,col))
                    if cell_value == "🟥":
                        distance = abs(row - self.cell.row) + abs(col - self.cell.col)
                        if distance < min_distance:
                            min_distance = distance
                            nearest = cell.Cell(row, col)
            return nearest
            
        def nearest_empty_tile(arena):
            """Returns the nearest empty tile to the bot."""
            nearest = None
            min_distance = float('inf')
            for row in range(arena.size):
                for col in range(arena.size):
                    cell_value = arena.get_symbol(cell.Cell(row,col))
                    if cell_value == "⬜":
                        distance = abs(row - self.cell.row) + abs(col - self.cell.col)
                        if distance < min_distance:
                            min_distance = distance
                            nearest = cell.Cell(row, col)
            return nearest
        def move_towards(target):
            """Returns a move towards the target cell."""
            if not target:
                return self.cell
            
            new_row = self.cell.row + (1 if target.row > self.cell.row else -1 if target.row < self.cell.row else 0)
            new_col = self.cell.col + (1 if target.col > self.cell.col else -1 if target.col < self.cell.col else 0)
            return cell.Cell(new_row, new_col)
        
        target = nearest_enemy_tile(arena)
        if not target:
            target = nearest_empty_tile(arena)
        
        return move_towards(target)