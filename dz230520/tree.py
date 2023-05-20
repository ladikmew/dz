class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.first_value = None

    def __finding(self, node, parent, val):
        if node is None:
            return None, parent, False

        if val == node.data:
            return node, parent, True

        if val < node.data:
            if node.left:
                return self.__finding(node.left, node, val)

        if val > node.data:
            if node.right:
                return self.__finding(node.right, node, val)

        return node, parent, False

    def append_node(self, obj):
        if self.first_value is None:
            self.first_value = obj
            return obj
        s,p,find = self.__finding(self.first_value, None,obj.data)

        if not find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show(self,node):
        if node is None:
            return

        self.show(node.left)
        print(node.data)
        self.show(node.right)

    def __del_leaf(self,s,p):
        if p.left ==s:
            p.lef = None
        elif p.right ==s:
            p.right = None

    def __del_one_node(self,s,p):
        if p.left ==s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.right  #*

        elif p.right ==s:
            if s.left is None:
                p.right = s.left
            elif s.right is None:
                p.right = s.left

    def __find_min(self,node,parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node,parent



    def del_node(self,key):
        s, p, find = self.__finding(self.first_value, None, key)

        if not find:
            return None
        if s.left is None and s.right is None:
            self.__del_leaf(s,p)
        elif s.left is None or s.right is None:
            self.__del_one_node(s,p)
        else:
            sr,pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_node(sr,pr)




v = [10,5,7,16,13,2,20]

t = Tree()
for i in v:
    t.append_node(Node(i))
t.del_node(5)
t.show(t.first_value)

