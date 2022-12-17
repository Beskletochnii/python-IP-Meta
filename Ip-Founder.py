#!/usr/bin/env python3
# pip install geoip2

#By Beskletochnii

import os
import requests
import argparse
from colorama import Fore, Style
import geoip2.database
import colorama
import re

def get_location_offline(ip, bool_c, outfff):

    with geoip2.database.Reader('./GeoLite2-City.mmdb') as reader:
        try:
            #print(Fore.YELLOW + Style.BRIGHT + f"READ {ip}")
            response = reader.city(ip)
        except:
            print(Fore.RED + Style.BRIGHT + f"{ip} - Not found")
            outfff.write(
                f"{ip};None;None;None;None;None;None\n")
            return 0
        if(bool_c):
            print(Fore.GREEN + Style.BRIGHT + f"IP:{ip} <=> "
                                              f"Country:{str(response.country.name)}\n"
                                              f"Town:{str(response.subdivisions.most_specific.name)}\n"
                                              f"ISO_Code:{str(response.subdivisions.most_specific.iso_code)}\n"
                                              f"City:{str(response.city.name)}\n"
                                              f"Location:{str(response.location.latitude)} {response.location.longitude}\n"
                                              f"Network:{str(response.traits.network)}\n")
        else:
            #print(Fore.WHITE + Style.BRIGHT + f"WRITE {ip}")
            outfff.write(f"{str(ip)};"
                       f"{str(response.country.name)};{str(response.subdivisions.most_specific.name)};{str(response.subdivisions.most_specific.iso_code)};"
                       f"{str(response.city.name).encode('ascii', 'replace').decode('ascii')};{str(response.location.latitude)} {str(response.location.longitude)};{str(response.traits.network)}\n")
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--IPfile", dest="ip_file", type=str, help="Specify file with your ip's")
    parser.add_argument("-i", "--ip", dest="ip", type=str, help="Specify your ip")
    parser.add_argument("-o", "--output", dest="outfile", type=str, help="Specify your output file")
    outfile = "./outIpLoc.txt"
    args = parser.parse_args()
    if args.ip_file is None and args.ip is None:
        parser.error("At least one of -f/--IPfile and -i/--ip required. Use -h to view help")
    if args.ip_file is not None and args.ip is not None:
        parser.error("You need to specify only one argument -f/--IPfile or -i/--ip")
    if args.outfile is not None:
        outfle = args.outfile

    existfile = os.path.exists(outfile)
    if not existfile:
        print(Fore.YELLOW + Style.BRIGHT + f"Create HEAD")
        outf = open(outfile, "w")
        outf.write("IP;Country;Town;ISO_Code;City;Location;Network\n")
    else:
        outf = open(outfile, "w")

    if args.ip_file is not None:
        f = open(args.ip_file, "r")
        for ipfile in f:
            loc_ip = get_location_offline(ipfile[:-1], 0, outf)
    else:
        body = {"ip": args.ip[-1]}
        get_location_offline(args.ip,1,outf)

