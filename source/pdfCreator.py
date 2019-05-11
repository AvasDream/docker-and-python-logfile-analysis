from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import sys
import socket
class pdfCreator:

    def __init__(self):
        print("[*] Initialized pdfCreator")
    
    def addBasicInfo(self,date):
        try:
            filename = "output/report-" + date +".pdf"
            canv = canvas.Canvas(filename, pagesize=letter)
            canv.drawString(100,750, "Date: " + date \
                + " ContainerID: " + socket.gethostname())
            canv.save()
        except:
            f = open("output/error.log", "w")
            f.write(str(sys.exc_info()))
            f.write( "\n" + str(sys.exc_info()[1]))
            print("[!] Error while initializing pdf file")
            sys.exit