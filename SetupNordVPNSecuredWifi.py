import os ,ctypes, sys, getpass

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def CheckNordVPNSecuredWifiOK(OK):
    if OK=="y" or OK=="Y":
        print ("NordVPN Secured Wifi Setup is successful...")
        xx=input("Press Enter to exit..")
        
    elif OK=="n" or OK=="N":
        os.system("mmc devmgmt.msc")
        print("In the Device Manager, navigate to Network Adapters and right-click Microsoft Hosted Network Virtual Adapter, and select Enable.")
        xx=input("Press Enter when done..")
        os.system("netsh wlan start hostednetwork")
        print ("NordVPN Secured Wifi Setup is successful...")
        xx=input("Press Enter to exit..")
        
    else:
        CHECK = input ("Is the Network Status: 'Started'? (y/n) :")
        CheckNordVPNSecuredWifiOK(CHECK)
        
def NordVPNSecuredWifiSetup(i):
    if i=="y" or i=="Y":
        ssid = input ("Please enter the Secured Network Name: ")
        KA = getpass.getpass("Please enter the Secured Network Key: ")
        KB = getpass.getpass("Please confirm the Secured Network Key: ")
        if KA!=KB:
            print ("Secured Network Key confirmation failed !!")
            NordVPNSecuredWifiSetup("y")
        else:
            os.system("netsh wlan set hostednetwork mode=allow ssid=" + ssid + " key=" + KA)
            os.system("netsh wlan start hostednetwork")
            print ("1- Please right-click the network icon in the system tray and select Open Network and Sharing Center.")
            print ("2- Click Change adapter options.")
            print ("3- There you will see the newly created VirtualNord adapter and our the TAP-NordVPN Windows Adapter V9, which our NordVPN app uses to connect to the VPN. Right click on the TAP adapter and select Properties.")
            print ("4- Open Sharing tab, enable Allow other networks users to connect through this computer's Internet connection, and Select Local Area Connection* 13 (in our case it represents VirtualNord). After that, click OK.")
            os.system("netsh wlan start hostednetwork")
            OK = input ("Is the Network Status: 'Started'? (y/n) :")
            CheckNordVPNSecuredWifiOK(OK)
            
    elif i=="n" or i=="N":
        print ("Please try looking for a newer version of your adapter drivers and install them,")
        print ("or try using a different wireless card")
        print ("then start NordVPN Secured Wifi Setup again.")
        xx=input("Press Enter to exit..")
        
    elif i=="x" or i=="X":
        exit()
    else:
        print ("Please type 'y', 'n' or 'x'...")
        print ("")
        print ("What is the status of 'Hosted network supported'? :")
        D = input ("'y' for yes, 'n' for no, 'x' to exit:  ")
        if D=="y" or D=="Y":
            print ("NordVPN Secured Wifi setup in progress......")
        NordVPNSecuredWifiSetup(D)
        
if is_admin():
    print (" NordVPN Secured Wifi Setup for Windows")
    print (" Programmed by Eng. Mina Magdy, email: eng.minamagdy@live.com ")
    print ("==============================================================")
    print ("")
    os.system("netsh wlan show drivers")
    print ("What is the status of 'Hosted network supported'? :")
    i = input ("'y' for yes, 'n' for no, 'x' to exit:  ")
    if i=="y" or i=="Y":
        print ("NordVPN Secured Wifi setup in progress......")
    NordVPNSecuredWifiSetup(i)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
