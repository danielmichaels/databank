# Resize LVM

Refer to [url](http://rabexc.org/posts/resizing-filesystem)

- Become root with `su`
- Identify the partition to extend with `fdisk -l`
- use `pvcreate` to make that partition usable (e.g. `pvcreate /dev/nvme0n1p3`)
- check that the space is now usable `pvs`
- then extend the LV with `lvextend -L +10G /dev/lvmpool/root`
- check that its worked with `vgs`
- now run `resize2fs -p /dev/mapper/lvmpool-root` to make the changes stick
- `df -h` to see the changes or `dmesg` to see the changes taken effect
