class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
           
            if self.left:
                self.left.add_child(data) 
            else:
                self.left = BinaryTreeNode(data)
        else:
            
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def search_element(self, elem):
        if self.data == elem:
            return True
        elif elem < self.data:
           
            if self.left:
               return self.left.search_element(elem)  
            else:
                return False
            
        else:
            
            if self.right:
                return self.right.search_element(elem)  
            else:
                return False


def deleteNode(root, key):
 
    
    if root is None:
        return root
 
   
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root
 
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
        return root
 
  
     
     
    if root.left is None and root.right is None:
          return None
 
 
    if root.left is None:
        temp = root.right
        root = None
        return temp
 
    elif root.right is None:
        temp = root.left
        root = None
        return temp
 
    
 
    succParent = root
 
    
 
    succ = root.right
 
    while succ.left != None:
        succParent = succ
        succ = succ.left
 
   
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
 
    
 
    root.key = succ.key
 
    return root


#inspired by https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
