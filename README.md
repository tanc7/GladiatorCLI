# Gladiator CLI - Experimental Capture-the-Flag Framework

<code>
<pre>
Chang Tan
Lister Unlimited Cybersecurity Solutions, LLC.
changtan@listerunlimited.com
</pre>
</code>
Disclaimer: Project opened on May 14th. Development and drafting/design just begun.

Cost: Completely free

License: Copy-Left, completely open source

# What is GCLI?

GCLI is a collection of...

1. Tools
2. Tactics
3. Utilities
4. Exploits
5. Evasion Methods

Designed to assist participants in Capture-the-Flag type matches, commonly found in DEFCON meetups, either officially sanctioned or as a amateur circuit. GCLI is designed to be...

1. Fast
2. Self-sufficient
3. Reliable

To ensure that the participants of these games will never be without a tool or trick under their sleeve. GCLI is designed to cover all of the MAJOR disciplines of "hacking", and contains easy-to-access interfaces and toolkits to conduct

1. Wireless Attacks
2. Fast creation of SSH Tunnels, Ping/ICMP Tunnels, UDP Tunnels, Dynamic Proxies
3. Web Application Attacks
4. Vulnerability Scanning and Organization
5. Forensics and Counter-Forensics
6. Red Team operations
7. As well as having a unique "SIEM" designed to better favor the "intruder" rather than the "sheepdog".
8. Fuzzing
9. Pivoting and lateral movement through several techniques (Local Port Forwarding, Directory Traversal, Credential Reuse, Named Pipes)

# Disclaimer - Criminal usage of GladiatorCLI

Under no circumstances should GCLI be used for criminal acts. I did not and will not encourage the use of GCLI to conduct or perpetrate acts or campaigns of "cybercrime". GCLI would most certainly benefit a malicious threat actor, but it's real purpose is to be designed to better favor competitive teams with a strong offensive strategy.

GCLI is designed to be...

