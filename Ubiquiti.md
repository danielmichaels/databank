# Ubiquiti 

A collection of notes regarding Ubiquiti products

## Unifi

- Unifi gear is fantastic and comes with its own dashboard. However, the UAC-PRO WAP's are fickle at times. The connection can get flaky.
- A cloud controller is required for the management of the WAP's
- Cloud Key is 200 bucks and takes a spot in the switch but is a solid manager option. Otherwise they can be hosted in a VM on a server.

## EdgeMax

- Not compatible with Unifi - it won't show up in the Unifi cloud dashboard. I did not realise this until after I purchased it, however the switch is very capable.
- Must be managed separately from the Unifi gear
- SSH, HTTP, HTTP/S and Telnet methods to configure. USB to DB9 for serial link configuration available.
- Initial setup defaults to DHCP or fallback to 192.168.1.2.
