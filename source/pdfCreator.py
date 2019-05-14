from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from barchartCreator import barchartCreator
import os
import sys
import socket
class pdfCreator:

    def __init__(self,date):
        self.doc = SimpleDocTemplate("output/report-" + date + ".pdf",
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=72,
                            bottomMargin=18)
        print("[*] Initialized pdfCreator")

    def addImage(self, date, datatype, flowable):
        try:
            imgname = "output/" + date + "-" + datatype + ".jpeg"
            im = Image(imgname, width=500,height=350)
            im.hAlign = "CENTER"
            flowable.append(im)
            print("[*] added " + imgname + " to PDF report")
            return flowable
        except:
            f = open("output/error.log", "w")
            f.write(str(sys.exc_info()))
            f.write( "\n" + str(sys.exc_info()[1]))
            print("[!] Error while adding image to PDF report")
            sys.exit
    
    def addTop15List(self, data, title, flowable):
        try:
            styles = getSampleStyleSheet()
            flowable.append(Spacer(20,20))
            flowable.append(Paragraph(title, styles["Heading2"]))
            for c,x in enumerate(data):
                isp_string = str(c+1) + ". " + str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(isp_string, style=styles["Normal"])
                flowable.append(p)
            print("[*] Added '" + title + "' Paragraph to report")
            return flowable
        except:
            f = open("output/error.log", "w")
            f.write(str(sys.exc_info()))
            f.write( "\n" + str(sys.exc_info()[1]))
            print("[!] Error while adding '" + title + "' Paragraph to report")
            sys.exit


    def generateReport(self,date,data):
        try:
            styles = getSampleStyleSheet()
            flowables = []
            str_arr = ["Date: " + date, 
                        " ContainerID: " + socket.gethostname(), 
                        " Ips Total: " + str(len(data)) ]
            for string in str_arr:
                para = Paragraph(string, style=styles["Normal"])
                flowables.append(para)
            bc = barchartCreator()
            # Internet Service Provider
            isp = bc.getTop15(data, "isp")
            flowables = self.addTop15List(isp, "Internet service providers top 15", flowables)
            # Autonomous System
            as_data = bc.getTop15(data, "as")
            flowables = self.addTop15List(as_data, "Autonomous system Top 15", flowables)            
            # Timezone
            timezone = bc.getTop15(data, "timezone")
            flowables = self.addTop15List(timezone, "Timezones Top 15", flowables) 
            # Organization
            organization = bc.getTop15(data, "org")
            flowables = self.addTop15List(organization, "Organizations Top 15", flowables) 
            # Countries
            countries = bc.getTop15(data, "country")
            flowables = self.addTop15List(countries, "Countries Top 15", flowables) 
            # Add image
            flowables = self.addImage(date, "country",flowables)
            self.doc.build(flowables)
            print("[*] PDF report generated to output/report-" + date + ".pdf")
        except:
            f = open("output/error.log", "w")
            f.write(str(sys.exc_info()))
            f.write( "\n" + str(sys.exc_info()[1]))
            print("[!] Error while generating PDF report")
            sys.exit

