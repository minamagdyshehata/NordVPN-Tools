import os ,ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def RemoveVirtualAdapter(i):
    if i=="y" or i=="Y":
        os.system("netsh wlan stop hostednetwork")
        os.system("netsh wlan set hostednetwork mode=disallow")
        print ("Microsoft Wi-Fi Direct Virtual Adapter successfully removed...")
        print ("")
        xx = input ("Press Enter to exit...")
    elif i=="n" or i=="N":
        print ("Microsoft Wi-Fi Direct Virtual Adapter is not removed...")
        print ("")
        print ("Do you want to remove Microsoft Wi-Fi Direct Virtual Adapter? ")
        D = input ("'y' for yes, 'n' for no, 'x' to exit:  ")
        RemoveVirtualAdapter(D)       
    elif i=="x" or i=="X":
        exit()
    else:
        print ("Please type 'y', 'n' or 'x'...")
        print ("")
        print ("Are you sure you want to remove Microsoft Wi-Fi Direct Virtual Adapter? ")
        D = input ("'y' for yes, 'n' for no, 'x' to exit:  ")
        RemoveVirtualAdapter(D)
        
if is_admin():
    print (" Remove Microsoft Wi-Fi Direct Virtual Adapter for Windows")
    print (" Programmed by Eng. Mina Magdy, email: eng.minamagdy@live.com ")
    print ("==============================================================")
    print ("")
    print ("Are you sure you want to remove Microsoft Wi-Fi Direct Virtual Adapter? ")
    i = input ("'y' for yes, 'n' for no, 'x' to exit:  ")
    RemoveVirtualAdapter(i)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
