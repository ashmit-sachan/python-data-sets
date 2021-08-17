class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches.
            if current_node.key == desired_key:
                return current_node
            elif desired_key < current_node.key:
                current_node = current_node.left

            else:
                current_node = current_node.right

        # The key was not found in the tree.
        return None

    def insert(self, node):

        # Check if the tree is empty
        if self.root is None:
            self.root = node
            self.count += 1
        else:
            current_node = self.root
            self.count += 1
            while current_node is not None:
                if node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right

    def Distance(self, node_find, node_get=None, number_edges=-1):
        number_edges += 1
        if node_find == node_get.key:
            print(number_edges)
        else:
            if node_find.left is not None:
                self.Distance(node_find, node_find.left, number_edges)
            if node_find.right is not None:
                self.Distance(node_find, node_find.left, number_edges)

        if number_edges == 0:
            print("Not Found!")


if __name__ == '__main__':
    tree = BinarySearchTree()
    inp = input()
    while inp == "End!":
        print("BST needs at least one node, enter a valid input please!")
        inp = input()

    while inp != "End!":
        nd = Node(inp)
        tree.insert(nd)
        inp = input()

    print("Which node would you pick?")
    nod = input()

    while nod == "Y":
        tree.Distance(tree.root)
        print("Would you like to choose another node? Y/N")




