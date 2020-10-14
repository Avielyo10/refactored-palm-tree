from strategies.base_strategy import Strategy, formula


def __greedy_formula(x1, x2, y1, y2):
    a = x1*y2
    b = x2*y1
    if a > b:
        return "root"
    return "node"


def __is_root_bigger(root, node):
    name = __greedy_formula(root.x, root.y, node.x, node.y)
    if name == "root":
        return True
    return False


class Node:
    def __init__(self, x, y):
        self.l_child = None
        self.r_child = None
        self.x = x
        self.y = y


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if __is_root_bigger(root, node):
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)


class Greedy(Strategy):
    def solve(self):
        root_node = Node(self.a_array[0], self.b_array[0])
        for index in range(1, self.num_of_jobs):
            binary_insert(root_node, Node(self.a_array[index], self.b_array[index]))
        
        self.move_in_order(root_node)
        self.find_cmax_greedy()

    def move_in_order(self, root):
        if not root:
            return
        self.move_in_order(root.l_child)
        self.correct_order.append((root.x, root.y))
        self.move_in_order(root.r_child)

    def find_cmax_greedy(self):
        cmax = 0
        for a_i, b_i in self.correct_order:
            cmax += formula(a_i, b_i,cmax)
        self.cmax = cmax