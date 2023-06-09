
import random
import re

MAC_ADDR_BITS = 48
MAC_ADDR_BYTES = int(MAC_ADDR_BITS / 8)


def check_mac_addr(mac_addr: str, delimiter=':') -> bool:
    """check format of mac address

    Args:
        mac_addr (str): target
        delimiter (str, optional): delimiter. Defaults to ':'.

    Returns:
        bool:
            "True" matches pattern.
    """
    res = re.match(r'^([0-9a-fA-F]{{2}}{delimiter}){{5}}[0-9a-fA-F]{{2}}$'.format(delimiter=delimiter),
                   mac_addr)
    return res is not None


def create_mac_addr(delimiter=':') -> str:
    """create mac address

    Args:
        delimiter (str, optional): delimiter string. Defaults to ':'.

    Returns:
        str: mac address
    """
    addr = [f'{random.randint(0, 255):02x}' for _ in range(MAC_ADDR_BYTES)]
    ret = delimiter.join(random.sample(addr, MAC_ADDR_BYTES))

    return ret
