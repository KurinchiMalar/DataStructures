
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def set_data(self,newdata):
        self.data = newdata

    def get_left(self):
        return self.left

    def set_left(self,node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self,node):
        self.right = node

    def __str__(self):
        return "Node[Data = %s]" % (self.data,)