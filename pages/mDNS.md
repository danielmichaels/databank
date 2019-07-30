# mDNS

Multicast Domain Name System [RFC6762]

TLDR: Clients performing DNS-like queries for DNS-like resource records by sending DNS-like UDP query and response messages over IP Multicast to UDP port 5353

## Mechanisms

Multicast DNS allows devices to establish a connection over a local network without DHCP or DNS support. It is analogous to IPv4 addresses in the 169.254/16, or IPv6 FE80::/10 prefix, which are link local and only accessible via the link they originate from.

Any DNS query with a ".local" MUST be sent to the mDNS link-local multicast address of 224.0.0.1, or the IPv6 equivalent; FF02::FB.



