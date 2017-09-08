#!/usr/bin/env python3

#
# Copyright (c) 2017 HappinessLab
# Created by Shota Shimazu on 2017/09/08
#

import subprocess
import os
import shutil

try:
    import pexpect
except:
    print("Failed to import pexpect. Please install pexpect before.")


if __name__ == "__main__":

    print("Please remove this line if you use on production server.")
    print("Do not run this script on developing computer.")
    exit(1)


    print("Cleaning existing site...")
    if os.path.exists("./testing/"):
        shutil.rmtree("./testing")

    subprocess.call(["git", "clone", "https://hplab.work/HpLab/web-site.git"])
