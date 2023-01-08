#!/usr/bin/env python3
'''
Stephanie Cobble | Lab 55 - Moving & renaming files & folders
'''

import shutil
import os

def main():
    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')
    
    # rename based off of user input & move with new name saved
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
    

if __name__ == "__main__":
    main()
