# WebCrab

This tool collects HTTP responses for use by the DShield honeypot. You will first create a JSON file describing the requests. A small sample file is included. The following elements are required for each request:
- scheme: The scheme (http or https)
- host: The host name to connect to
- url: The URL to request (without hostname)
- method: One of the HTTP verbs (GET/POST...)
- comment: Describe the request so we know what it attempts to emulate

Optional parameters:
- headers: a dictionary with one or more headers.
- body: the body of the request
- port: the port number, if a port other than the default port is being used

To use "WebCrab", pass two parameters:

- request file: the JSON file you created with request data
- response file: this is the file name used to save the responses. The current timestamp will be appended to avoid overwriting prior files.

## Example: 

```./webcrab.py requests.json responses.json```

