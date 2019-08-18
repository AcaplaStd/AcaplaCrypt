def b64_to_random(b64: str):
    res = ""
    for i in b64:
        if 65 <= ord(i) <= 90:
            res += chr(ord(i) + 1007)
        elif 97 <= ord(i) <= 103:
            res += chr(ord(i) + 1001)
        elif 104 <= ord(i) <= 110:
            res += chr(ord(i) - 13)
        elif 111 <= ord(i) <= 114:
            res += chr(ord(i) - 12)
        elif 114 <= ord(i) <= 115:
            res += chr(ord(i) - 56)
        elif 116 <= ord(i) <= 122:
            res += chr(ord(i) - 83)
        else:
            res += i
    return res


def random_to_b64(random: str):
    res = ""
    for i in random:
        if 1072 <= ord(i) <= 1097:
            res += chr(ord(i) - 1007)
        elif 1098 <= ord(i) <= 1104:
            res += chr(ord(i) - 1001)
        elif 91 <= ord(i) <= 97:
            res += chr(ord(i) + 13)
        elif 99 <= ord(i) <= 102:
            res += chr(ord(i) + 12)
        elif 58 <= ord(i) <= 59:
            res += chr(ord(i) + 56)
        elif 33 <= ord(i) <= 39:
            res += chr(ord(i) + 83)
        else:
            res += i
    return res
