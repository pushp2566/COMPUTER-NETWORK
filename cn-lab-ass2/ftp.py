from ftplib import FTP
import os

ftp = FTP("ftp.dlptest.com",encoding="latin-1")
ftp.login("dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")

print("Files on server:")
ftp.retrlines("LIST")

# Upload a file
if os.path.exists("test.txt"):
    with open("test.txt", "rb") as f:
        ftp.storbinary("STOR test.txt", f)
        print("File uploaded")
else:
    print("test.txt not found for upload")

# Download file
with open("downloaded.txt", "wb") as f:
    ftp.retrbinary("RETR test.txt", f.write)
    print("File downloaded")

ftp.quit()

