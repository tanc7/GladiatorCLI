import os, sys, socket, operator, subprocess, threading
from termcolor import colored
def menu_parser(menu):
    options_list = {}
    menu = str(menu)
    menu = menu.splitlines()
    counter = 1
    for item in menu:
        option = str(item.encode('utf-8')).rstrip().strip()
        print '\t\t',str(counter),'\t\t\t',option
        options_list[counter] = option
        counter += 1
    print options_list
    return options_list
def popen_background(cmd):
    p = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o = p.stdout.read()
    e = p.stderr.read()
    o = str(o.encode('utf-8')).strip().rstrip()
    e = str(e.encode('utf-8')).strip().rstrip()
    output = o + e
    return output
def bash_cmd(cmd):
    subprocess.call(cmd, shell=True, executable='/bin/bash')
    return

def ruby_cmd(cmd):
    return

def nodejs_cmd(cmd):
    return

def py_cmd(cmd):
    return