1. Usable in long-endurance matchups (DEFCON's official CTF teams)
2. Easy to understand and use
3. Effective and regularly tested and vetted for (reviewed periodically on a monthly basis)

# GCLI is not designed to...

1. Not designed to help script-kiddies. To use these tools, you need still, a base understanding of how the method, protocol, or concept works. This will NOT make one-shotting a unaware target easier if you do not know what to do next.

For example, the custom reverse-shells included still require a upgrade to a Remote Access Trojan/RAT, but it can also be interacted with on a basic level with netcat to provide the Red Teamers a root/sudo-capable shell. This is NOT a Meterpreter payload but it can be used to create Meterpreter payloads (as it is capable of running with root privileges allowing system-level root execution).

Proper usage of 'nohup <cmd> &' or '<cmd> 2>&1' will permit the operator to perform remotely controlled downloads and execution of a desired RAT in the enemy team.

Furthermore, that same victim could instead be turned into a DNS redirector should the game conditions and Rules of Engagement permit it. For example, should it be a competitor's enemy server, can be used to redirect traffic from ITSELF and it's PEERS into a socat relay that will downgrade encrypted traffic much like SSLProxy.

**For that reason, I have included a resources.list file, informing early adopters WHERE one can learn proper usage of these tactics. This can give your immediate team a major competitive advantage as your methods and vectors of attack are completely unorthodox and therefore, unpredictable.**

2. Not designed to assist or disrupt law enforcement forensics activities. While the modules in GCLI are indeed capable of immediately clearing your logs, and wiping your cache by shredding it (overwritten with zeroes), it is NOT a guarantee-or of being immune to prosecution. Such acts are immediately perceived as a attempted destruction of evidence.

**Such malignant actors, if I identify them, will be asked to leave and not use this toolkit. But furthermore, the very fact is, Law Enforcement has more than one simple data recovery resource, and such a bad actor must be prepared to disrupt forensically recoverable data following the Order of Volatility (from most volatile data source like caches to the least volatile, like physical hard disk sectors)**

3. Not designed to perform anything else outside of the role of CTF. You can choose to use GCLI as any way you deem fit, but I take no responsibility for anything that happens as a result of that. The techniques in GCLI WERE derived from my tactics that I used to evade pursuers in real-life, but times always change. New exploits, vulnerabilities (WebRTC defeats VPNs, and certain Tor implementations), are being discovered each and every day, even more so since early 2018.

For that reason I cannot provide any guarantees.

# Get ready for a huge installation file...

It's highly recommended to have your competitive machine set up as so...

a. A Ubuntu/Debian HOST machine
b. With a KVM Hypervisor running alongside of it
c. Micromanaging multiple VM instances of Kali Linux, Mac OSX, QEMU-binwalk embedded emulated routers, Windows 10, 8.1, 7, Professional, and Server 2016
d. Which then is running their own instances of Hyper-V (Nested Virtualization), DockerCE (Containerization), nvidia-docker, docker-hashcat
e. The HOST should be secured with UFW + IPTables
f. Network connectivity is provided via the virtual shell interface's commands, such as virsh net-start/autostart network, virsh start domain
g. **The security of such a system is physically protected using a Defense-in-Depth Concept**. If a attacker fails to breach the HOST but instead pwns a containerized hashcat instance, the attacker can't do anything more outside of being confined in the container because the container does not have the proper scripting or shell environments to enable pivoting and lateral movement (unless such a framework was BROUGHT with them into the session OR somehow installed)
h. **Future incursions and major breaches are "sealed off" by the operator**. Much like, how a ship can seal it's bulkheads when hit by a torpedo to prevent the entire ship from going down.

# Included toolkits and installers

The following toolkits have been documented and approved by the developer to be used and included in GCLI's installation. These toolkits are made by outside parties and I do not retain responsibility or credit for their work.

Unless the item in the list is marked PROPRIETARY, then the item is not my work.

1. socat
2. rpivot
3. sslproxy
4. ncat and netcat, and for Ubuntu, nc.traditional
5. sshuttle
6. KVM, libvirtd
7. Streisand, OpenVPN, WireGuard, Tor, Shadowsocks
8. Pupy, Metasploit Nightly, Webshells, Weevely
9. Django, Tornado-WebSockets, NodeJS
10. wifiphisher, KingPhisher, ghost-phisher, mana-toolkit, aircrack-suite, freeRADIUS, HostAPD, dnsmasq
11. Many toolkits available in the Kali Linux APT Repositories including but not limited to... hashcat, dnstracer, dnsrecon,
12. Proxychains 3 AND 4. Both are provided because **Proxychains3 can modify it's DNS nameservers**, and **Proxychains4 can create their own proxychains configuration** to be used. This means you can have "multiple-ways to play effectively" as well as tampering with your DNS resources used to resolve your proxies. For reliability, the tsocks transparent proxifier is automatically run as "tsocks proxychains4 -f config.conf <command>" so that it will allow certain non-proxy-aware apps to be forced into using proxychains.
13. **PROPRIETARY: ProxyShell**. Proxy management of HTTP, SOCKS4/4a/5, PHP, JavaScript Proxies and Proxy ARP Bridges.
14. **PROPRIETARY: GladiatorCLI**. Command-line interface to interface with every module in the Gladiator Framework. It supports spawning daemonized processes via subprocess forking, micromanagement of hypervisor resources, optimal default commands, tab-completion, database creation and management (using Django), remote automation of VPSes that can be acquired from Amazon Web Services/OnehostCloud/DigitalOcean/Vultr/Linode and numerous fixes for annoying Linux mishaps such as DNS daemon conflicts in Ubuntu/Debian
15. **PROPRIETARY: "Next-Gen Universal C2" (Name undecided)**. A in-development project for reverse shell and RAT command and control. The copy released in GCLI is a Open-Source design, loaded with experimental and unproven concepts. This C2 project is designed to be delivered via web-application exploits, and automatically upgrades, downgrades, pushes updates to reverse shells, and can remotely lock-down antimalware suites and intrusion detection systems. It also is capable of detecting forensic investigations and foreign attacker scans and will automatically "rotate" itself by spinning a new VPS using your Amazon IAM credentials, and migrating all of the victims and hosts and credentials to the new box on-its-own. It is heavily reliant on Streisand Framework and the Python 2.7/3.5 PExpect Module for self-automation.
16. **PROPRIETARY: "Blink"**. "Blink" is the signature and primary special ability utilized by the developer since January 2018 when he evaded his unidentified pursuers at the UNLV Campus, his own home, and in various informal "arenas" across the city of Las Vegas.

The developer, "Lister" has chosen to reveal the "magic behind blinking", because in the last week alone, numerous challengers have already demonstrated their own variations of Blink in a attempt to counter him. Including a arp-spoofing variant, a ip link swap variant, and a reflection/redirection variant.

**The seamless implementation of "Blink" without having any connectivity problems allows the user to immediately attack or "get the drop on" their former pursuers and take them on by surprise.**

This gives the developer's opponents the appearance that the person appears to be "teleporting, shapeshifting" or managed to "always attack someone from behind" even if the user appears to be "taking a serious beating" moments before. The usage of "Blink" gives the user the breathing-room they need to reassess the situation and come back prepared in just seconds.

# "Blink", Hostname/Network Daemon Variant (original)

"Blink" does three things...

1. Swap out the BURNED-IN MAC address after downing its own wireless card
2. Change the hostname WITHOUT requiring a reboot
3. Change the IP address

PRIOR to allowing the NIC to go back "up" and reconnecting back to Wi-Fi, without a hitch. The timing of the scripts and commands were designed to permit

1. Immediate reconnection back to target's wifi to rejoin the fight
2. Little to no DNS issues
3. Immediate formation of the correct routing tables
4. Fixed multiple issues with Ubuntu's DNS resolution by using a semi-permanent static DNS method

It can be configured to use common network manager daemons such as network-manager/NetworkManager, wicd, and wpa_supplicant.

Blink, requires:

(a) a working wireless connection
(b) no impeding Rules of Engagement forbidding disconnections or "relogging into wifi" from the gamemaker(s)
(c) Preferably a WPA2-PSK or WPA2-MGT/Enterprise/RADIUS WiFi network set as the "arena"
(d) And to have the Rules "allow wireless attacks".
(e) Also, disabling IPv6 support is PREFERABLE. As the octets of your IPv6 address contains your hardware MAC address. It's not that hard for your adversaries to immediately draw the connection from a unknown IPv6 address back to you if IPv6 is enabled.



17. **PROPRIETARY: Redteamer SIEM**. RSIEM is designed to address the shortcomings of the standard charts and graphs of a modern day SIEM used by Computer Incident Response Teams to make it "viable for the attacker".

SIEMs used by Blue-Teamers/Defenders are subject to informational overload and being unable to draw immediate conclusions out of the attack logs due to...  (a)Attacker's efforts to disrupt it, such as flooding it with packets (b) False positives, (c) Web application attacks, (d) Failures of either service daemons, or required subprocesses

**It should be noted that RSIEM is NOT a defender's toolkit! RSIEM trims the excessive output and verbosity of the standard SIEM and/or IDS/IPS/nDPI solution, to better assist penetration testers and Red Teamers in detecting response from incident response teams.**

When it comes to Blue versus Red, my conclusions and observations point that Red Teamers tend to "stay on the run" far more often, even when they are in the Exploitation/Post-Exploitation/Pivoting stage of a breach. The approximate, first twenty minutes of the initial breach are the most critical for the Red Teamer.

1. Either they can take advantage of their initial foothold and expand their presence across multiple networks, subnets, and gateways (switches, NATs, routers, dual-homed physical components, and bastion servers) using varying techniques like planting proxies and spreading malware via, example, a named pipe exploit or malicious Server Message Block shared folders (Windows SMB file sharing)...

2. Or they will die trying if the Incident Response Team reacts faster than predicted. Furthermore, the identified methods of attack and methods of exploitation will soon be extracted from memory dumps of the victim's hard disk (you can even dump memory yourself from the Task Manager).

The Red Teamer's abilities will eventually become fully developed the LONGER they reside within the compromised network, allowing them to compromise additional hosts and redirect legitimate traffic as well as silencing Indicators of Compromise (by killing off IDS's and tampering with, lets say... proxies and internally established network tunnels). But the Red Team needs time, and hopefully, lack of attention and notice.

