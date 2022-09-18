import time
import datetime
from alarmdecoder import AlarmDecoder
from devices.usb_device import USBDevice
import tconfig
import sys

Znames = "Smoke alarm", "Front Door", "Mud room door", "Backyard door", "Masterbedroom slide door", "Guest room window","Elaine's bedroom window", "Hall Motion", "Side Garage Door", "Front Window", "Kitchen window", "Dining Room window", "Living room window left", "Living Room window right", "Master bedroom Jacuuzi window", "Masterbedroom bathroom window", "Hall bathroom window", "unknown", "Office window", "unknown", "unknown"
Ztimes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 


def main():
    print ("main: rebooting")
    sys.stdout.flush()
    tconfig.send_text_alert("HomeBot: rebooting")
    try:
        device = AlarmDecoder(USBDevice.find())
        device.on_message += handle_message
        with device.open():
            while True:
                time.sleep(1)
                tnow = int(time.time())
                for n in range(len(Ztimes)):
                    if Ztimes[n-1]!=0 and tnow-Ztimes[n-1] > 30:
                        #timestamp = (' {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
                        #if n != 8 : print(timestamp, "CLEAR! ", n-1, Znames[n-1])
                        Ztimes[n-1] = 0
                        
    except Exception as ex:
        print('Exception:', ex)

def handle_message(sender, message):
    timestamp = (' {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    shorttimestamp = (' {:%H:%M}'.format(datetime.datetime.now()))
    epochtime = int(time.time())
    zoneN = message.raw[23:26]
    i = int(zoneN)-1
    if Ztimes[i]>0:
        Ztimes[i] = epochtime
    else:
        Ztimes[i] = epochtime
        print(timestamp, "Alert! ", i, Znames[i])
        tconfig.send_text_alert(Znames[i])
        sys.stdout.flush()


if __name__ == '__main__':
    main()
