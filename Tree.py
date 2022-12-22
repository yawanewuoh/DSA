class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    # every data must be an object of the TreeNode class.
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level


    def print_tree(self):
        # space according to level
        spaces= ' ' * self.get_level() * 3
        prefix=spaces + '|__' if self.parent else ''
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root=TreeNode('Electronics')

    laptop=TreeNode('Laptop')
    laptop.add_child(TreeNode('Hp'))
    laptop.add_child(TreeNode('Dell'))
    laptop.add_child(TreeNode('Mac'))

    cellphone=TreeNode('cellphone')
    cellphone.add_child(TreeNode('Samsung'))
    cellphone.add_child(TreeNode('Techno'))
    cellphone.add_child(TreeNode('Iphone'))

    Tv=TreeNode('Tv')
    Tv.add_child(TreeNode('Hisense'))
    Tv.add_child(TreeNode('Samsung'))
    Tv.add_child(TreeNode('Akai'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(Tv)

    return root

if __name__=='__main__':
    root=build_product_tree()
    root.print_tree()

