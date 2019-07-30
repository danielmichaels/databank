# pfSense DNS

Some tips and tricks learnt along the way.

## Forward all requests via DNS-over-TLS (DoT)

In general it is a good idea to force all DNS requests within your network to use the firewall. Many embedded devices will hardcode DNS, or have their own resolver running in an attempt to circumvent your system defences. Egregiously, this is done by many Google devices in an attempt to serve you ads (hello YouTube). We can stop that, as the fallback on these devices once their resolver fails will be the DNS address handed to it via DHCP.

Netgate provides the following guide, [here](https://docs.netgate.com/pfsense/en/latest/dns/redirecting-all-dns-requests-to-pfsense.html) which walks you through how to set it up.

This can be validated by first setting the Advanced settings Log Level to 3 or 4. Then in the "Status" bar on the upper right corner, the logging can be accessed. The button bar as seen below. 

![Buttons](https://github.com/danielmichaels/dwiki/blob/master/images/pfsenseButtons.png?raw=true "pfSense button menu")
Hovering over the buttons will detail their usage.

By default unbound's DNS Cache is set to a 15 minute TTL.

## DNS LAN Name resolution

To ensure the LAN DHCP sends out the local domain you must check:

- [X] Register DHCP leases in the DNS Resolver
- [X] Register DHCP static mappings in the DNS resolver (optional)
- [X] Register connected OpenVPN clients in DNS Resolver (optional)
