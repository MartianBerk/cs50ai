"""
Tic Tac Toe Player
"""
import copy
from typing import List, Set, Tuple, Union

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board) -> Union[str, None]:
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None

    counts = {X: 0, O: 0}
    for row in board:
        for cell in row:
            if cell is not None:
                counts[cell] += 1

    if counts[X] > counts[O]:
        return O

    return X


def actions(board) -> Union[Set[Tuple], None]:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                possible_actions.add((i, j,))

    return possible_actions


def result(board, action) -> List[List]:
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    # Cannot take credit for this, included as a result of check50
    if i < 0 or j < 0:
        raise Exception("Out of bounds.")

    if board[i][j]:
        raise Exception("Invalid action")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board


def winner(board) -> Union[str, None]:
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] != EMPTY and board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    
    elif board[1][0] != EMPTY and board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    
    elif board[2][0] != EMPTY and board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    
    elif board[0][0] != EMPTY and board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    
    elif board[0][1] != EMPTY and board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    
    elif board[0][2] != EMPTY and board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    
    elif board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    elif board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board) -> bool:
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    elif len(actions(board)) == 0:
        return True
    
    return False


def utility(board) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)

    if w == X:
        return 1
    
    if w == O:
        return -1
    
    return 0


def minimax(board) -> Union[Tuple, None]:
    """
    Returns the optimal action for the current player on the board.
    """

    # Wrap minimax algo to support tuple(score, action) for ease of execution. 
    # Alpha-Beta Pruning supported via alpha and beta arguments.
    def minimax_inner(board, player, alpha, beta):
        if terminal(board):
            return utility(board), None

        v = -11 if player == X else 11  # we represent infinity with 1 more than the highest/lowest possible score.
        va = None
        for a in actions(board):
            res = result(board, a)
            score, _ = minimax_inner(res, X if player == O else O, alpha, beta)
            if (player == X and score > v) or (player == O and score < v):
                v, va = score, a

            if alpha is not None and beta is not None:
                if player == X:
                    alpha = max(alpha, score)
                elif player == O:
                    beta = min(beta, score)
                
                if beta <= alpha:
                    break
        
        return v, va

    _, move = minimax_inner(board, player(board), -11, 11)
    return move
