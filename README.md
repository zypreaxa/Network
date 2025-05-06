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


