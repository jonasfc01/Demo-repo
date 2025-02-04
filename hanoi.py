from sys import stdin
moves = []
def hanoi(a,b,c,n):
    global moves
    if n ==1:
        moves.append(a + "->" + c)
    else:
        hanoi(a,c,b,n-1)
        moves.append(a + "->" + c)
        hanoi(b,a,c,n-1)
    