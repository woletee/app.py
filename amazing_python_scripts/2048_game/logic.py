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
    
