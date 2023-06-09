
import unittest

from wifi_utils import mac_addr


class Test(unittest.TestCase):

    def test_True(self):
        self.assertEqual(len(mac_addr.create_mac_addr().split(':')), 6)
        for addr in mac_addr.create_mac_addr().split(':'):
            self.assertEqual(len(addr), 2)

        self.assertEqual(len(mac_addr.create_mac_addr(delimiter='-').split('-')), 6)
        for addr in mac_addr.create_mac_addr(delimiter='-').split('-'):
            self.assertEqual(len(addr), 2)

    def test_False(self):
        pass


if __name__ == '__main__':
    unittest.main()