From the start, the Blue Team has a major advantage in internal knowledge of the network and the resources they have on hand. They have privatized and proprietary tools such as Network Deep Packet Inspection, and multi-million dollar licenses to frameworks such as Rapid7's InsightIDR. Since IT IS the Blue Team's network, they have no restrictions on how, when, or what to use their resources on.

Red Teamers have LIMITED access to certain tools when entering the target's domain, depending on the toolkit's portability and size, and the vector used to bring such a tool with them like a Proxy-Tunnel interacting with nmap and nikto, and the proxy-awareness of the app or it's support of transparent proxifiers. Nmap scans can be conducted remotely without having to bring or install the tool, by running it through a dynamically forwarded SSH SOCKS4/5 proxy with a initially compromised victim acting as a "jump-box" or "pivot".

*Aside from that, Red Teamers have only whats in the victim's environment to use. What I say that, I mean go open your Linux terminal, and type "env", "echo $SHELL", "which python", "which ruby", "which php", "which nodejs". What you see from that, is what your attacker will have at hand.*

**I would like to remind you, this is not a framework for pentesting or criminal acts**.

# RSIEM's purpose

RSIEM is meant to be a attempt to create a "decent early-warning system" for the Red Team. It's much like.... being in a fireteam of United States Colonial Marines, equipped with motion trackers on their pulse rifles, and being stalked by killer Xenomorphs and facehuggers across the ship.

"I sure as hell do not want the bugs to get the drop on me. I'd rather get warned ahead of time before my head gets eaten by their inner jaws. Or birth a chestburster."

RSIEM is designed to analyze ongoing attack traffic (from you basically) to search for the conditions that indicate... the arrival of a Incident Response Team. It filters out the irrelevant and quite-often disruptive, verbose output and only shows you the RELEVANT data that you need to know, NOW.

TLDR. It tells you, "wee-woo, GTFO now!"
