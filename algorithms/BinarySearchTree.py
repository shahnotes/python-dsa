class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        temp = self.root
        while True:
            if node.value == temp.value:
                return False
            if node.value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def DFS_pre_order(self):
        results = []

        def traverse(current_node):
            if current_node is not None:
                results.append(current_node.value)
                if current_node.left is not None:
                    traverse(current_node.left)
                if current_node.right is not None:
                    traverse(current_node.right)

        traverse(self.root)
        return results

    def DFS_post_order(self):
        results = []

        def traverse(current_node):
            if current_node is not None:
                if current_node.left is not None:
                    traverse(current_node.left)
                if current_node.right is not None:
                    traverse(current_node.right)
                results.append(current_node.value)

        traverse(self.root)
        return results

    def DFS_in_order(self):
        results = []

        def traverse(current_node):
            if current_node is not None:
                if current_node.left is not None:
                    traverse(current_node.left)
                results.append(current_node.value)
                if current_node.right is not None:
                    traverse(current_node.right)

        traverse(self.root)
        return results
