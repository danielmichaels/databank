# DNS

Fundamental concepts of the Domain Name System.

## What

The DNS is a query/response protocol in which messages are sent in both directions using the same format. 

## How

A graphic summary of how a DNS query takes place.

![dns-lookup](https://github.com/danielmichaels/dwiki/blob/master/images/pdns-lookup-diagram.png "dns lookup diagram from cloudflare")
1. When the user types `example.com` into the browser and presses enter, the client machine sends a request for that IP address of the website to a DNS recursive resolver.
2. The resolver, having not found the address in its cache, forwards the request to one of the DNS root name servers. Root name servers represent the "dot", or period - '.'.
3. Once received, the root name server looks for the top-level domain address that matches the request - in this case; `com`. If found, it returns the `com` TLD IP address.
4. The DNS resolver then sends out another request to the `com` name server.
5. Next the `com` name server looks up the domain name server address matching `example`, and returns it to the resolver.
6. Now the resolver can query `example.com` for its IP address.
7. If `example.com` exists, the server will respond with its address.
8. Once received, the DNS recursive resolver sends the IP address for `example.com` to the browser.
9. The browser now makes a HTTP request to `example.com` via its IPv4 or IPv6 address.
10. Now the browser and the website can freely communicate using HTTP.

## Terms

### DNS resolver

The 'resolver' is the agent between the client and the name servers that have the IP address of the domain being queried. A resolver will start the queries that eventually returns a valid address translation for the client.
A recursive resolver knows how to traverse the tree to deliver a response to a query.

### Authoritative Server

- Owns the domain, or has all the records for that domain.

### Top-level Domain (TLD)

### Recursive request

### Iterative request

### Non-Iterative request

