import gla_library

def popen_background(cmd):
    p = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o = p.stdout.read()
    e = p.stderr.read()
    o = str(o.encode('utf-8')).strip().rstrip()
    e = str(e.encode('utf-8')).strip().rstrip()
    output = o + e
    return output

def main():
    options = """
    ### Wireless Offensives

    1. mdk3, top choice for wireless disruption, defeating Wireless Distribution Systems, WIPS, WIDS, and brute-forcing whitelisted MAC addrs
    2. aircrack-suite,
    3. airbase-ng,
    4. mana-toolkit
    5. wifi-phisher
    6. ghost-phisher
    7. freeRADIUS + HostAPD, phish for RADIUS authentication credentials using a phony WPA2-MGT RADIUS authenticated server
    8. Routersploit Framework
    9. 'Abominable Intelligence/AutoExploit Pi', open source copy of my original Autohacking Wireless Pi Project, configured to automatically audit known wireless routers with RouterSploit's AutoPwn vulnerability scanner, and msfconsole
    10. wifite
    11. reaver + PixieWPS
    12. besside-ng + Wardriver XPress bugfix upgrade, auto deauths all WPA2-PSK networks in range to collect handshakes transmitted in air, this version contains the network interface card fix

    ### Wireless Evasion

    A. 'Smoke Bomb', disconnects and reconnects to wireless after changing MAC address, IP, and Hostname.
    B. 'mdk3 multiply-access points', uses mdk3's Beacon Flood Mode to show fake access points
    C.
    """
    return
main()
