# DNS

Fundamental concepts of the Domain Name System.
<!-- TOC -->

- [DNS](#dns)
  - [What](#what)
  - [How](#how)
  - [Zone Files](#zone-files)
    - [Zone Transfers](#zone-transfers)
  - [Resource Records](#resource-records)
    - [Start of Authority (SOA):](#start-of-authority-soa)
    - [A:](#a)
    - [AAAA:](#aaaa)
    - [Mail Exchanger (MX):](#mail-exchanger-mx)
    - [Name Server (NS):](#name-server-ns)
    - [Pointer (PTR):](#pointer-ptr)
    - [Canonical Name (CNAME):](#canonical-name-cname)
  - [Caching](#caching)
    - [Browsers](#browsers)
    - [Predictive Search Queries](#predictive-search-queries)
    - [OS](#os)
  - [Terms](#terms)
    - [DNS resolver](#dns-resolver)
    - [Authoritative Server](#authoritative-server)
    - [Top-level Domain (TLD)](#top-level-domain-tld)
    - [Recursive request](#recursive-request)
    - [Iterative request](#iterative-request)
    - [Non-Iterative request](#non-iterative-request)
    - [Flags](#flags)
  - [Firefox and DNS](#firefox-and-dns)

<!-- /TOC -->
## What

The DNS is a query/response protocol in which messages are sent in both directions using the same format.

## How

A graphic summary of how a DNS query takes place.

![dns-lookup](https://github.com/danielmichaels/dwiki/blob/master/images/dns-lookup-diagram.png "dns lookup diagram from cloudflare")
> fig.1 [attribution](https://www.cloudflare.com/learning/dns/what-is-dns/)

1. When the user types `example.com` into the browser and presses enter, the client machine does a lookup in its `hosts` file for a match. If no match is found it sends a request for the IP address of the website to a DNS recursive resolver.
2. The resolver, having not found the address in its cache, forwards the request to one of the DNS root name servers. Root name servers represent the "dot", or period - `'.'`.
3. Once received, the root name server looks for the top-level domain address (TLD) that matches the request - in this case; `com`. If found, it returns the `com` TLD IP address.
4. The DNS resolver then sends out a request to the `com` name server.
5. Next, the `com` name server looks up the domain name matching `example`, and returns it's address to the resolver.
6. Now the resolver can query the `example` domain name server for an IP address.
7. The server will respond with its mapped address.
8. Once received, the DNS recursive resolver sends the IP address for `example.com` to the browser, and stores it in it's cache.
9. The browser now makes a HTTP request to `example.com` via its IPv4 or IPv6 address.
10. Now the browser and the website can freely communicate using HTTP.

## Zone Files

Zone files are how a name server stores information about the domain it has authority for. Every domain that the server has authority over, will have its own zone file.

Zone files contain many different record types.


### Zone Transfers

Any transaction between name servers used to replicate databases across servers. Zone transfers are conducted using TCP over port 53 in a client-server fashion. Clients requesting the zone transfer may be slave or secondary server attempting to replicate the zone file.

Transfers start with a SOA lookup checking the serial number to determine if the transfer/replication needs to take place at all.
If the clients serial number is less than the servers serial number, it will proceed to request the actual transfer. It is a form of version control, and validation.

The first response during a zone transfer is a SOA record. All other fields are in no particular order but it will always end with another SOA.

Zone transfers are _entirely_ client initiated. A freshly raised name server will have no records and will begin its first zone transfer. Thereafter, it will continue to refresh its zone file in regular intervals as determined by the `refresh`, `retry`, and `expire` fields in the SOA resource record.

Running the following command will produce a zone transfer response from the name server. The response record types are expanded in more detail below.

`drill AXFR @nsztm1.digi.ninja zonetransfer.me`

## Resource Records

### Start of Authority (SOA):
  - Contains administrative info about a zone such as domain owner, contact details and serial number.
  - Can be of use in a audit, or give detail about the domain.
  - serial number is used to determine the currency of the zone's data, and if a zone transfer needs to be conducted at all.

```shell
drill SOA taste.com.au

>>> ;; QUESTION SECTION:
>>> ;; taste.com.au.        IN      SOA
>>>
>>> ;; ANSWER SECTION:
>>> taste.com.au.   176     IN      SOA     dns0.news.com.au. hostmaster.news.com.au. 2019060600 900 600 604800 300

```

Each tabbed section in detail:

- `IN` and `SOA`; Internet and Start of Authority.
- `dns0.news.com.au` is the primary name server.
- The email contact for the domain; `hostmaster.news.com.au` is equal to `hostmaster@news.com.au` - first `.` should be replaced by an `@` symbol.
- `2019060600` is the current serial number for the domain.
- `900` - time in seconds secondary name servers should wait between making requests for changes. Also known as the `refresh` rate. More aptly this means; how long am I willing to accept my secondary server to have out-of-date information.
- `600` refers the time it should wait before trying another `refresh` if the last one failed.
- `604800` is the `expire` counter in seconds. It lets the secondary name server know how long to hold their information for before it is no longer considered authoritative. Generally, this is a large number, and should always be greater than `refresh` and `retry` counters.
- `300` is the `minimum` time-to-live in seconds before the records in the zone are considered invalid.


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
This adds latency to the request as another round trip must be conducted.

## Caching

### Browsers

To increase efficency by reducing the number of lookups, browsers such as Chrome, and Firefox cache DNS data.

### Predictive Search Queries

example of dns lookups via googles predictive search

### OS

OS level cache

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

This can be seen via `drill -T taste.com.au` which will trace (what `-T` does) through each root name server all the way to the A record of `taste.com.au`.


### Recursive request

When the needs to get the address for a URL, it first checks its cache, then if not found will send a request to its recursive resolver asking for the address. In most cases the resolver being queried will be an ISP default (please don't do this; they monetize it), or something like Google's public DNS server; `8.8.8.8`. Sidenote: use `1.1.1.1` or some other provider - google are using you, too.

The recursive resolver will then begin a series of iterative requests out to the root name servers.

For the most part recursive queries begin with the client and end at the recursive resolver in a kind of A->B, B->A relationship. Some instances, such as private DNS in large organisations may have several recursive queries out the requested resource. This is due to the authoritative nature of such setups.

### Iterative request

Generally, the queries from a recursive resolver are iterative. They leave the resolver and start at the top of the DNS tree via the root name servers. The root replies with the appropriate domains name server. The resolver then makes another query to that server. The iterations continue down the hierarchy until an address is resolved.

### Non-Iterative request

When a query is made and the resolver has the address mapping in its cache, it will refer the client immediately to it. No further queries are made and this is known as a non-iterative request.


### Flags

[more info](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-12)
- `aa` Authoritative Answer
- `tc` Truncated Response
- `rd` Recursion Desired
- `ra` Recursion Available
- `ad` Authentic Data
- `cd` Checking Disabled

## Firefox and DNS

Today I learnt that my firefox DNS is overriding my pfBlockerNG settings. How, I am not sure but its been driving me crazy.

In `about:config` I had set `network.trr:2` and this had created a DNS-over-HTTPS connection for all DNS queries coming from Firefox. I posit that my pfSense firewall is not filtering the DNS traffic through itself and therefore blocking ads because it cannot inspect the HTTPS traffic and see that it is DNS.

My thoughts on DoH were that its a shamble, and thats been solidified here. In an attempt to make my DNS queries private, they have exposed me to potentially malicious ads - monetising me all the way. Its my fault for turning on `network.trr` without fully understanding the repercussions.

ADD the TRR codes and how to disable it.
