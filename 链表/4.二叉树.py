

#二叉树的最高节点只能小于等于2
# 完全二叉树：除了最底层大的节点，上面所有的节点都满了，也就是说其他的每一个节点的子节点数都是2
# 满二叉树：所有层都达到最大的数量，包括最底层的节点
# 平衡二叉树：任意两颗子树之间的深度之差不能超过1
# 排序二叉树|二叉搜索树
class Node:
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None
class Tree:
    """
    二叉树
    """
    def __init__(self):
        self.root = None
    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    def breadth_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=',')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    def preorder(self,node):
        """先序遍历"""
        if node is None:
            return
        print(node.elem,end=',')
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    def cenorder(self,node):
        """中序遍历"""
        if node is None:
            return
        self.cenorder(node.lchild)
        print(node.elem,end=',')
        self.cenorder(node.rchild)
    def postorder(self,node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem,end=' ')
    def postorder2(self,node):
        stack = [node]
        stack2 = []
        while stack:
            node = stack.pop()
            stack2.append(node)
            if node.lchild is not None:
                stack.append(node.lchild)
            if node .rchild is not None:
                stack.append(node.rchild)
        #在这里把左右的节点都存起来放到第二个栈里面，所以输出的时候反着输出就好了
        while stack2:
            print(stack2.pop().val)
if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print()
    tree.preorder(tree.root)
    print()
    tree.cenorder(tree.root)
    print()
    tree.postorder(tree.root)

