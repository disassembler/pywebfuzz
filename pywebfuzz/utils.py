#!/usr/bin/env python

""" This is the fuzzutils package. This contains useful items for performing
your fuzzing tasks agaist web applications

(c) 2010 Nathan Hamiel
Email: nathan{at}neohaxor{dot}org
Hexsec Labs: http://hexsec.com/labs

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

import urllib
import urllib2

def make_request(location, method="GET", postdata=None, headers=None):
    """ This provides a convenience function for making requests. This interfaces
    with urllib2 and provides the ability to make GET and POST requests for content.
    The return data from this function is headers and content"""
    
    # Checks to ensure that if it is a POST request that postdata is present
    # I may remove this because it could potentially be a valid test case w/o data
    if method == "POST" and postdata == None:
        print("You did not specify any associated postdata and this is a POST request")
        sys.exit(1)
    
    # Checks to ensure that header values and postdata are in the appropriate format
    if type(headers) != dict and headers != None:
        raise TypeError, ("headers are not a valid Python dictionary")
    if type(postdata) != str and postdata != None:
        raise TypeError, ("postdata is not a valid Python string")
    
    ####
    # Todo: Add support for more HTTP methods
    ####
    
    # Takes the appropriate actions based on the request type
    if method == "GET":
        if headers:
            req = urllib2.Request(location, headers=headers)
        else:
            req = urllib2.Request(location)
            
        response = urllib2.urlopen(req)
        
        headers = response.info()
        content = response.read()
        return(headers, content)
        
    elif method == "POST":
        if headers:
            req = urllib2.Request(location, headers=headers)
        else:
            req = urllib2.Request(location)
            
        req.add_data(postdata)

        response = urllib2.urlopen(req)
        headers = response.info()
        content = response.read()
        return(headers, content)
        
    else:
        print("Invalid method for make_request function")
    
def generate_range(start, stop, step=1, pre=None, post=None):
    """ Generate a range of values with optional stepping. Chars can be prepended or attached to
    the end of each value that is generated. """
    
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