
from wifi_utils import ssid

my_ssid = 'raspberrypi-ssid'
my_pass = 'Raspberrypi-pass0001'

print('check ssid -> ' + ssid.check_ssid(my_ssid))
print('check pass -> ' + ssid.check_passphrase(my_pass))
print('check pass_ex -> ' + ssid.check_passphrase_ex(my_pass))

print('create pass -> ' + ssid.create_passphrase(13))
print('create pass_ex -> ' + ssid.create_passphrase_ex(13))
