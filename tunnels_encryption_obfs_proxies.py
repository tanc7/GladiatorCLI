import gla_library

enable_pchain_gen = True
def proxychain_generator(host, port, proxyport, proxytype, action):
    proxychain_ver = "proxychains4"
    homepath = popen_background("echo $HOME")

    conf_defaults = "/etc/proxychains.conf"
    conf_file = "{homepath}/proxychains.conf".format(str(homepath))
    if action == "add":
        line = "{proxytype} {host} {proxyport}"
        r = open(conf_file,'a+')
        o = r.read()
        o = str(o.encode('utf-8')).strip().rstrip()
        if re.search(line, o):
            pass
        else:
            r.write(line)

        r.close()

    elif action == "delete":
        line = "{proxytype} {host} {proxyport}"

        r = open(conf_file,'a+')
        o = r.read()
        o = o.splitlines()
        for line in o:
            if re.search(line, o):
                o.remove(line)
            r.write(line)
        r.close()
    else:
        proxychain_generator(host, port, proxyport, action)
    return
def generate_pchain_check(enable_pchain_gen, host, port, proxyport, proxytype, action):
    if enable_pchain_gen == True:
        proxychain_generator(host, port, proxyport, proxytype, action)
    else:
        pass
    return
def main():
    proxytracker = True
    options = """
    ### Offensive

    SSLProxy
    SSLDump
    tshark
    ngrep

    webmitm

    ### Tunnel Creation

    (Enabled={enable_pchain_gen}) ProxyTracker, automatically edit your proxychains on proxychains4 as you go through these menu options

    socat commands, useful socat commands
    Streisand OpenVPN + Custom AWS Jump-Server
    Streisand Tor + Custom AWS Tor Relay
    Streisand WireGuard + Custom AWS Jump-Server
    Ssshuttle, Auto-create SSH tunnels, both Locally Forwarded and Reverse
    SSH Tunnel, Dynamic, with Proxychains
    SSH Tunnel, Local-Forwarded
    SSH Tunnel, Local-Reversed
    HTTP Tunnel, ncat, local
    HTTP Tunnel, ncat, authenticated
    """

    return
main()
