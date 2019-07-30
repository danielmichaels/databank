# pfBlockerNG

_as at 14 June 2019_

## Testing Functionality

The tale of two pings

```
# Ping 1 -> pfsense.org

PING pfsense.org (208.123.73.69) 56(84) bytes of data.
64 bytes from www.pfsense.org (208.123.73.69): icmp_seq=1 ttl=51 time=199 ms
64 bytes from www.pfsense.org (208.123.73.69): icmp_seq=2 ttl=51 time=201 ms
64 bytes from www.pfsense.org (208.123.73.69): icmp_seq=3 ttl=51 time=201 ms

--- pfsense.org ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 5ms
rtt min/avg/max/mdev = 199.398/200.597/201.336/0.999 ms

```

Ping 1 returns the IP address of the domain

```
# Ping 2 -> analytics.yahoo.com

PING analytics.yahoo.com (10.10.10.1) 56(84) bytes of data.
64 bytes from 10.10.10.1 (10.10.10.1): icmp_seq=1 ttl=64 time=0.748 ms
64 bytes from 10.10.10.1 (10.10.10.1): icmp_seq=2 ttl=64 time=1.07 ms
64 bytes from 10.10.10.1 (10.10.10.1): icmp_seq=3 ttl=64 time=2.47 ms

--- analytics.yahoo.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 5ms
rtt min/avg/max/mdev = 0.748/1.427/2.467/0.747 ms
```

Ping 2 returns a RFC 1918 address. Why? Because pfBlockerNG has this domain in its block list, and automatically routes it via its own address thereby sinkholing it.

