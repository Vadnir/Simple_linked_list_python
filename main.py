from linkedList.LinkedListTest import LinkedListTestUnit
import unittest


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(LinkedListTestUnit)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()