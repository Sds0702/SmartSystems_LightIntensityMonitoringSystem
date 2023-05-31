# SmartSystems_LightIntensityMonitoringSystem
Smart Light Intensity Monitoring System using Raspberry PI

**Implementation and Experimental Setup:**
Using a photoresistor, an analog-to-digital converter (MCP3008), actuators (like a fan), a Raspberry Pi (a microcontroller), and an OpenStack server (Cloud), we have developed and implemented a smart light intensity monitoring system that can be used in both private and public settings, including homes, businesses, and even public spaces. The amount of light a photoresistor can absorb varies according on its resistance and the resistance of the component decreases with increasing brightness and increases with decreasing brightness. 

We have employed an independent variable in this experiment that is user-controllable and independent of all other factors. In this application configuration, we will connect all our gadgets to the Raspberry Pi 4 using a breadboard. An Analog-to-Digital Converter must be connected to the breadboard before the Photoresistor can be read by the Raspberry Pi.

The Light-dependent resistor (Photoresistor), an Analog-to-Digital Converter (MCP3008), and a 10 k Resistor will all be attached to the breadboard. The Raspberry Pi's GPIO pins are then used to link these devices to the system. We will be triggering a Fan (serving as the actuator) based on the output of the resistor to demonstrate that the data is being received. The below image is the experimental setup of the application, to implement and demonstrate the working of a Smart Light Intensity Monitoring System.

![image](https://github.com/Sds0702/SmartSystems_LightIntensityMonitoringSystem/assets/124682336/9d0bf3f6-b3b1-47a8-8c3e-f8c2db702cd5)
                                           
                                                    Figure: Experimental Setup

Two phases of the experiment were carried out. The values output when the Photoresistor is exposed to bright light are lower than when the sensor is completely covered to prevent the light, as we found when we first implemented the programme on the Raspberry Pi network. The sensors, actuator, and Raspberry Pi served as the client in the second section of the project, while the Open Stack Server (cloud) served as the server. 

We discovered that even though we could ping the networks using the Raspberry Pi system during the installation of the server application on the Open stack Server, we could not establish a connection to the Virtual Instance Console. However, we were able to connect to the Open stack Virtual Instance Console through a normal system.
