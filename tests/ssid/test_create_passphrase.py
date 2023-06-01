
import unittest

from wifi_utils import ssid


class TestCheckSsid(unittest.TestCase):

    def test_True(self):
        res = ssid.create_passphrase(8)
        print(res)
        self.assertEqual(len(res), 8)

        res = ssid.create_passphrase(63)
        print(res)
        self.assertEqual(len(res), 63)

    def test_False(self):
        with self.assertRaises(ValueError):
            ssid.create_passphrase(7)
        with self.assertRaises(ValueError):
            ssid.create_passphrase(64)


if __name__ == '__main__':
    unittest.main()
