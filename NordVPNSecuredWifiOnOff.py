import os ,ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def NordVPNSecuredWifiOnOFF(i):
    if i=="y" or i=="Y":
        os.system("netsh wlan start hostednetwork")
        print ("Turning NordVPN Secured Wifi ON....")
        os.system("netsh wlan show hostednetwork")
        print ("")
        print ("Turn NordVPN Secured Wifi ON/OFF, Show Status or Exit?")
        D = input ("'y' for yes, 'n' for no, 's' to show network status, 'x' to exit:  ")
        NordVPNSecuredWifiOnOFF(D)
    elif i=="n" or i=="N":
        os.system("netsh wlan stop hostednetwork")
        print ("Turning NordVPN Secured Wifi OFF....")
        os.system("netsh wlan show hostednetwork")
        print ("")
        print ("Turn NordVPN Secured Wifi ON/OFF, Show Status or Exit?")
        D = input ("'y' for yes, 'n' for no, 's' to show network status, 'x' to exit:  ")
        NordVPNSecuredWifiOnOFF(D)
    elif i=="s" or i=="S":
        os.system("netsh wlan show hostednetwork")
        print ("")
        print ("Turn NordVPN Secured Wifi ON/OFF, Show Status or Exit?")
        D = input ("'y' for yes, 'n' for no, 's' to show network status, 'x' to exit:  ")
        NordVPNSecuredWifiOnOFF(D)       
    elif i=="x" or i=="X":
        exit()
    else:
        print ("Please type 'y', 'n' or 'x'...")
        print ("")
        print ("Turn NordVPN Secured Wifi ON/OFF, Show Status or Exit?")
        D = input ("'y' for yes, 'n' for no, 's' to show network status, 'x' to exit:  ")
        NordVPNSecuredWifiOnOFF(D)
        
if is_admin():
    print (" NordVPN Secured Wifi ON/OFF for Windows")
    print (" Programmed by Eng. Mina Magdy, email: eng.minamagdy@live.com ")
    print ("==============================================================")
    print ("")
    print ("Turn NordVPN Secured Wifi ON/OFF, Show Status or Exit?")
    i = input ("'y' for yes, 'n' for no, 's' to show network status, 'x' to exit:  ")
    NordVPNSecuredWifiOnOFF(i)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
