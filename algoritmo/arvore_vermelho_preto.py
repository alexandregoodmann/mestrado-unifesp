# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 05
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

# Uso
rb_tree = RedBlackTree()
for key in [41, 38, 31, 12, 19, 8, 50, 1, 100, 101]:
    rb_tree.insert(key)

print("Pre-ordem da árvore Vermelho-Preto:")
rb_tree.pre_order(rb_tree.root)
