
def knight_moves(position):
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    col = ord(position[0]) - ord('a')
    row = int(position[1]) - 1
    
    valid_moves = []
    for dc, dr in moves:
        new_col = col + dc
        new_row = row + dr
        if 0 <= new_col < 8 and 0 <= new_row < 8:
            valid_moves.append(chr(new_col + ord('a')) + str(new_row + 1))
    
    return valid_moves


def main():
    positions = ['a1', 'e4', 'h8', 'b5']
    for pos in positions:
        print(f"Knight moves from {pos}: {knight_moves(pos)}")


if __name__ == "__main__":
    main()
