import random   
def get_start_game():
    mat=[]
    for i in range(4):
        mat.append([0,0,0,0,0])
        add_two(mat)
        return mat
def add_two(mat):
    r=random.randint(0,4)
    c=random.randint(0,4)
    while(mat[r]!=0):
        r=random.randint(0,4)
        c=random.randint(0,4)
    mat[r]=2
def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "won"
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return "Game is not yet over"
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return "Game is not over yet"
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return "Game is not over yet"
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "Game is not over yet"
    return "Lost"
