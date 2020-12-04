def passHash(s,p):
    salt = 'dsahdjsdkashdqo8382jhdajks'
    final_p = ''
    for i in p:
        final_p += chr(ord(i)+len(salt))
    for i in salt:
        final_p += chr(ord(i)+len(p)) 
    for i in s :
        final_p += chr(ord(i)+len(salt)+len(p)) + chr(ord(i)+len(salt))
    return final_p

def unhashpass(s,p):
    salt = 'dsahdjsdkashdqo8382jhdajks'
    z = p[0:len(p)-len(salt)-2*len(s)]
    passV = ''
    for i in z:
        passV += chr(ord(i)-len(salt))
    return passV    