# Network lab documentation
## Lab requirements

 - Employees must be able to seamlessly connect to the corporate network anywhere in the building (roaming).

- Only authenticated users should be allowed to access the network via WPA2-Enterprise.

- Guest users must use a separate network with Internet access only.

- The WLC should be redundant so that if one controller fails, the Wi-Fi remains available.

- Teams/Zoom traffic should be prioritised on the network.

- The IT department wants to be able to roll out all configurations via automated scripts.



## ToDo's
### Basic

- Add at least 2 additional access points and configure roaming.

- Make sure each AP is on its own VLAN.

- Connect the network to a router for internet access.
### Authentication and guest access

- Install and configure a RADIUS server.

- Link the WLC to the RADIUS server for WPA2-Enterprise.

- Configure a captive portal or separate guest VLAN with restricted access.
### High Availability & LAG

- Add a second WLC and set up HA SSO (Stateful SwitchOver).

- Configure LAG on the WLC and the core switch for more bandwidth/redundancy.
### QoS en Automatisation

- Analyse network traffic and set QoS profiles (prioritise VoIP/Video).

- Develop and test an automation script for deploying AP configurations.



 ## Prerequisite downloads for network setup
PuTTY application
```
https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.83-installer.msi
```
After running PuTTY, you should select the _Serial_ connection type and type in the serial line that your connection with the network is on, as shown in the example below.


![436502061-a1aaa944-f73e-4bed-92bf-b2a4e59207dc.png](attachment:436502061-a1aaa944-f73e-4bed-92bf-b2a4e59207dc.png)




## Physical connections

### Switch
Configuration saved on switch.
Ports:
- GigabitEthernet1/0/1-12 - VLAN 10, Service 192.168.10.55/24, mode access, spanning tree portfast
- GigabitEthernet1/0/13-24 - VLAN 11, Management 192.168.11.55/24, mode access, spanning tree portfast
- GigabitEthernet1/0/25-36 - Vlan 12, Guest 192.168.12.55/24, mode access, spanning tree portfast
- GigabitEthernet1/0/47 - Router connection 10.0.0.1/24, no switchport
- GigabitEthernet1/0/48 - WLC connection, switchport mode trunk, switchport trunk allowed VLAN 10-12

Switch routes all traffic to the router:
- ip route 0.0.0.0 0.0.0.0 10.0.0.2

DHCP pools for each VLAN:
- ip dhcp pool VLAN 10: network 192.168.10.0/24, default-router 192.168.10.1
- ip dhcp pool VLAN 11: network 192.168.11.0/24, default-router 192.168.11.1
- ip dhcp pool VLAN 12: network 192.168.12.0/24, default-router 192.168.12.1


### Router
Configuration saved outside of router. After every bootup configuration txt file should be copied and pasted in configure-terminal mode.
After this initial configuration, both GigabitEthernet0/0 and GigabitEthernet0/1 should be set to no shutdown.

Ports:
- GigabitEthernet0/0 - 192.168.8.8/24, ip nat outside
- GigabitEthernet0/1 - 10.0.0.2/24, ip nat inside

Initial source list solution did not work, so a route-map was also created
- ip nat inside source list 1 interface GigabitEthernet0/0 overload
- ip nat inside source route-map VLAN-NAT interface GigabitEthernet0/0 overload

Routes all traffic outside to the server:
- ip route 0.0.0.0 0.0.0.0 192.168.8.254
- ip default-gateway 192.168.8.254

Routes all the VLAn traffic to the port connecting to the switch:
- ip route 192.168.10.0 255.255.255.0 10.0.0.1
- ip route 192.168.11.0 255.255.255.0 10.0.0.1
- ip route 192.168.12.0 255.255.255.0 10.0.0.1

- ip access-list extended VLAN-SUBNETS
    - permit ip 192.168.10.0 0.0.0.255 any
    - permit ip 192.168.11.0 0.0.0.255 any
    - permit ip 192.168.12.0 0.0.0.255 any

Route maps:
- route-map VLAN-NAT permit 10
    - match ip address VLAN-SUBNETS
- route-map VLAN-NAT permit 11
    - match ip address VLAN-SUBNETS
- route-map VLAN-NAT permit 12
    - match ip address VLAN-SUBNETS

Access lists:
- access-list 1 permit 10.0.0.0 0.0.0.255
- access-list 1 permit 192.168.10.0 0.0.0.255
- access-list 1 permit 192.168.11.0 0.0.0.255
- access-list 1 permit 192.168.12.0 0.0.0.255


### Proxmox
Proxmox has two CISCO WLC VMs for high availability:
- Main, 192.168.11.56/24
- Failover, 192.168.11.57/24

Proxmox also has a RADIUS authentication server:
- TBD!!