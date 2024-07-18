# Layer 2 - Data Link

Layer 2 runs over a Layer 1 (physical network), but is built up of frames instead of just binary bits from changes in voltage (0s & 1s)

- Data Frames: Container of infomration that includes the data from Layer 1 (payload), a verification check, 
- MAC Addresses: Physical identifier address associated to a piece of hardware

  What builds up a frame
- MAC Header
  - Preamble: Identifier that shows where the dataframe starts
  - Destination MAC: Specifies where the data is to be sent on the local network. Specifying all *F's* will broadcast the data to all hosts.
  - Source MAC: Specicifies where the data is being sent from.
  - Ether Type: Specifies which Layer 3 protocol is being used to put the data into frame (IP for example)
- Payload: Contains the data that is being transfered (the binary bits)
- FCS (Frame Check Sequence): Checks that all bits made it without corruption

![](https://www.firewall.cx/images/stories/ethernet-frames-ethernet-ii-1.gif)

Why is Layer 2 and Data Frame encapsulation important?
- If there are two devices on a physical medium sending data at the same time, there can be collisions in the data (binary bits getting mixed)
- If there are more than two devices on a local network/physical medium, collision and corruption is almost guarenteed.
- With MAC source and destination addresses, we can identify devices
- Collision Control through checking whether something is currently being sent through Layer 1

Layer 2 is able to check if there is any data in the carrier (being transfered currently), and sends it through Layer 1. This avoids collisions. Then Layer 1 at all destinations pass the data to Layer 2 at the destination in order to build the frame from the binary payload and decipher the data frame to tell if it is the right destination. If it is, data will be read, if not it will be discarded. 

#### A Layer 1 HUB vs A Layer 2 Switch

Layer 1 HUB
- Allows for a local network over a physical medium with more than 2 devices. 
- All data is recieved by all devices on the network. With Layer 1, all data will be deciphered by all devices. with Layer 2 data frames the intended destination will decipher the data, otherwise it will be discarded.
Layer 2 Switch
- Allows for a local network over a physical medium with more than 2 devices. 
- Has Layer 2 capabilities built in and can understand the frame and the intended destination. Switch forwards the frame to only the destination MAC
- Identifes corrupted data and will not forward. Which prevents re-forwarding collision data.

