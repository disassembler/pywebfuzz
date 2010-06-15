#!/usr/bin/env python

""" This is the fuzzutils package. This contains useful items for performing
your fuzzing tasks agaist web applications """

import urllib
import urllib2
from EncoderLib import *

def make_request(location, verb="GET", postdata=None, head=None):
    """ This provides a convenience function for making requests. This interfaces
    with urllib2 and provides the ability to make GET and POST requests for content.
    The return data from this function is headers and content"""
    
    # Checks to ensure that if it is a POST request that postdata is present
    if verb == "POST" and postdata == None:
        print("You did not specify any associated postdata and this is a POST request")
        sys.exit(1)
    
    # Checks to ensure that header values and postdata are in the appropriate format
    if type(head) != dict and head != None:
        raise TypeError, ("headers are not a valid Python dictionary")
    if type(postdata) != str and postdata != None:
        raise TypeError, ("postdata is not a valid Python string")
    
    # Takes the appropriate actions based on the request type
    if verb == "GET":
        if head:
            req = urllib2.Request(location, headers=head)
        else:
            req = urllib2.Request(location)
            
        response = urllib2.urlopen(req)
        
        headers = response.info()
        content = response.read()
        return(headers, content)
        
    elif verb == "POST":
        if head:
            req = urllib2.Request(location, headers=head)
        else:
            req = urllib2.Request(location)
            
        req.add_data(postdata)

        response = urllib2.urlopen(req)
        headers = response.info()
        content = response.read()
        return(headers, content)
    
def generate_range(start, stop, step=1, pre=None, post=None):
    """ Generate a range of values with optional stepping as well as chars prepended or attached to
    the end of each value that is generated """
    
    rangevals = range(start, stop, step)
    values = []
    
    try:
        if pre and post:
            for item in rangevals:
                values.append(pre + str(item) + post)
            return(values)
        elif pre:
            for item in rangevals:
                values.append(pre + str(item))
            return(values)
        elif post:
            for item in rangevals:
                values.append(str(item) + post)
            return(values)
        else:
            for item in rangevals:
                values.append(str(item))
            return(values)
    except:
        print("You did not specify all of the values necessary for this function")