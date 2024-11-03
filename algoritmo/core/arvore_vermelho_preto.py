# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------

class RBNode:
    def __init__(self, key, color="R"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = RBNode(0, "B")  # Nó nulo da árvore
        self.root = self.TNULL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, k):
        while k.parent and k.parent.color == "R":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "R":  # Caso 1
                    u.color = "B"
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:  # Caso 2
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = "B"  # Caso 3
                    k.parent.parent.color = "R"
                    self.rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "R":  # Caso 1
                    u.color = "B"
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:  # Caso 2
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = "B"  # Caso 3
                    k.parent.parent.color = "R"
                    self.rotate_left(k.parent.parent)
        self.root.color = "B"

    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent is None:
            new_node.color = "B"
            return

        if new_node.parent.parent is None:
            return

        self.insert_fixup(new_node)

    def pre_order(self, node):
        if node != self.TNULL:
            print(f"{node.key}({node.color}) ", end="")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.key:
            return node

        if key < node.key:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    def search(self, key):
        node = self.search_tree_helper(self.root, key)
        if node != self.TNULL:
            return f"Nó com chave {key} encontrado. Cor: {node.color}"
        else:
            return f"Nó com chave {key} não encontrado."
        
    def height(self, node):
        if node == self.TNULL:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def left_subtree_height(self):
        return self.height(self.root.left) if self.root != self.TNULL else 0

    def right_subtree_height(self):
        return self.height(self.root.right) if self.root != self.TNULL else 0
