import os, sys
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    C = dict(ok=Fore.GREEN, err=Fore.RED, info=Fore.CYAN,
             warn=Fore.YELLOW, dim=Style.DIM, bold=Style.BRIGHT, reset=Style.RESET_ALL)
except ImportError:
    C = {k:"" for k in ["ok","err","info","warn","dim","bold","reset"]}

BANNER = r"""
 ######:                                           ##    ##                      . ####:
 #######               ##                          ##    ##                      #######:
 ##   :##              ##                          ##    ##                      #:.   ##
 ##    ##   :####    #######              :#####.  ##    ##   :###:##   :####          ##
 ##   :##   ######   #######             ########  ##    ##  .#######   ######         ##
 #######:   #:  :##    ##                ##:  .:#  ########  ###  ###   #:  :##    #####
 ######      :#####    ##                ##### .   ########  ##.  .##    :#####    #####.
 ##   ##.  .#######    ##                .######:  ##    ##  ##    ##  .#######        ##
 ##   ##   ## .  ##    ##                   .: ##  ##    ##  ##.  .##  ## .  ##        ##
 ##   :##  ##:  ###    ##.               #:.  :##  ##    ##  ###  ###  ##:  ###  #:    ##
 ##    ##: ########    #####             ########  ##    ##  .#######  ########  #######
 ##    ###   ###.##    .####             . ####    ##    ##   :###:##    ###.##  :#####:
                                                              #.  :##
                                                              ######
                                                              :####:
"""

def clear(): os.system("clear")
def banner(): print(BANNER)
def ok(m):   print(f"{C['ok']}[+] {m}{C['reset']}")
def err(m):  print(f"{C['err']}[!] {m}{C['reset']}")
def info(m): print(f"{C['info']}[*] {m}{C['reset']}")
def warn(m): print(f"{C['warn']}[~] {m}{C['reset']}")

def table(rows, headers):
    if not rows: print(f"{C['dim']}  (empty){C['reset']}"); return
    w = [len(h) for h in headers]
    for r in rows:
        for i, c in enumerate(r): w[i] = max(w[i], len(str(c)))
    sep = "+" + "+".join("-"*(x+2) for x in w) + "+"
    print(sep)
    print("|" + "|".join(f" {h.center(w[i])} " for i, h in enumerate(headers)) + "|")
    print(sep)
    for r in rows:
        print("|" + "|".join(f" {str(c).ljust(w[i])} " for i, c in enumerate(r)) + "|")
    print(sep)

def prompt(cid=None):
    if cid: return f"{C['info']}
