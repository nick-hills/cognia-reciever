#!/usr/bin/python

import config

def main():
    get_data('/2.0/license', config.AccessKey, config.SecretKey)


def get_data(endpoint, ak, sk):

    import urllib2, json, hashlib, base64, datetime, time, hmac
    from email import utils

    url = 'https://api.cognia.com'+endpoint
    payload = {''} 
    data=''
    req = urllib2.Request(url)

    bodyMD5 = hashlib.md5("").hexdigest()
    base64BodyMD5 = base64.b64encode(bodyMD5)
    req.add_header("Content-MD5", base64BodyMD5)
    reqContentType = "application/json"
    req.add_header("Content-Type", reqContentType)
    
    nowdt = datetime.datetime.now()
    nowtuple = nowdt.timetuple()
    nowtimestamp = time.mktime(nowtuple)
    reqDate = utils.formatdate(nowtimestamp, usegmt=True)
    req.add_header("x-cognia-date", reqDate)

    reqMethod = req.get_method()
    reqPath = req.get_selector()

    digestMaker = hmac.new(sk, '', hashlib.sha1)
    reqHmacString = reqMethod + '\n' + base64BodyMD5 + '\n' + reqContentType + '\n' + reqDate + '\n' + reqPath + '\n'

    digestMaker.update(reqHmacString)
    reqHmac = base64.b64encode(digestMaker.digest())
    authHeader = "COGNIA:" + ak + ":" + reqHmac
    req.add_header("Authorization", authHeader)

    handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler)
    try:
        connection = opener.open(req)
    except urllib2.HTTPError,e:
        connection = e

    if 200 <= connection.code <= 207:
        print connection.read()
    else:
        print 'Error fetching data. code=' + str(connection.code)


def decrypt_rsa(encryptedBytes):
   
    import crypto
    import sys
    sys.modules['Crypto'] = crypto
    from Crypto.PublicKey import RSA
    from base64 import b64decode

    key = open('./key.pem', "r").read()
    rsakey = RSA.importKey(key)
    
    raw_cipher_data = b64decode(encryptedBytes)
    decrypted = rsakey.decrypt(raw_cipher_data)
    return pkcs1_unpad(decrypted)



def pkcs1_unpad(text): 
    #remove padding from decrypted bytes
    if len(text) > 0 and text[0] == '\x02': 
        # Find end of padding marked by nul 
        pos = text.find('\x00') 
        if pos > 0: 
            return text[pos+1:] 
    return None

main()


