#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: snigdhaghoshdastidar
"""

# SNIGDHA GHOSH DASTIDAR
# PROJECT 4 

import urllib.request as ur
import re

def list_all_links(s):
    """ Returns a list of strings one string for each URL contained in s"""
    slen=len(s)
    j=0
    lists=[]
    if "<a href" not in s:
        return -1
    while j<=slen:
        if "<a href=" in s[j:]:
            url_start=s.find("<a href=",j)
            url_end= s.find('"',url_start + 10)
            j=url_end + 1
            string= s[url_start+9:url_end]
            lists.append(string)
        else:
            break 
    return lists
    


def get_addresses(cont):
    """Gets email addresses"""
    strings=re.findall('[a-zA-Z0-9_.]*[@][a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
                       str(cont)) 
    for i in range(len(strings)):
        if strings[i].endswith("."):
            strings[i]+=strings[i][0:len(strings[i])-1]
    return strings


def crawl(start,limit):
    """Returns a list of unique email addresses"""
    to_visit=[start]
    visited=[]
    
    for x in to_visit:
        cont=str(ur.urlopen(start).read())
        links=list_all_links(cont)
    to_visit.extend(links)
    
    while links:
        if len(set(to_visit))>=limit:
            break 
        link2=[]
        link3=[]
        for y in links:
            source=str(ur.urlopen(y).read())
            link2.extend(list_all_links(source))
        for i in link2:
            if i not in to_visit:
                link3.append(i)
        links=link3
        to_visit.extend(links)
    to_visit.reverse()
    
    emails=[]
    while to_visit:
        address=to_visit.pop()
        if address not in visited:
            connection=ur.urlopen(address)
            content=str(connection.read())
            ema=get_addresses(content)
            visited.append(address)
            emails.extend(ema)
            if len(visited)>=limit:
                break
    emails=list(set(emails))
    # print(emails)
    return emails 


print("\n\nWelcome!\n")
loop = "c"
while(loop == "C" or loop == "c"):
    start=input("\nEnter the site: ")
    limit=input("Number of sites to be visited: ")
    print("Emails addresses found: ")
    print(crawl(start, int(limit)))
    loop = input("\nType Q to Quit and C to continue: ")

    
