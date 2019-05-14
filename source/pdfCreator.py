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
            print("[*] added " + imgname + "to PDF report")
            return flowable
        except:
            f = open("output/error.log", "w")
            f.write(str(sys.exc_info()))
            f.write( "\n" + str(sys.exc_info()[1]))
            print("[!] Error while adding image to PDF report")
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
            # Space between paragraphs
            flowables.append(Spacer(20,20))
            # Add Data
            bc = barchartCreator()
            # Internet Service Provider
            flowables.append(Paragraph("Internet service providers top 15", styles["Heading2"]))
            isp = bc.getTop15(data, "isp")
            for c,x in enumerate(isp):
                isp_string = str(c+1) + ". " + str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(isp_string, style=styles["Normal"])
                flowables.append(p)
            # Autonomous System
            flowables.append(Spacer(20,20))
            flowables.append(Paragraph("Autonomous system Top 15", styles["Heading2"]))
            as_data = bc.getTop15(data, "as")
            for c,x in enumerate(as_data):
                as_string = str(c+1) + ". " + str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(as_string, style=styles["Normal"])
                flowables.append(p)
            # timezone
            flowables.append(Spacer(20,20))
            flowables.append(Paragraph("Timezones Top 15", styles["Heading2"]))
            timezone = bc.getTop15(data, "timezone")
            for c,x in enumerate(timezone):
                timezone_string = str(c+1) + ". " + str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(timezone_string, style=styles["Normal"])
                flowables.append(p)
            # Organization
            flowables.append(Spacer(20,45))
            flowables.append(Paragraph("Organizations Top 15", styles["Heading2"]))
            organization = bc.getTop15(data, "org")
            for c,x in enumerate(organization):
                organization_string = str(c+1) + ". " + str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(organization_string, style=styles["Normal"])
                flowables.append(p)
            # countries
            flowables.append(Spacer(20,20))
            flowables.append(Paragraph("Countries Top 15", styles["Heading2"]))
            timezone = bc.getTop15(data, "country")
            for c,x in enumerate(timezone):
                country_string = str(c+1) + ". " + str(x[0]) + " : " + str(x[1]) + "\n"
                p = Paragraph(country_string, style=styles["Normal"])
                flowables.append(p)
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

