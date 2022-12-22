class TreeNode:
    def __init__(self,name,position):
        self.name=name
        self.children=[]
        self.parent=None
        self.position=position


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


    def print_root(self,level):
        if self.get_level() > level:
            return
        # space according to level
        spaces= ' ' * self.get_level() * 3
        prefix=spaces + '|__' if self.parent else ''
        print(prefix + self.name)

        if self.children:
            for child in self.children:
                child.print_root(level)



def build_product_tree():
    root=TreeNode('Nilpul','CEO')

    CTO=TreeNode('Chinmay','CTO')
    Infrastructure_Head=TreeNode('Vishwa','Infrastructure Head')
    Infrastructure_Head.add_child(TreeNode('Dhaval','Cloud Manager'))
    Infrastructure_Head.add_child(TreeNode('Abhijit','App Manager'))
    CTO.add_child(Infrastructure_Head)

    Application_Head = TreeNode('Aamir','Application Head')
    CTO.add_child(Application_Head)

    HR_Head=TreeNode('Gels','HR_Head')
    Recruitment_Manager=TreeNode('Peter','Recruitment Manager')
    Policy_Manager = TreeNode('Waqas','Policy Manager')

    HR_Head.add_child(Recruitment_Manager)
    HR_Head.add_child(Policy_Manager)

    root.add_child(CTO)
    root.add_child(HR_Head)
    return root

if __name__=='__main__':
    root=build_product_tree()
    root.print_root(-1)