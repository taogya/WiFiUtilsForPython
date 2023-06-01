
from wifi_utils import ssid

my_ssid = 'raspberrypi-ssid'
my_pass = 'Raspberrypi-pass0001'

print('check ssid -> ' + f'{ssid.check_ssid(my_ssid)}')
print('check pass -> ' + f'{ssid.check_passphrase(my_pass)}')
print('check pass_ex -> ' + f'{ssid.check_passphrase_ex(my_pass)}')

print('create pass -> ' + ssid.create_passphrase(13))
print('create pass_ex -> ' + ssid.create_passphrase_ex(13))
