class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            seen = set()

            for col in range(9):
                current_cell = board[row][col]


                if current_cell == ".":
                    continue

                if current_cell in seen:
                    return False

                seen.add(current_cell)

        for col in range(9):
            seen = set()

            for row in range(9):
                current_cell = board[row][col]


                if current_cell == ".":
                    continue

                if current_cell in seen:
                    return False

                seen.add(current_cell)

        for box_row in range(3):
            for box_col in range(3):
                seen = set()

                for row in range(3):
                    for col in range(3):
                        current_cell = board[box_row * 3 + row][box_col * 3 + col]

                        if current_cell == ".":
                            continue 
                        if current_cell in seen:
                            return False
                        seen.add(current_cell)
        return True


            