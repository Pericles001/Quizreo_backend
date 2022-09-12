import this

from cryptography.fernet import Fernet

key = Fernet.generate_key()


def encrypt_str(target):
    """
    Method that encrypt a given string
    :param target:
    :return:
    """
    return Fernet(key).encrypt(target.encode(encoding='UTF-8', errors='strict'))


def decrypt_str(target):
    """
    Method that decrypt a given string
    :param target:
    :return:
    """
    return Fernet(key).decrypt(target).decode(encoding='UTF-8', errors='strict')
