
import unittest

from wifi_utils import mac_addr


class Test(unittest.TestCase):

    def test_True(self):
        self.assertTrue(mac_addr.check_mac_addr('00:00:00:00:00:00'))
        self.assertTrue(mac_addr.check_mac_addr('ff:ff:ff:ff:ff:ff'))
        self.assertTrue(mac_addr.check_mac_addr('FF:FF:FF:FF:FF:FF'))
        self.assertTrue(mac_addr.check_mac_addr('000000000000', delimiter=''))
        self.assertTrue(mac_addr.check_mac_addr('00-00-00-00-00-00', delimiter='-'))

    def test_False(self):
        self.assertFalse(mac_addr.check_mac_addr(''))
        self.assertFalse(mac_addr.check_mac_addr('000000000000'))
        self.assertFalse(mac_addr.check_mac_addr('0:00:00:00:00:00'))
        self.assertFalse(mac_addr.check_mac_addr('00:0:00:00:00:00'))
        self.assertFalse(mac_addr.check_mac_addr('00:00:0:00:00:00'))
        self.assertFalse(mac_addr.check_mac_addr('00:00:00:0:00:00'))
        self.assertFalse(mac_addr.check_mac_addr('00:00:00:00:0:00'))
        self.assertFalse(mac_addr.check_mac_addr('00:00:00:00:00:0'))
        self.assertFalse(mac_addr.check_mac_addr('gg:gg:gg:gg:gg:gg'))
        self.assertFalse(mac_addr.check_mac_addr('GG:GG:GG:GG:GG:GG'))
        self.assertFalse(mac_addr.check_mac_addr('00-00-00-00-00-00'))


if __name__ == '__main__':
    unittest.main()
