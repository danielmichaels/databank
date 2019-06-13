# DNS

Fundamental concepts of the Domain Name System.

## What

The DNS is a query/response protocol in which messages are sent in both directions using the same format. 

## How

A graphic summary of how a DNS query takes place.

![dns-lookup](https://github.com/danielmichaels/dwiki/blob/master/images/dns-lookup-diagram.png "dns lookup diagram from cloudflare")
> fig.1 [attribution](https://www.cloudflare.com/learning/dns/what-is-dns/)

1. When the user types `example.com` into the browser and presses enter, the client machine does a lookup in its `hosts` table for a match. If no match is found it sends a request for the IP address of the website to a DNS recursive resolver.
2. The resolver, having not found the address in its cache, forwards the request to one of the DNS root name servers. Root name servers represent the "dot", or period - `'.'`.
3. Once received, the root name server looks for the top-level domain address that matches the request - in this case; `com`. If found, it returns the `com` TLD IP address.
4. The DNS resolver then sends out another request to the `com` name server.
5. Next the `com` name server looks up the domain name server address matching `example`, and returns it to the resolver.
6. Now the resolver can query the `example` domain name server for an IP address.
7. If `example.com` exists, the server will respond with its mapped address.
8. Once received, the DNS recursive resolver sends the IP address for `example.com` to the browser.
9. The browser now makes a HTTP request to `example.com` via its IPv4 or IPv6 address.
10. Now the browser and the website can freely communicate using HTTP.

## Resource Records

### Start of Authority (SOA):
  - Contains administrative info about a zone such as domain owner, contact details and serial number.
### A:
  - IPv4 address associated to domain name.
### AAAA:
  - IPv6 address association.
### Mail Exchanger (MX):
  - Mail exchanger records containing the emails associated to the domain.
### Name Server (NS):
  - A list of name servers connected to the domain.
### Pointer (PTR):
  - Pointer file for reverse DNS lookups
### Canonical Name (CNAME):
  - Some domains will have alias' such as `www.example.com` might be an alias of `example.com`. The CNAME record tells the resolver to start another query for that name.
   
DNS zone file that reads:

```shell
   NAME                    TYPE   VALUE
--------------------------------------------------
bar.example.com.        CNAME  foo.example.com.
foo.example.com.        A      192.0.2.23
   
```
This should be read as:

> `bar.example.com.` is an alias for the CNAME `foo.example.com.`. A client request for `bar.example.com.` will be returned `foo.example.com.`

The next query to the `example` domain will be asking for `foo.`. It will then be returned an `A` record with address `192.0.2.23`.

## Terms

### DNS resolver

The 'resolver' is the agent between the client and the name servers. A resolver will start the queries that eventually return a valid address translation for the client.

A recursive resolver knows how to traverse the tree to deliver a response to a query.

### Authoritative Server

Owns the domain, or has all the records for that domain.

### Top-level Domain (TLD)

Domains that are one level below the root are known as top level domains. 

- Examples:
  `com`, `jp`, `edu`  

Country Code TLD's such as `au` eg. `taste.com.au` will be resolved in the following order:

1. Root - `.`
2. -> `.au`
3. -> `com.au`
4. -> `taste.com.au`


### Recursive request

### Iterative request

### Non-Iterative request

