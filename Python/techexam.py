A = "apple"
B = "pear"

def solution(A, B):
 a = A.split()
 b = B.split()
 c = []
 d = zip(a,b)
 for char in d:
     if len(char) == 1 in d:
         c.append(char)
         print(c)
         return len(c)

print(solution(A,B))



