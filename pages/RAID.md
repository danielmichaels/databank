# Redundant Array Independent Disks

## Raid 0

- Splits many disks to increase the throughput
- Referred to as 'disk stripping'
- Used mostly for streaming
- Logically groups disks into one large disk
- If one disk fails it will break the whole array - no redundancy

## Raid 1

- RW data to a pair of drives
- Often called mirroring
- Provides redundancy incase one drive fails
- If any drive fails it will operate off the remaining disk
- Once the faulty disk is replaced, data is copied across to new disk for redundancy
- Easiest failover strategy to implement


