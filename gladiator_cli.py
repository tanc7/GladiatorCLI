import os, sys, operator
def menuparser(options):
    return menu

apt_list = [
    'socat',
    'ncat.traditional',
    'netcat',
    'hashcat',
    'nmap',
    'xprobe2',
    'dnstracer',
    'dnsenum',
    'dnsmap',
    'dnsspoof',
    'kali-linux-wireless',
    'kali-linux-web',
    'kali-linux-forensics',
    'ngrep',
    'tcpkill',
    'tshark',
    'wireshark',
    'libevent-dev'
]

def installer(apt_list):
    return
def main():
    options = """
    Reconnaisance
    Wireless Offensives and Evasion
    Web Application Attacks
    Remote Exploitation
    DNS Attacks/Enumeration
    Pivoting, Lateral Movement, Post-Exploitation
    Network Defense, Threat Assessment, and Pandemic Containment Methods
    Example:
        * Nested Virtualization with Qemu, Binwalk, KVM
        * Containerization with Docker, nvidia-docker, and Docker-Hashcat
    Tunneling, Encryption, Obfuscation, VPNs, and both Dynamic and Static Tunneling methods (Local and Remote forwarded)
    Network Daemon Fixes and other fix-its for Linux frustrations (Ubuntu-Kali-Debian builds)
    """
    menu = menu_parser(options)
    text_options = """
    INSTALL - Install a required python modules, frameworks, toolkits
    SIEM - Make makeshift Red-Teamer-Oriented SIEM's using improvised commands with watch, tail, etc.
    """
    print menu
    print text_options

    choice = str(raw_input(""))

    if choice == "INSTALL":

    dictOptions = menuparser(options)
    return
main()
