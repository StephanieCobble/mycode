#!/usr/bin/env python3
'''
StephanieCobble | Lab 54 - Copying Files & Folders using shutil and os from standard library 
'''

import shutil
import os

def main(): 
    
    # move into working directory 
    os.chdir("/home/student/mycode/")
    # to copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    # to copy a folder and all folders/files in it. Copy directoryA to directoryB
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__== "__main__":
    main()
