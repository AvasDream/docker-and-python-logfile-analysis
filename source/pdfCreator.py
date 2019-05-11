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
            # Space between paragraphs
            flowables.append(Spacer(20,20))
            # Add Data
            bc = barchartCreator()
            # Internet Service Provider
            isp = bc.getTop15(data, "isp")
            for x in isp:
                isp_string = str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(isp_string, style=styles["Normal"])
                flowables.append(p)
            # Autonomes System
            flowables.append(Spacer(20,20))
            as_data = bc.getTop15(data, "as")
            for x in as_data:
                as_string = str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(as_string, style=styles["Normal"])
                flowables.append(p)
            # timezone
            flowables.append(Spacer(20,20))
            timezone = bc.getTop15(data, "timezone")
            for x in timezone:
                timezone_string = str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(timezone_string, style=styles["Normal"])
                flowables.append(p)
            # Organization
            flowables.append(Spacer(20,45))
            organization = bc.getTop15(data, "org")
            for x in organization:
                organization_string = str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(organization_string, style=styles["Normal"])
                flowables.append(p)
            # countires
            flowables.append(Spacer(20,20))
            timezone = bc.getTop15(data, "country")
            for x in timezone:
                country_string = str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(country_string, style=styles["Normal"])
                flowables.append(p)
            self.doc.build(flowables)
        except:
            f = open("output/error.log", "w")
            f.write(str(sys.exc_info()))
            f.write( "\n" + str(sys.exc_info()[1]))
            print("[!] Error while initializing pdf file")
            sys.exit

