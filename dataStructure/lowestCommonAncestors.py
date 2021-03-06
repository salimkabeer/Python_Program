class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    if root.info > max(v1, v2):
        # if v1, v2 is smaller than root then lca exist on left side of tree
        ans = lca(root.left, v1, v2)
    elif root.info < min(v1, v2):
        # if v1, v2 is greater than root then lca exist on right side of tree
        ans = lca(root.right, v1, v2)
    else:
        return root
    return ans


tree = BinarySearchTree()
t = int(raw_input())

arr = list(map(int, raw_input().split()))

for i in xrange(t):
    tree.create(arr[i])
    
v = list(map(int, raw_input().split()))
# import pdb; pdb.set_trace()
ans = lca(tree.root, v[0], v[1])
print ans
