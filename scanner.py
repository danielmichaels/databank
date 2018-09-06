import network
import ubinascii

station = network.WLAN(network.STA_IF)
station.active(True)

results = []
for x in station.scan():
    result_dict = dict()
    result_dict['name'] = x[0]
    result_dict['bssid'] = ubinascii.hexlify(x[1]).decode()
    result_dict['channel'] = x[2]
    result_dict['rssi'] = x[3]
    result_dict['auth_mode'] = x[4]
    result_dict['hidden'] = x[5]
    results.append(result_dict)

for item in results:
    for k, v in item.items():
        print("{k}:\t\t{v}".format(k=k, v=v)
