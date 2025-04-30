# AWS VPC Flow Logs

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721149200/GkyF8Mg8z4_WVdL503GbNw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/ePeV0mLtWzEim05O_jWMWmmOz2t5m_nsh.png)

## Summary

Many AWS services provide built-in access-control audit trails and logs. You can enable Amazon VPC Flow Logs to capture information about the IP traffic going to and from network interfaces in your VPC. VPC Flow Logs can help you with a number of tasks. For example, you can troubleshoot why specific traffic is not reaching an instance, which in turn helps you diagnose overly restrictive security group rules. You can also use Flow Logs as a security tool to monitor the traffic that is reaching your instance.

To learn more, see Logging IP Traffic Using [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html).

## Use

- Track network activity to your instances inside a VPC. Troubleshoot connectivity and identify network threats. 
- Troubleshoot overly strict Security groups and NACLs to find why traffic is not making it to your host.
- Identify overly permissive security groups and NACLs to find traffic that should not be making it to your host.


- Only capture packet metadata, does not capture the contents. Ex. source/dest IP, packet size, action, start/end and things you can see from the outside of the packet.
  - Ex. 2 ACC-ID eni-ID 123.22.22.22 10.11.1.1 443 0 1 4 336 14329177019 14329341 ACCEPT OK
  - First 0 is the protocol ICMP=1, TCP=6, UDP=17.
- Work by attaching a network monitor to a VPC to monitor all ENIs in the VPC, to a subnet to monitor all ENIs in a subnet, or attached to an ENI directly. 
- VPC Flow Logs are not real-time
- Log destinations can be either S3 or CloudWatch Logs
- Requests to 169.254.169.254 (IMSD), DHCP, Amazon DNS Server, and Amazon Windows license is not recorded by VPC Flow Logs
