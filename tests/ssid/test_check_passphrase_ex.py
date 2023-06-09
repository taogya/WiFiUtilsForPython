
import unittest

from wifi_utils import ssid


class Test(unittest.TestCase):

    def test_True(self):
        self.assertTrue(ssid.check_passphrase_ex('0' * 5 + 'a' + 'A' + '!'))
        self.assertTrue(ssid.check_passphrase_ex('0' + 'a' * 5 + 'A' + '!'))
        self.assertTrue(ssid.check_passphrase_ex('0' + 'a' + 'A' * 5 + '!'))
        self.assertTrue(ssid.check_passphrase_ex('0' + 'a' + 'A' + '!' * 5))

    def test_False(self):
        self.assertFalse(ssid.check_passphrase_ex('0' * 0 + 'a' + 'A' + '!' + 'a' * 5))
        self.assertFalse(ssid.check_passphrase_ex('0' + 'a' * 0 + 'A' + '!' + '0' * 5))
        self.assertFalse(ssid.check_passphrase_ex('0' + 'a' + 'A' * 0 + '!' + '0' * 5))
        self.assertFalse(ssid.check_passphrase_ex('0' + 'a' + 'A' + '!' * 0 + '0' * 5))


if __name__ == '__main__':
    unittest.main()
