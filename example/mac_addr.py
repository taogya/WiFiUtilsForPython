
from wifi_utils import mac_addr

my_mac_addr = mac_addr.create_mac_addr()

print('mac addr -> ' + f'{my_mac_addr}, {mac_addr.check_mac_addr(my_mac_addr)}')
