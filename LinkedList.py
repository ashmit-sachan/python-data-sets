from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAfter(self, node, data):
        given_node = self.search(node)['node']
        new_node = Node(data)
        next_node = given_node.next
        next_node.prev = new_node
        new_node.next = next_node
        new_node.prev = given_node
        given_node.next = new_node

    def insertBefore(self, node, data):
        given_node = self.search(node)['node']
        new_node = Node(data)
        prev_node = given_node.prev
        prev_node.next = new_node
        new_node.next = given_node
        new_node.prev = prev_node
        given_node.prev = new_node

    def delete(self, elements):
        index = -1
        head = self.head
        while head is not None:
            index += 1
            if index in elements:
                prev_node = head.prev
                next_node = head.next
                if prev_node is not None:
                    prev_node.next = next_node
                if next_node is not None:
                    next_node.prev = prev_node

            head = head.next

    def remove(self, key):
        if isinstance(key, list):
            self.delete(key)
        else:
            node_indexes = self.search(key)['indexes']
            self.delete(node_indexes)

    def search(self, data):
        head = self.head
        current_index = -1
        info = {'node': None, 'count': 0, 'indexes': []}
        while head is not None:
            current_index += 1
            if head.data == data:
                info['node'] = head
                info['count'] += 1
                info['indexes'].append(current_index)
            head = head.next
        if info['count'] == 0:
            return None
        else:
            return info

    def sort(self):
        current_node = self.head.next
        while current_node is not None:
            next_node = current_node.next
            search_node = current_node.prev
            while search_node is not None and search_node.data > current_node.data:
                search_node = search_node.prev
            self.remove(current_node.data)
            if search_node is None:
                current_node.prev = None
                self.prepend(current_node.data)
            else:
                self.insertAfter(search_node.data, current_node.data)
            current_node = next_node

    def print(self):
        output = ""
        head = self.head
        while head is not None:
            output += str(head.data) + " ---> "
            head = head.next

        if not len(output) > 0:
            output += "The list is empty!"

        return output[:-6]
