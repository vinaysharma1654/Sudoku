from collections import defaultdict
class Solution:
    def __init__(self):
    	self.final=[]
    def solveSudoku(self, A):
       self.final=[]
       dic={0:0,1:0,2:0,3:1,4:1,5:1,6:2,7:2,8:2}
       d2=defaultdict(set)
       M=[]
       for i in range(len(A)):
           M.append([])
           for j in range(len(A[0])):
               M[i].append(A[i][j])
               if(A[i][j]!='.'):
                   d2[(dic[i],dic[j])].add(A[i][j])
       def check(y,M,e):
           for i in range(9):
               if(M[i][y]==e):
                   return(True)
           return(False)
       def recur(M,A,d,x,y,dic):
           if(x==9):
               print('a')
               self.final=M
               return
           if(A[x][y]!='.'):
               if(y==8):
                   recur(M,A,d,x+1,0,dic)
                   if(self.final!=[]):return
               else:
                   recur(M,A,d,x,y+1,dic)
                   if(self.final!=[]):return
               return
           for i in range(1,10):
               if((str(i) not in M[x]) and (check(y,M,str(i))==False) and (str(i) not in d[(dic[x],dic[y])])):
                   M[x][y]=str(i)
                   d[(dic[x],dic[y])].add(str(i))
                   if(y==8):
                       recur(M,A,d,x+1,0,dic)
                       if(self.final!=[]):return
                   else:
                       recur(M,A,d,x,y+1,dic)
                       if(self.final!=[]):return
                   M[x][y]='.'
                   d[(dic[x],dic[y])].remove(str(i))
           return
       recur(M,A,d2,0,0,dic)
       return(self.final)
cl=Solution()
mat=[['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
print(cl.solveSudoku(mat))                  
              
              
           
       