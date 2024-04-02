'''
input: s="egg" , t = "add"
output: true
'''
def isIsomorphic(self, s: str, t: str) -> bool:
    hashtable1 = {}
    hashtable2 = {}
    for h1, h2 in zip(s,t):
        if h1 not in hashtable1 and h2 not in hashtable2:
            hashtable1[h1] = h1
            hashtable2[h2] = h2
        elif hashtable1.get(h1) != h2 and hashtable2.get(h2) != h1:
            return False
        return True

s = "egg"
t = "add"
result = isIsomorphic(None, s,t)
print(result)