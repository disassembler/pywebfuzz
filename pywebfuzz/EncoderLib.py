#!/usr/bin/env python

# This is the functions collection for DharmaEncoder

import urllib
import hashlib
import cgi
import StringIO
import zlib
import decimal
from xml.sax.saxutils import unescape
from xml.sax.saxutils import escape

###################
# Encoder section #
###################

def url_encode(encvalue):
    """ URL encode the value """
    
    try:
        encoded_value = urllib.quote(encvalue)
    except:
        encoded_value = "There was a problem with the specified value"
    return(encoded_value)
    
def full_url_encode(encvalue):
    """ Full URL Hex encode """
    
    hexval = ""
    
    for item in encvalue:
        val = hex(ord(item)).replace("0x", "%")
        hexval += val
        
    return(hexval)

def base64_encode(encvalue):
    """ Base64 encode value """
    
    try:
        basedata = encvalue.encode("Base64")
    except:
        basedata = "There was an error"
    
    return(basedata)
    
def html_entity_encode(encvalue):
    """ Encode using HTML entities """
    
    encoded_value = cgi.escape(encvalue)
    
    return(encoded_value)

def hex_encode(encvalue):
    """ Encode using Hex """
    
    hexval = ""
    
    for item in encvalue:
        val = hex(ord(item)).strip("0x")
        hexval += val
        
    return(hexval)
    
def hex_entity_encode(encvalue):
    """ Encode Hex entitiy """
    
    hexval = ""
    
    for item in encvalue:
        val = hex(ord(item)).replace("0x", "&#x") + ";"
        hexval += val
        
    return(hexval)
    
def unicode_encode(encvalue):
    """ Unicode encode """
    
    hexval = ""
    
    for item in encvalue:
        val = hex(ord(item)).replace("0x", "%u00")
        hexval += val
        
    return(hexval)
    
def escape_xml(encvalue):
    """ Escape HTML/XML """
    
    # escaped = escape(decvalue, {"&apos;": "'", "&quot;": '"'})
    escaped = escape(encvalue, {"'": "&apos;", '"': "&quot;"})
    
    return(escaped)
    
def md5_hash(encvalue):
    """ md5 hash value """
    
    hashdata = hashlib.md5(encvalue).hexdigest()
    
    return(hashdata)
    
def sha1_hash(encvalue):
    """ sha1 hash value """
    
    hashdata = hashlib.sha1(encvalue).hexdigest()
    
    return(hashdata)
    
def sqlchar_encode(encvalue):
    """ SQL char encode """
    
    charstring = ""
    
    for item in encvalue:
        val = "CHAR(" + str(ord(item)) + ")+"
        charstring += val
    
    return(charstring.rstrip("+"))
    
def decimal_convert(encvalue):
    """ Convert input to decimal value """
    
    decvalue = ""
    
    for item in encvalue:
        decvalue += str(ord(item))
    
    return(decvalue)

def decimal_entity_encode(encvalue):
    """ Convert input to decimal entity """
    
    decvalue = ""
    
    for item in encvalue:
        decvalue += "&#" + str(ord(item)) +";"
        
    return(decvalue)

def rot13_encode(encvalue):
    """ Perform ROT13 encoding on the value """
    
    return(encvalue.encode("rot13"))

###################
# Decoder section #
###################

def url_decode(decvalue):
    """ URL Decode the data """
    
    returnval = urllib.unquote(decvalue)
    
    return(returnval)
    
def fullurl_decode(decvalue):
    """ Full URL decode """
    
    splithex = decvalue.split("%")
    hexdec = ""
    for item in splithex:
        if item != "":
            hexdec += chr(int(item, 16))
            
    return(hexdec)
    
def base64_decode(decvalue):
    """ Base64 decode """
    
    msg = """ There was an error. Most likely this isn't a valid Base64 value
    and Python choked on it """
    
    try:
        base64dec = decvalue.decode("Base64")
        return(base64dec)
    except:
        return(msg)

def hex_decode(decvalue):
    """ Decode Hex """
    
    msg = """ There was an error, perhaps an invalid length for the hex
    value """
    
    try:
        decodeval = decvalue.decode("hex")
        return(decodeval)
    except:
        return(msg)
        
def hexentity_decode(decvalue):
    """ Hex entity decode """
    
    charval = ""
    splithex = decvalue.split(";")
    
    for item in splithex:
        # Necessary because split creates an empty "" that tries to be
        # converted with int()
        if item != "":
            hexcon = item.replace("&#", "0")
            charcon = chr(int(hexcon, 16))
            charval += charcon
        else:
            pass
    
    return(charval)

def unescape_xml(decvalue):
    """ Unescape HTML and XML """
    
    unescaped = unescape(decvalue, {"&apos;": "'", "&quot;": '"'})
    
    return(unescaped)
    
def unicode_decode(decvalue):
    """ Unicode decode value """
    
    charval = ""
    splithex = decvalue.split("%u00")
    
    for item in splithex:
        if item != "":
            hexcon = item.replace("%u00", "0")
            charcon = chr(int(hexcon, 16))
            charval += charcon
        else:
            pass
        
    return(charval)
    
def decimal_decode(decvalue):
    """ Decimal value decode """
    
    charval = ""
    
    for item in decvalue:
        charval += chr(int(item))
        
    print(chr(int(decvalue)))        
    return(charval)
    
def rot13_decode(decvalue):
    """ Decode ROT13 value """
    
    return(decvalue.decode("rot13"))
            
    