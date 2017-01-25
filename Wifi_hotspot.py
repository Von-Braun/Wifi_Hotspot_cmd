import os,subprocess
os.system("title Wifi Hotspot Control")
settings_file = open('Wifi_settings.txt','r')
SSID = settings_file.readline().strip('\n')
Password = settings_file.readline()
settings_file.close()
info=''

def get_cmd_output(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.communicate() #out, error

while True:
    if 'Not started' in get_cmd_output('netsh wlan show hostednetwork')[0]:
        Status='Off'
    else:
        Status='On'
    os.system('cls')
    print '---Info'+('-'*87)+'\n'+info+'\n'+('-'*94)
    print 'Status:'+Status+'\nSSID: '+SSID+'\nPassword: '+Password+'\n\n1) Enable hotspot\n2) Disable hotspot\n3) Change SSID\n4) Change Password\n'
    option = raw_input('>')
    if option=='1':
        info=get_cmd_output('netsh wlan set hostednetwork mode=allow ssid=\"'+SSID+'\" key='+Password)[0].strip()
        info=info+get_cmd_output('netsh wlan start hostednetwork')[0].strip()
    elif option=='2':
        info=get_cmd_output('netsh wlan stop hostednetwork')[0].strip()
    elif option=='3':
        SSID = raw_input('SSID:')
        settings_file = open('Wifi_settings.txt','w')
        settings_file.write(SSID+'\n'+Password)
        settings_file.close()
        info='SSID changed to: '+SSID
    elif option=='4':
        Password = raw_input('Password:')
        settings_file = open('Wifi_settings.txt','w')
        settings_file.write(SSID+'\n'+Password)
        settings_file.close()
        info='Password changed to: '+Password
    else:
        break