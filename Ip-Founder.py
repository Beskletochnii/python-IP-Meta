#!/usr/bin/env python3
# pip install geoip2
import json
# By Beskletochnii

import os
from time import sleep

import requests
import argparse
from colorama import Fore, Style
import geoip2.database
import colorama
import re
import io


def online_ip_api(ip, bool_c, outfff):
    request_url = 'http://ip-api.com/json/' + ip
    response = requests.get(request_url)
    result = response.content.decode()
    result = json.loads(result)
    # print(str(result) + str("\n"))
    if result['status'] == "fail":
        if bool_c:
            print(Fore.YELLOW + Style.BRIGHT + f"{ip} - {result['status']} - {result['message']}")
        else:
            print(Fore.YELLOW + Style.BRIGHT + f"{ip} - {result['status']} - {result['message']}")
            outfff.write(f"{ip};{result['status']};{result['message']}\n")
        return 0
    # print(f"bool_c: {bool_c}")
    if (bool_c):
        print(Fore.WHITE + Style.BRIGHT + f"Online MODE!")
        print(Fore.GREEN + Style.BRIGHT + f"IP:{ip} <=> "
                                          f"Status:{result['status']}\n"
                                          f"Country:{result['country']}\n"
                                          f"RegionName:{result['regionName']}\n"
                                          f"ISO_Code:{result['countryCode']}\n"
                                          f"City:{result['city']}\n"
                                          f"Location:{result['lat']} {result['lon']}\n"
                                          f"Network:NoneInOnlineMode\n"
                                          f"TimeZone:{result['timezone']}\n"
                                          f"Company:{result['isp']}\n"
                                          f"Organization:{result['org']}\n"
                                          f"AS:{result['as']}\n"
                                          f"Query:{result['query']}\n")
    else:
        print(Fore.WHITE + Style.BRIGHT + f"WRITE {ip}")
        outfff.write(f"{ip};"
                     f"{result['status']};{result['country']};{result['regionName']};"
                     f"{result['countryCode']};{result['city']};{result['lat']} {result['lon']};NoneInOnlineMode;{result['timezone']};{result['isp']};"
                     f"{result['org']};{result['as']};{result['query']}\n")

    return 0


def get_location_offline(ip, bool_c, outfff):
    with geoip2.database.Reader('./GeoLite2-City.mmdb') as reader:
        try:
            # print(Fore.YELLOW + Style.BRIGHT + f"READ {ip}")
            response = reader.city(ip)
        except:
            print(Fore.RED + Style.BRIGHT + f"{ip} - Not found")
            outfff.write(
                f"{ip};None;None;None;None;None;None\n")
            return 0
        if (bool_c):
            print(Fore.GREEN + Style.BRIGHT + f"IP:{ip} <=> "
                                              f"Country:{str(response.country.name)}\n"
                                              f"Town:{str(response.subdivisions.most_specific.name)}\n"
                                              f"ISO_Code:{str(response.subdivisions.most_specific.iso_code)}\n"
                                              f"City:{str(response.city.name)}\n"
                                              f"Location:{str(response.location.latitude)} {response.location.longitude}\n"
                                              f"Network:{str(response.traits.network)}\n")
        else:
            # print(Fore.WHITE + Style.BRIGHT + f"WRITE {ip}")
            outfff.write(f"{str(ip)};"
                         f"{str(response.country.name)};{str(response.subdivisions.most_specific.name)};{str(response.subdivisions.most_specific.iso_code)};"
                         f"{str(response.city.name).encode('ascii', 'replace').decode('ascii')};{str(response.location.latitude)} {str(response.location.longitude)};{str(response.traits.network)}\n")
        return 0


req_sec = 45
counter = 1
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--IPfile", dest="ip_file", type=str, help="Specify file with your ip's")
    parser.add_argument("-i", "--ip", dest="ip", type=str, help="Specify your ip")
    parser.add_argument("-o", "--output", dest="outfile", type=str, help="Specify your output file")
    parser.add_argument("-O", "--online", dest="online_geo", action='store_const', const=True, default=False,
                        help="Use ip-api.com service.")

    args = parser.parse_args()
    if args.online_geo:
        outfile = "./DefaultOutOnline.txt"
    else:
        outfile = "./DefaultOut.txt"

    if args.ip_file is None and args.ip is None:
        parser.error("At least one of -f/--IPfile and -i/--ip required. Use -h to view help")
    if args.ip_file is not None and args.ip is not None:
        parser.error("You need to specify only one argument -f/--IPfile or -i/--ip")
    if args.outfile is not None:
        outfile = args.outfile


    existfile = os.path.exists(outfile)
    print(f"existfile: {existfile}")
    if not existfile:
        print(Fore.YELLOW + Style.BRIGHT + f"Create HEAD")
        outf = open(outfile, "w", encoding="utf-8")
        if args.online_geo:
            outf.write(
                "IP;Status;Country;RegionName;ISO_Code;City;Location;Network;TimeZone;Company;Organization;AS;Query\n")
        else:
            outf.write("IP;Country;Town;ISO_Code;City;Location;Network\n")
    else:
        outf = open(outfile, "w", encoding="utf-8")

    if args.ip_file is not None and args.online_geo == False:
        f = open(args.ip_file, "r")
        for ipline in f:
            print(f"Number: {counter}")
            loc_ip = get_location_offline(ipline[:-1], 0, outf)
            counter+= 1
    elif not args.online_geo:
        body = {"ip": args.ip[-1]}
        get_location_offline(args.ip, 1, outf)
    elif args.ip_file is not None and args.online_geo:
        f = open(args.ip_file, "r")
        # line_count = sum(1 for line in open(args.ip_file))
        for ipline in f:
            print(f"Number: {counter}")
            loc_ip = online_ip_api(ipline[:-1], 0, outf)
            sleep(60 / req_sec)
            counter += 1
    elif args.online_geo:
        online_ip_api(args.ip, 1, outf)
