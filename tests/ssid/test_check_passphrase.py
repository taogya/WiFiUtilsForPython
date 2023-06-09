
import unittest

from wifi_utils import ssid


class Test(unittest.TestCase):

    def test_True(self):
        self.assertTrue(ssid.check_passphrase('0' * 8))
        self.assertTrue(ssid.check_passphrase('0' * 32))
        for c in '0123456789':
            self.assertTrue(ssid.check_passphrase(c * 8))
        for c in 'abcdefghijklmnopqrstuvwxyz':
            self.assertTrue(ssid.check_passphrase(c * 8))
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.assertTrue(ssid.check_passphrase(c * 8))
        for c in '@#%&/|:;!"\',=~_<>[](){}^$?.+*-\\':
            self.assertTrue(ssid.check_passphrase(c * 8))

    def test_False(self):
        self.assertFalse(ssid.check_passphrase('0' * 7))
        self.assertFalse(ssid.check_passphrase('0' * 64))
        for c in '\n\t\r\b\0':
            self.assertFalse(ssid.check_passphrase(c))
        for c in 'あアｱ ':
            self.assertFalse(ssid.check_passphrase(c))


if __name__ == '__main__':
    unittest.main()
