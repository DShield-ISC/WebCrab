#!/usr/bin/env python3

"""
quick script to collect responses from a web server
to be copied to the DShield honeypot
"""

import requests
import sys
import json
import time

def jsonfy(resp,comment):
    """
    create a json version of the response compatible with the
    dshield honeypot
    """
    jresp={}
    jresp['id']=0
    jresp['headers']=dict(resp.headers)
    jresp['comment']=comment
    jresp['status_code']=resp.status_code
    jresp['body']=resp.text
    return(json.dumps(dict(jresp), indent=2))

def sendrequest(r):
    """
    send the request to the webserver
    """
    required=['host','host','url','method','comment','scheme']
    for x in required:
        if x not in r:
            print(f"Missing required parameter {x} in request. \n\n{r}")
            sys.exit()

    if 'headers' not in 'r':
        r['headers']={}
    if 'body' not in 'r':
        r['body']=''
    if 'port' in 'r':        
        url = r['scheme']+'://'+r['host']+':'+r['port']+r['url']
    else:
        url = r['scheme']+'://'+r['host']+r['url']
    print(f"Requesting {url}")
    response = requests.request(r['method'],url, headers=r['headers'], data=r['body'])
    return(response)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: webcrab.py [request file] [response file]")
        sys.exit()
    requestfile = sys.argv[1]
    resultfile = sys.argv[2] + "." + str(int(time.time()))
    try:
        f = open(requestfile)
    except FileNotFoundError:
        print(f"Can not find {requestfile}")
        sys.exit()
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError:
        print(f"Error parsing '{requestfile}'")
        sys.exit()
    f.close()
    f = open(resultfile,'a')    
    for r in data:
        response = sendrequest(r)
        f.write(jsonfy(response,r['comment']))
    f.close()
        
    
