
import random
import re


def check_ssid(ssid: str) -> bool:
    """check ssid pattern.

    Args:
        ssid (str): target

    Returns:
        bool:
            "True" matches pattern.
            Pattern is "^[0-9a-zA-Z-_]{1,32}$".

    """
    res = re.match(r'^[0-9a-zA-Z-_]{1,32}$',
                   ssid)
    return res is not None


def check_passphrase(passphrase: str) -> bool:
    """check passphrase pattern.

    Args:
        passphrase (str): target

    Returns:
        bool:
            "True" matches pattern.
            Pattern is "^[0-9a-zA-Z@#%&/|:;!"',=~_<>\\\\[\\\\]\\\\(\\\\)\\\\{\\\\}\\\\^\\\\$\\\\?\\\\.\\\\+\\\\*\\\\-\\\\]{8,63}$".
    """
    res = re.match(r'^[0-9a-zA-Z@#%&/|:;!"\',=~_<>\[\]\(\)\{\}\^\$\?\.\+\*\-\\]{8,63}$',
                   passphrase)
    return res is not None


def create_passphrase(length: int = 8) -> str:
    """create passphrase.

    Args:
        length (int, optional): passphrase length(8 <= length <= 63). Defaults to 8.

    Raises:
        ValueError: not 8 <= length <= 63.

    Returns:
        str:
            passphrase is: specified length.
    """
    if length < 8 or 63 < length:
        raise ValueError(f'not 8 <= length <= 63. -> args: {length}')

    res = random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                         + 'abcdefghijklmnopqrstuvwxyz'
                         + '0123456789'
                         + '@#%&/|:;!"\',=~_<>[](){}^$?.+*-\\', k=length)
    res = ''.join(res)
    return res


def check_passphrase_ex(passphrase: str) -> bool:
    """check passphrase pattern. (with uppercase, lowercase, numbers, symbols)

    Args:
        passphrase (str): target

    Returns:
        bool:
            "True" matches pattern.
            Pattern is "^[0-9a-zA-Z@#%&/|:;!"',=~_<>\\\\[\\\\]\\\\(\\\\)\\\\{\\\\}\\\\^\\\\$\\\\?\\\\.\\\\+\\\\*\\\\-\\\\]{8,63}$".
                and include uppercase strings at least one.
                and include lowercase strings at least one.
                and include numbers at least one.
                and include symbols at least one.
    """
    res = check_passphrase(passphrase)
    res_ex = re.match(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#%&/|:;!"\',=~_<>\[\]\(\)\{\}\^\$\?\.\+\*\-\\]).+$',
                      passphrase)
    return (res is not None) and (res_ex is not None)


def create_passphrase_ex(length: int = 8) -> str:
    """create passphrase. (with uppercase, lowercase, numbers, symbols)

    Args:
        length (int, optional): passphrase length(8 <= length <= 63). Defaults to 8.

    Raises:
        ValueError: not 8 <= length <= 63.

    Returns:
        str:
            passphrase is:
                specified length.
                include uppercase strings at least one.
                include lowercase strings at least one.
                include numbers at least one.
                include symbols at least one.
    """
    if length < 8 or 63 < length:
        raise ValueError(f'not 8 <= length <= 63. -> args: {length}')

    uc = random.randint(1, length - 3)
    lc = random.randint(1, length - uc - 2)
    nm = random.randint(1, length - uc - lc - 1)
    sb = length - uc - lc - nm
    res = random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=uc)\
        + random.choices('abcdefghijklmnopqrstuvwxyz', k=lc)\
        + random.choices('0123456789', k=nm)\
        + random.choices('@#%&/|:;!"\',=~_<>[](){}^$?.+*-\\', k=sb)
    res = ''.join(random.sample(res, len(res)))
    return res
