import hashlib


def md5_convert(line):
    md5 = hashlib.md5(line.encode())
    return md5.hexdigest()
