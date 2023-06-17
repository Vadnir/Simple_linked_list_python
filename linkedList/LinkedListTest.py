from .LinkedList import LinkedList, Node
import unittest


class LinkedListTestUnit(unittest.TestCase):

    def test_linked_list_creation(self):
        l1 = LinkedList()
        self.assertEqual(l1.__str__(), "linkedList(None)")

    def test_linked_list_creation_with_args(self):
        l1 = LinkedList(nodes=["1", "2", "3"])
        self.assertEqual(l1.__str__(), "linkedList(1 -> 2 -> 3 -> None)")

    def test_linked_list_iterable(self):
        args = ["1", "2", "3"]
        l1 = LinkedList(nodes=args)
        test_args = []
        for i in l1:
            test_args.append(i.data)

        self.assertEqual(test_args, args)

    def test_linked_list_add_first(self):
        l1 = LinkedList()
        l1.add_first(Node("1"))

        self.assertEqual(l1.__str__(), "linkedList(1 -> None)")

    def test_linked_list_add_first_with_args(self):
        args = ["1", "2", "3"]
        l1 = LinkedList(nodes=args)
        l1.add_first(Node("new first"))

        self.assertEqual(l1.__str__(), "linkedList(new first -> 1 -> 2 -> 3 -> None)")

    def test_linked_list_add_last(self):
        l1 = LinkedList()
        l1.add_last(Node("last"))

        self.assertEqual(l1.__str__(), "linkedList(last -> None)")

    def test_linked_list_add_last_with_args(self):
        args = ["1", "2", "3"]
        l1 = LinkedList(nodes=args)
        l1.add_last(Node("last"))

        self.assertEqual(l1.__str__(), "linkedList(1 -> 2 -> 3 -> last -> None)")

    def test_linked_list_add_after(self):
        l1 = LinkedList()
        l1.add_first(Node("Node"))
        l1.add_after("Node", Node("New Node"))

        self.assertEqual(l1.__str__(), "linkedList(Node -> New Node -> None)")

    def test_linked_list_add_after_with_args(self):
        args = ["1", "2", "3"]
        l1 = LinkedList(nodes=args)
        l1.add_after("2", Node("2.5"))

        self.assertEqual(l1.__str__(), "linkedList(1 -> 2 -> 2.5 -> 3 -> None)")

    def test_linked_list_add_after_with_empy_list(self):
        l1 = LinkedList()
        l1.add_after("Some Data", Node("Node"))

        self.assertEqual(l1.__str__(), "linkedList(Some Data -> None)")

    def test_linked_list_add_before(self):
        l1 = LinkedList()
        l1.add_first(Node("Node"))
        l1.add_before("Node", Node("New Node"))

        self.assertEqual(l1.__str__(), "linkedList(New Node -> Node -> None)")

    def test_linked_list_add_before_with_args(self):
        args = ["1", "2", "3"]
        l1 = LinkedList(nodes=args)
        l1.add_before("2", Node("1.5"))

        self.assertEqual(l1.__str__(), "linkedList(1 -> 1.5 -> 2 -> 3 -> None)")

    def test_linked_list_add_before_with_empy_list(self):
        l1 = LinkedList()
        l1.add_before("Some Data", Node("Node"))

        self.assertEqual(l1.__str__(), "linkedList(Some Data -> None)")

    def test_linked_list_remove_node(self):
        l1 = LinkedList()
        l1.add_first(Node("Node"))
        l1.remove_node("Node")

        self.assertEqual(l1.__str__(), "linkedList(None)")

    def test_linked_list_remove_node_with_args(self):
        args = ["1", "2", "3"]
        l1 = LinkedList(nodes=args)
        l1.remove_node("2")

        self.assertEqual(l1.__str__(), "linkedList(1 -> 3 -> None)")

    def test_linked_list_remove_node_with_empy_list(self):
        l1 = LinkedList()
        l1.remove_node("Some Data")

        self.assertRaises(l1.__str__(), "Exception: List is empty")


if __name__ == '__main__':
    unittest.main()
