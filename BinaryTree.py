class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self, data):
        # checking for duplicate
        if data==self.data:
            return
        if data < self.data:
            # if the left node is available
            if self.left:
                # add a new data
                # (left direction)
                self.left.add_child(data)
            else:
                # if the left node is empty, create a new node
                # (creation)
                self.left=BinaryTreeNode(data)
        else:
            # if the right node is available
            if self.right:
                # (right direction)
                self.right.add_child(data)
            else:
                # (creation)
                # if the right node is empty, create a new node
                self.right=BinaryTreeNode(data)

    def search(self,val):
        if self.data == val:
            return True

       #(left direction)
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        # (right direction)
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

# In_order_traversal, we add all elements from the left tree,add the root node
 # and finally add all elements from the right tree.
    def in_order_traversal(self):
        elements=[]
        # visit  the left tree
        if self.left:
            elements+=self.left.in_order_traversal()

        # add the root node
        elements.append(self.data)

       # visit the right node
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    #--------------------Exercise-------------------
#1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calculates sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): performs preorder traversal of a binary tree

    def find_min(self):
        if self.left is None:
            return self.data
        elements = []
        # visit  the left tree
        if self.left:
            elements += self.left.in_order_traversal()
        print(elements)
        return elements[0]

    def delete(self,val):
        if val < self.data:
            if self.left:
                return self.left.delete(val)
        elif val > self.data:
            if self.right:
                return self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)

        return self
        


    def find_max(self):
        if self.right is None:
            return self.data
        elements = []
        # visit  the left tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements[len(elements)-1]

    def calculate_sum(self):
        elements = []
        # visit  the left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # add the root node
        elements.append(self.data)
        # visit the right node
        if self.right:
            elements += self.right.in_order_traversal()
        result=0
        for i in range(len(elements)):
            result+=elements[i]
        return result

    # In post_order_traversal, we add all elements from the left tree,add all elements from the right tree
    # before the root node.
    def post_order_traversal(self):
        elements = []
        # visit  the left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit the right node
        if self.right:
            elements += self.right.in_order_traversal()
        # add the root node
        elements.append(self.data)
        return elements


    # In pre_order_traversal, we add the root node first, before all elements from the left tree,
    # and all elements from the right tree
    def pre_order_traversal(self):
        # add the root node
        elements = [self.data]
        # visit  the left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit the right node
        if self.right:
            elements += self.right.in_order_traversal()



        return elements

# builds a tree
def build_tree(elements):
    print("Building tree with these elements ",elements)
    root=BinaryTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__=='__main__':
  # countries=['India','Pakistan','Holland','Germany','Zambia','USA','China','UK','Argentina']
  # countries_tree=build_tree(countries)
  numbers=[50,30,10,2,89,54,76,12,5,0,8,33,67,89,100]
  numbers_tree=build_tree(numbers)
  numbers_tree.delete(100)
  print("after deleting 100 ",numbers_tree.in_order_traversal())
#   print('In_Order_Traversal')
#   print(numbers_tree.in_order_traversal())
#   print('Post_Order_Traversal')
#   print(numbers_tree.post_order_traversal())
#   print('Pre_Order_Traversal')
#   print(numbers_tree.pre_order_traversal())
  # print('Does UK exist in the list?',countries_tree.search('UK'))
  # print('Does UK Ghana in the list?', countries_tree.search('Ghana'))