# python-IP-Meta
Try RUN!
$ python3 Ip-Founder.py -h
usage: Ip-Founder.py [-h] [-f IP_FILE] [-i IP] [-o OUTFILE] [-O]

options:
  -h, --help            show this help message and exit
  -f IP_FILE, --IPfile IP_FILE
                        Specify file with your ip's
  -i IP, --ip IP        Specify your ip
  -o OUTFILE, --output OUTFILE
                        Specify your output file
  -O, --online          Use ip-api.com service.

Example1:
$ python3 Ip-Founder.py -O -i 1.1.1.1
existfile: True
Online MODE!
IP:1.1.1.1 <=> Status:success
Country:Australia
RegionName:Queensland
ISO_Code:AU
City:South Brisbane
Location:-27.4766 153.0166
Network:NoneInOnlineMode
TimeZone:Australia/Brisbane
Company:Cloudflare, Inc
Organization:APNIC and Cloudflare DNS Resolver project
AS:AS13335 Cloudflare, Inc.
Query:1.1.1.1


Example2:
$ python3 Ip-Founder.py -O -i google.com
existfile: True
Online MODE!
IP:google.com <=> Status:success
Country:United Kingdom
RegionName:England
ISO_Code:GB
City:London
Location:51.5074 -0.127758
Network:NoneInOnlineMode
TimeZone:Europe/London
Company:Google LLC
Organization:Google LLC
AS:AS15169 Google LLC
Query:142.250.187.206

Example3:
$ python3 Ip-Founder.py -O -f IpList.txt
existfile: True
Number: 1
WRITE 8.8.8.8
Number: 2
WRITE 1.1.1.1
Number: 3
WRITE 8.8.4.4
Number: 4
WRITE 192.0.0.1

In File CSV With split ";"
8.8.8.8;success;United States;Virginia;US;Ashburn;39.03 -77.5;NoneInOnlineMode;America/New_York;Google LLC;Google Public DNS;AS15169 Google LLC;8.8.8.8
1.1.1.1;success;Australia;Queensland;AU;South Brisbane;-27.4766 153.0166;NoneInOnlineMode;Australia/Brisbane;Cloudflare, Inc;APNIC and Cloudflare DNS Resolver project;AS13335 Cloudflare, Inc.;1.1.1.1
8.8.4.4;success;United States;Virginia;US;Ashburn;39.03 -77.5;NoneInOnlineMode;America/New_York;Google LLC;Google Public DNS;AS15169 Google LLC;8.8.4.4
192.0.0.1;success;;;;;0 0;NoneInOnlineMode;;;;;192.0.0.1







