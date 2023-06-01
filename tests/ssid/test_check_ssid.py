
import unittest

from wifi_utils import ssid


class TestCheckSsid(unittest.TestCase):

    def test_False(self):
        self.assertFalse(ssid.check_ssid('0' * 0))
        self.assertFalse(ssid.check_ssid('0' * 33))
        for c in '^\\@[;:],./!"#$%&\'()=~|`{+*}<>?':
            self.assertFalse(ssid.check_ssid(c))
        for c in '\n\t\r\b\0':
            self.assertFalse(ssid.check_ssid(c))
        for c in 'あアｱ':
            self.assertFalse(ssid.check_ssid(c))

    def test_True(self):
        self.assertTrue(ssid.check_ssid('0' * 1))
        self.assertTrue(ssid.check_ssid('0' * 32))
        for c in '0123456789':
            self.assertTrue(ssid.check_ssid(c))
        for c in 'abcdefghijklmnopqrstuvwxyz':
            self.assertTrue(ssid.check_ssid(c))
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.assertTrue(ssid.check_ssid(c))
        for c in '-_':
            self.assertTrue(ssid.check_ssid(c))


if __name__ == '__main__':
    unittest.main()
