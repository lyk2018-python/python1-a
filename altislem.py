import subprocess
import time

"""
cikti = subprocess.run(["df","-h"],stdout=subprocess.PIPE)

print(cikti.stdout.decode("utf-8"))
"""
gecmis_islem = ""
while True:
    p1 = subprocess.Popen(["dmesg"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "usb"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    output = p2.communicate()[0]
    son_satir = output.decode("utf-8").split("\n")[-2]
    son_islem = son_satir.split("[")[1].split("]")[0]
    if gecmis_islem != son_islem:
        gecmis_islem = son_islem
        print(son_satir)
    time.sleep(2)
