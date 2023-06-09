
import unittest

from wifi_utils import ssid


class Test(unittest.TestCase):

    def test_True(self):
        res = ssid.create_passphrase_ex(8)
        print(res)
        self.assertEqual(len(res), 8)
        self.assertTrue(ssid.check_passphrase_ex(res))

        res = ssid.create_passphrase_ex(63)
        print(res)
        self.assertEqual(len(res), 63)
        self.assertTrue(ssid.check_passphrase_ex(res))

    def test_False(self):
        with self.assertRaises(ValueError):
            ssid.create_passphrase_ex(7)
        with self.assertRaises(ValueError):
            ssid.create_passphrase_ex(64)


if __name__ == '__main__':
    unittest.main()
