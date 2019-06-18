# STW

## TC3G

Setting up a custom mobile carrier.

1. in `/mnt/dataflash/stw/modem/` create a two files:
    1. `apns-conf.xml`, and
    2. `apn-default.xml`
2. What worked for me was making both files the same:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<apns version="7">
  <apn carrier="Telstra"
    mcc="505"
    mnc="01"
    apn="m2mone.com.au"
    user=""
    password=""
    type="default,supl"/>
</apns>
```

Now the TC3G will accept the these settings for the M2MOne network, whereas it will otherwise fail thinking the Telstra supplied sim card is for their network's APN.
