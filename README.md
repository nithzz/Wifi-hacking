# Wifi-hacking
If there is a lock next to the network name (SSID / Service Set Identifier), that indicates security
is activated. Without a password or passphrase, we won't be able to get access to that network
or the internet. WIfi security can be based on Wired Equivalent Privacy(WEP) or Wifi Protected
Access(WPA). Aircrack-ng is a suite of tools to assess WIfi network security, it can be used on
cracking WEP and WPA-PSK keys.

# REQUIREMENTS
1. Wifi network adapter
2. WIfi network to attack
3. Kali linux
4. Airmon-ng
5. Airodump-ng
6. Aircrack-ng

# COMMANDS
1. iwconfig - 
  <iwconfig> command shows us that a network adapter is connected to the virtual box or
  the attacker’s machine. It also shows the mode of the network adapter - initially, it will be
  in managed mode.
2. Sudo airmon-ng check kill   - 
  It kills any conflicting processes so that it won't interfere with the Wi-Fi attacks.
3. Sudo airmon-ng start <wlan0>   - 
  Initially the network adapter connected to the attacker’s machine will be in "engaged
  mode", we need to modify it into monitoring mode.
4. Sudo airmon-ng   - 
  We use this command to verify if the adapter’s mode is changed to monitoring mode.
5. Sudo airodump-ng <wlan0mon>   - 
  In order to discover the access points or the available wifi networks, we make use of this
  command. It displays the wireless networks, channel, SSID, MAC address of the various
  stations. From this we need to select a network to be attacked.
6. Sudo airodump-ng wlan0mon -d <mac-address>   - 
  It only displays the details related to the particular access points. If we try connecting to
  that network using some other device, we would be able to spot the connected client
  device.
7. Sudo aireplay-ng –deauth 0 -a <mac-address> wlan0mon   - 
It de-authenticates the clients from the network. We are going to send continuous deauth
packets to the connected devices of the network. WPA four-way handshake is captured.
8. Sudo airodump-ng -w hack1 -c 2 –bssid <bssid id> wlan0mon   - 
It is used to capture the 4-way handshake. Which is stored in a wireshark file named
hack1, we further use it to crack the password of the device connected to.
9. Sudo airmon-ng stop wlan0mon   - 
It stops the network adapter from monitor mode and changes it back to the default.
10. Aircrack-ng <pcap file name> -w </usr/share/wordlists/rockyou.txt>   - 
It cracks the passphrase of the network.

# DEMO

 - The process can be automated by the Python script.
 - git clone the repository and pip install the requirements
 - run the python script to automate the tasks
![w1](https://github.com/nithzz/Wifi-hacking/assets/79152978/bce6b783-eed9-4276-a29d-b868429229b8)

![w2](https://github.com/nithzz/Wifi-hacking/assets/79152978/9436bfa4-6fe2-475b-83d3-7a95da6f5c51)

![w3](https://github.com/nithzz/Wifi-hacking/assets/79152978/20e4b4bf-c44c-4d9b-8cbf-74adc07ee9c0)

![w4](https://github.com/nithzz/Wifi-hacking/assets/79152978/2426fd29-f554-4d4c-a41a-ef64df4483e1)

![w5](https://github.com/nithzz/Wifi-hacking/assets/79152978/2fa7c40e-0819-4917-a042-f4147ab95eec)

![w6](https://github.com/nithzz/Wifi-hacking/assets/79152978/ce7da352-b099-4b76-a41b-5cbf94f8c153)

![w7](https://github.com/nithzz/Wifi-hacking/assets/79152978/011517c0-9409-46a7-9a69-612c966d7dad)

![w8](https://github.com/nithzz/Wifi-hacking/assets/79152978/204f3744-959e-4e96-a8a7-bb168a356195)

