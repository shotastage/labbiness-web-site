#!/usr/bin/env python3

from ftplib import FTP
import os


# FTP Login Information
ftp = FTP('ftp.homepage.shinobi.jp')
ftp.login('hplab2test0page.uijin.com','226c028e67b35156e51c12efc3e5f3b3')


print("Current FTP Files:")
print(ftp.nlst())




print("Uploading...")

upload_files = [
    "index.html"
]

for up_file in upload_files:
    with open("../dist/" + up_file, "rb") as f:
        ftp.storlines("STOR /" + up_file, f)



print("Open http://hplab2test0page.uijin.com")
ftp.quit()
