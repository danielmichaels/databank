# Cisco

## SG300

SSH setup requires older key variations. To SSH in without a key error;

`ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 123.123.123.123`
