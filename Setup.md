# Setup

Notes from setting up several pfSense installs

## ISP Issues

### Aussie Broadband

- nil issues on VDSL; much love for ABB

### Telstra HFC

Only issues pertain to HFC itself. One install site had nearly 100 Mbps down and was very stable. Another fluctuated between 20 and 45 Mbps on a 75 link. 

Otherwise effortless, as long as you waited long enough for the link to establish a new connection after pulling down the router.

### Telstra Business

What a joke. The POS gateway that comes with it is so poorly managed its beyond a joke. Telstra hides behind 'security' as its fundamental right to provision barely adequate and half functional equipment.

For example you cannot:
- Bridge the modem
- Turn off wifi
- Turn off DHCP

For future reference, to fix this hot garbage all you need is:
- Cheap af am200 Netgear VDSL router (80 bucks last I checked) with these settings:
  - Upgraded to latest firmware (rumours stock <1.0.0.32 (I think) result in port block upstream)
  - DHCP off
  - Bridging (Modem mode) with VLAN Passthru (not needed technically)

