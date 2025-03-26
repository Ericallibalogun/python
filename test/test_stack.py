import unittest

from mycollection import stack

class Stack(unittest.TestCase):
    def test_that_element_can_add_stack(self):
        stack1 = stack.Stack()
        self.assertEqual(len(stack1.stack), 0)
        stack1.push(1)
        self.assertEqual(len(stack1.stack),1)
        stack1.push(6)
        self.assertEqual(len(stack1.stack),2)

    def test_that_element_can_remove_stack(self):
        stack1 = stack.Stack()
        stack1.push(1)
        stack1.push(6)
        stack1.pop(1)
        self.assertEqual(len(stack1.stack),1)


if __name__ == '__main__':
    unittest.main()
