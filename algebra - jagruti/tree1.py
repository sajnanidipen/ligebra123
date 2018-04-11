class TreeNode:
    def __init__(self,d):
        self.data = d
        self.lchild = None
        self.rchild = None

class MyTree:
    def __init__(self,t):
        self.root = t

    def preorder(self,t):
        if t is not None:
            print(t.data)
             self.preorder(t.lchild)
            self.preorder(t.rchild)

    def postorder(self,t):
        if t is not None:
            self.postorder(t.lchild)
            self.postorder(t.rchild)
            print(t.data)

    def inorder(self,t):
        if t is not None:
            self.inorder(t.lchild)
            print(t.data)
            self.inorder(t.rchild)
    def conversepre(self,t):
        if t is not None:
            print(t.data)
            self.conversepre(t.rchild)
            self.conversepre(t.lchild)
    def conversepost(self,t):
        if t is not None:
            self.conversepost(t.rchild)
            self.conversepost(t.lchild)
            print(t.data)
            
    def conversein(self,t):
        if t is not None:
            self.conversepost(t.rchild)
            print(t.data)
            self.conversepost(t.lchild)  
 
F = TreeNode("F")
B = TreeNode("B")
K = TreeNode("K")
A = TreeNode("A")
D = TreeNode("D")
G = TreeNode("G")
C = TreeNode("C")

F.lchild = B
F.rchild = K
def preorder(self,t):
        if t is not None:
            print(t.data)
             self.preorder(t.lchild)
            self.preorder(t.rchild)B.lchild = A
B.rchild = D
K.lchild = G
D.lchild = C

mt = MyTree(F)
print("the preorder is:")
mt.preorder(mt.root)
print("the postorder is:")
mt.postorder(mt.root)
print("the inorder is:")
mt.inorder(mt.root)
print("the conversepre is:")
mt.conversepre(mt.root)
print("the conversepost is:")
mt.conversepost(mt.root)
print("the conversein is:")
mt.conversein(mt.root)
