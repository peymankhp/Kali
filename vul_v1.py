import subprocess
import os
import time
import shutil
import sys
import iptools
import re

##################################
#remove inside of folder
def Remove_path(path):
    for dir in os.listdir(path):
        shutil.rmtree(os.path.join(path, dir))

config_path = '/home/peiman/Python/Command output'
Remove_path(config_path)

##################################

#Find_IP
def Find_IP(textfile):
    for line in textfile:
        #print(line)
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
        if ip:
            # Add each ip to ip text file
            for i in ip:
                a_ip = open('/home/peiman/Python/ip_output.txt', "a")
                # Write IP as string
                a_ip.write(str(i))
                #print(i)
                a_ip.write('\n')     


##################################
#DNSRECON 
def dnsrecon (host):
    CMD_dnsrecon = ('dnsrecon -d ' + host)
    output_CMD_dnsrecon = os.popen(str(CMD_dnsrecon))
    outputcmd_dnsrecon=output_CMD_dnsrecon.read()
    CMDfilename_dnsrecon = str(host + ' ' + '.txt')
    # creat folder with hostname of SW
    newpath_dnsrecon = os.path.join('/home/peiman/Python/Command output/dnsrecon/', host)
    if not os.path.exists(newpath_dnsrecon):
        os.makedirs(newpath_dnsrecon)
    # creat string of path
    newpath_dnsrecon = str(newpath_dnsrecon)
    # creat text file in path of hostname
    filepath_dnsrecon = os.path.join(newpath_dnsrecon, CMDfilename_dnsrecon)
    if not os.path.exists('/home/peiman/Python/Command output/dnsrecon/'):
        os.makedirs('/home/peiman/Python/Command output/dnsrecon/')
    f_dnsrecon = open(filepath_dnsrecon, "w")
    f_dnsrecon.truncate(0)
    f_dnsrecon = open(filepath_dnsrecon, "a")
    # write config to hostname file
    f_dnsrecon.write(outputcmd_dnsrecon)
    #Find ip and save on file
    Read_dnsTXT = open('/home/peiman/Python/ip_input.txt',"w")
    Read_dnsTXT.truncate(0)
    Read_dnsTXT.write(outputcmd_dnsrecon)
    Read_dnsTXT=open('/home/peiman/Python/ip_input.txt',"r")
    DNS_Output=Read_dnsTXT.readlines()
    Find_IP(DNS_Output)
    
host_dns='mirdamad.ac.ir'
dnsrecon (host_dns)

##################################
#Run nmap for ip

def nmap (host,sudoPassword):
    CMD_nmap = ('sudo nmap -Pn -F -sV -O  ' + host)
    cmd_nmap = os.popen('echo %s|sudo -S %s' % (sudoPassword,CMD_nmap))
    output_nmap = cmd_nmap.read()
    #print (output_nmap)
    CMDfilename_nmap = str(host + ' ' + '.txt')
    # creat folder with hostname of SW
    newpath_nmap = os.path.join('/home/peiman/Python/Command output/nmap/', host)
    if not os.path.exists(newpath_nmap):
        os.makedirs(newpath_nmap)
    # creat string of path
    newpath_nmap = str(newpath_nmap)
    # creat text file in path of hostname
    filepath_nmap = os.path.join(newpath_nmap, CMDfilename_nmap)
    #print(filepath_nmap)
    if not os.path.exists('/home/peiman/Python/Command output/nmap/'):
        os.makedirs('/home/peiman/Python/Command output/nmap/')
    f_nmap = open(filepath_nmap, "w")
    f_nmap.truncate(0)
    f_nmap = open(filepath_nmap, "a")
    # write config to hostname file
    f_nmap.write(output_nmap)

sudoPass=input("Please type sudo pass: ")
Read_IP_List=open('/home/peiman/Python/ip_output.txt',"r")
ip_nmap=Read_IP_List.read()
ip_nmap_list = ip_nmap.split("\n")

for ip_nmap in ip_nmap_list:
    nmap(ip_nmap,sudoPass) 

##################################
    





