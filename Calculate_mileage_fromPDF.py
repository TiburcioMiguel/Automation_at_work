#!/usr/bin/env python3

## This is to test out the idea I have for
## automating the mileage sheet process for FCUSD
import sys
from PyPDF2 import PdfReader
## Creating the lists that contain the distance between 2 sites
distance_one = ["FHE", "SJG", 4.1]
distance_two = ["SJG", "EOE", 5.2]
distance_three = ["EOE", "BSE", 4]
distance_four = ["FHE", "EOE", 2]
distance_five = ["FHE", "BSE", 2.7]
distance_six =["FHE", "ESC", 6.7]
distance_seven = ["FHE", "SMS", 3.4]
distance_eight = ["FHE", "CSE", 3.5]
distance_nine = ["FHE", "NSE", 4.9]
distance_ten = ["FHE", "FHS", 4.8]
distance_eleven = ["FHE", "RRE", 4.2]
distance_twelve = ["FHE", "VDLHS", 3.7]
distance_thirteen = ["FHE", "FMS", 2.1]
distance_fourteen = ["FHE", "TJE", 2.9]
distance_fifteen = ["FHE", "MRE", 6.2]
distance_sixteen = ["FHE", "OCE", 2.5]
distance_seventeen = ["FHE", "GRE", 3.8]
distance_eighteen = ["SJG", "BSE", 2.6]
distance_nineteen = ["SJG", "MRE", 5.3]
distance_twenty = ["SJG", "OCE", 3.1]
distance_twentyone = ["SJG", "GRE", 2.5]
distance_twentytwo = ["SJG", "SMS", 2.4]
distance_twentythree = ["SJG", "CSE", 5]
distnace_twentyfour = ["SJG", "FHS", 0.8]
distance_twentyfive = ["SJG", "NSE", 2]
distance_twentysix = ["SJG", "VDLHS", 3.8]
distance_twentyseven = ["SJG", "RRE", 4.6]
distance_twentyeight = ["SJG", "FMS", 2.2]
distance_twentynine = ["SJG", "TJE", 2.5]
distance_thirty = ["SJG", "ESC", 3.2]
distance_thirtyone = ["EOE", "ESC", 8.6]
distance_thirtytwo = ["EOE", "MRE", 5.1]
distance_thirtythree = ["EOE", "OCE", 1.7]
distance_thirtyfour = ["EOE", "GRE", 3.3]
distance_thirtyfive = ["EOE", "SMS", 4.8]
distance_thirtysix = ["EOE", "CSE", 5]
distance_thirtyseven = ["EOE", "FHS", 5.8]
distance_thirtyeight = ["EOE", "NSE", 6.3]
distance_thirtynine = ["EOE", "VDLHS", 1.9]
distance_fourty = ["EOE", "RRE", 2.4]
distance_fortyone = ["EOE", "FMS", 3.5]
distance_fortytwo = ["EOE", "TJE", 4.8]
distance_fortythree = ["BSE","ESC", 5]
distance_fortyfour = ["BSE", "MRE", 5.7]
distance_fortyfive = ["BSE", "OCE", 2.5]
distance_fortysix = ["BSE", "GRE", 3.2]
distance_fortyseven = ["BSE", "SMS", 1.7]
distance_fortyeight = ["BSE", "CSE", 3.8]
distance_fortynine = ["BSE", "FHS", 3.2]
distance_fifty = ["BSE", "NSE", 3.2]
distance_fiftyone = ["BSE", "VDLHS", 4.1]
distance_fiftytwo = ["BSE", "RRE", 6.1]
distance_fiftythree = ["BSE", "FMS", 1.2]
distance_fiftyfour = ["BSE", "TJE", 1.2]
distance_fiftyfive = ["BSE", "FLHS", 2.7]
distance_fiftysix = ["MRE", "ESC", 7.5]
distance_fiftyseven = ["MRE", "OCE", 5.1]
distance_fiftyeight = ["MRE", "GRE", 3.8]
distance_fiftynine = ["MRE", "SMS", 5.8]
distance_sixty = ["MRE", "CSE", 9.7]
distance_sixtyone = ["MRE", "FHS", 4.7]
distance_sixtytwo = ["MRE", "FLHS", 5.4]
distance_sixtythree = ["MRE", "NSE", 7.5]
distance_sixtyfour = ["MRE", "VDLHS", 3.7]
distance_sixtyfive = ["MRE", "RRE", 3.9]
distance_sixtysix = ["MRE", "FMS", 5.3]
distance_sixtyseven = ["MRE", "TJE", 6]
distance_sixtyeight = ["OCE", "GRE", 2.6]
distance_sixtynine = ["OCE", "SMS", 3]
distance_seventy = ["OCE", "CSE", 5.9]
distance_seventyone = ["OCE", "FHS", 4]
distance_seventytwo = ["OCE", "FLHS", 3.5]
distance_seventythree = ["OCE", "NSE", 4.1]
distance_seventyfour = ["OCE", "VDLHS", 2.9]
distance_seventyfive = ["OCE", "RRE", 3.5]
distance_seventysix = ["OCE", "FMS", 1.5]
distance_seventyseven = ["OCE", "TJE", 2.9]
distance_seventyeight = ["GRE", "SMS", 3]
distance_seventynine = ["GRE", "CSE", 5.9]
distance_eighty = ["GRE", "FHS", 4.2]
distance_eightyone = ["GRE", "FLHS", 3.5]
distance_eightytwo = ["GRE", "NSE", 4.3]
distance_eightythree = ["GRE", "VDLHS", 2.9]
distance_eightyfour = ["GRE", "RRE", 3.9]
distance_eightyfive = ["GRE", "FMS", 1.5]
distance_eightysix = ["GRE", "TJE", 2.9]
distance_eightyseven = ["SMS", "CSE", 5.9]
distance_eightyeight = ["SMS", "FHS", 4]
distance_eightynine = ["SMS", "FLHS", 3.5]
distance_ninety = ["SMS", "NSE", 4.3]
distance_ninetyone = ["SMS", "VDLHS", 2.9]
distance_ninetytwo = ["SMS", "RRE", 3.9]
distance_ninetythree = ["SMS", "FMS", 1.5]
distance_ninetyfour = ["SMS", "TJE", 2.9]
distance_ninetyfive = ["CSE", "FHS", 4.2]
distance_ninetysix = ["CSE", "FLHS", 3.5]
distance_ninetyseven = ["CSE", "NSE", 4.4]
distance_ninetyeight = ["CSE", "VDLHS", 2.9]
distance_ninetynine = ["CSE", "RRE", 3.9]
distance_hundred = ["CSE", "FMS", 1.5]
distance_hundredone = ["CSE", "TJE", 2.9]
distance_hundredtwo = ["OCE", "ESC", 6.1]
distance_hundredthree = ["GRE", "ESC", 5.9]
distance_hundredfour = ["SMS", "ESC", 5.1]
distance_hundredfive = ["CSE", "ESC", 5.6]
distance_hundredsix = ["FHS", "ESC", 3.1]
distance_hundredseven = ["FHS", "FLHS", 1]
distance_hundredeight = ["FHS", "NSE", 1.8]
distance_hundrednine = ["FHS", "VDLHS", 3.7]
distance_hundredten = ["FHS", "RRE", 4.7]
distance_hundredeleven = ["FHS", "FMS", 2.8]
distance_hundredtwelve = ["FHS", "TJE", 2.7]
distance_hundredthirteen = ["NSE", "ESC", 3.1]
distance_hundredfourteen = ["NSE", "VDLHS", 3.7]
distance_hundredfifteen = ["NSE", "RRE", 4.9]
distance_hundredsixteen = ["NSE", "FMS", 2.8]
distance_hundredseventeen = ["NSE", "TJE", 2.7]
distance_hundredeighteen = ["VDLHS", "ESC", 3.1]
distance_hundrednineteen = ["VDLHS", "RRE", 4.9]
distance_hundredtwenty = ["VDLHS", "FMS", 2.8]
distance_hundredtwentyone = ["VDLHS", "TJE", 2.7]
distance_hundredtwentytwo = ["RRE", "ESC", 7.4]
distance_hundredtwentythree = ["RRE", "FMS", 4.8]
distance_hundredtwentyfour = ["RRE", "TJE", 6.5]
distance_hundredtwentyfive = ["FMS", "ESC", 5.5]
distance_hundredtwentysix = ["FMS", "TJE", 1.6]
distance_hundredtwentyseven = ["TJE", "ESC", 4.3]
d_one = ["CEC", "BSE", 10]
d_two = ["CEC", "CSE", 11]
d_three = ["CEC", "CGE", 2]
d_four = ["CEC", "CHS", 2]
d_five = ["CEC", "CLC", 1]
d_six = ["CEC", "CME", 3]
d_seven = ["CEC", "CVE", 3]
d_eight = ["CEC", "ESC", 6]
d_nine = ["CEC", "FLHS", 9.5]
d_ten = ["CEC", "EOE", 14]
d_eleven = ["CEC", "FHS", 9]
d_twelve = ["CEC", "FHE", 12]
d_thirteen = ["CEC", "FMS", 10]
d_fourteen = ["CEC", "SJG", 10]
d_fifteen = ["CEC", "GRE", 11]
d_sixteen = ["CEC", "KHS", 1]
d_seventeen = ["CEC", "MHE", 8]
d_eighteen = ["CEC", "MMS", 2]
d_ninenteen = ["CEC", "MtMS", 1]
d_twenty = ["CEC", "NSE", 7]
d_twentyone = ["CEC", "NVE", 3]
d_twentytwo = ["CEC", "OCE", 14]
d_twentythree = ["CEC", "PJS", 2]
d_twentyfour = ["CEC", "RCE", 1]
d_twentyfive = ["CEC", "RVE", 2]
d_twentysix = ["CEC", "RRE", 12]
d_twentyseven = ["CEC", "SMS", 9.5]
d_twentyeight = ["CEC", "TJE", 10]
d_twentynine = ["CEC", "VDLHS", 12]
d_thirty = ["CEC", "WRE", 2]
d_thirtyone = ["CEC", "WME", 1]
dcge_one = ["CGE", "BSE", 13]
dcge_two = ["CGE", "CSE", 14]
dcge_three = ["CGE", "CHS", 1]
dcge_four = ["CGE", "CLC", 2]
dcge_five = ["CGE", "CME", 1]
dcge_six = ["CGE", "CVE", 2]
dcge_seven = ["CGE", "ESC", 9]
dcge_eight = ["CGE", "FLHS", 12]
dcge_nine = ["CGE", "EOE", 16]
dcge_ten = ["CGE", "FHS", 12]
dcge_eleven = ["CGE", "FHE", 15]
dcge_twelve = ["CGE", "FMS", 13]
dcge_thirteen = ["CGE", "SJG", 12]
dcge_fourteen = ["CGE", "GRE", 14]
dcge_fifteen = ["CGE", "KHS", 3]
dcge_sixteen = ["CGE", "MHE", 6]
dcge_seventeen = ["CGE", "MMS", 1]
dcge_eighteen = ["CGE", "MtMS", 3]
dcge_nineteen = ["CGE", "NSE", 10]
dcge_twenty = ["CGE", "NVE", 3.5]
dcge_twentyone = ["CGE", "OCE", 14]
dcge_twentytwo = ["CGE", "PJS", 1]
dcge_twentythree = ["CGE", "RCE", 1]
dcge_twentfour = ["CGE", "RVE", 2]
dcge_twentyfive = ["CGE", "RRE", 15]
dcge_twentysix = ["CGE", "SMS", 12]
dcge_twentyseven = ["CGE", "TJE", 13]
dcge_twentyeight = ["CGE", "VDLHS", 15]
dcge_twentynine = ["CGE", "WRE", 1]
dcge_thirty = ["CGE", "WME", 2]
dchs_one = ["CHS", "BSE", 13]
dchs_two = ["CHS", "CSE", 13]
dchs_three = ["CHS", "CLC", 2]
dchs_four = ["CHS", "CME", 1]
dchs_five = ["CHS", "CVE", 3]
dchs_six = ["CHS", "ESC", 9.5]
dchs_seven = ["CHS", "FLHS", 12.5]
dchs_eight = ["CHS", "EOE", 16]
dchs_nine = ["CHS", "FHS", 11]
dchs_ten = ["CHS", "FHE", 15]
dchs_eleven = ["CHS", "FMS", 12]
dchs_twelve = ["CHS", "SJG", 12]
dchs_thirteen = ["CHS", "GRE", 13]
dchs_fourteen = ["CHS", "KHS", 3]
dchs_fifteen = ["CHS", "MHE", 9]
dchs_sixteen = ["CHS", "MMS", 1]
dchs_seventeen = ["CHS", "MtMS", 3]
dchs_eighteen = ["CHS", "NSE", 10]
dchs_nineteen = ["CHS", "NVE", 3.5]
dchs_twenty = ["CHS", "OCE", 16]
dchs_twentyone = ["CHS", "PJS", 1]
dchs_twentytwo = ["CHS", "RCE", 1]
dchs_twentythree = ["CHS", "RVE", 2]
dchs_twentyfour = ["CHS", "RRE", 14.5]
dchs_twentyfive = ["CHS", "SMS", 12.5]
dchs_twentysix = ["CHS", "TJE", 12]
dchs_twentyseven = ["CHS", "VDLHS", 14]
dchs_twentyeight = ["CHS", "WRE", 2]
dchs_twentynine = ["CHS", "WME", 2]
dclc_one = ["CLC", "BSE", 11]
dclc_two = ["CLC", "CSE", 11]
dclc_three = ["CLC", "CME", 3]
dclc_four = ["CLC", "CVE", 3]
dclc_five = ["CLC", "ESC", 5.5]
dclc_six = ["CLC", "FLHS", 9]
dclc_seven = ["CLC", "EOE", 14]
dclc_eight = ["CLC", "FHS", 9]
dclc_nine = ["CLC", "FHE", 12]
dclc_ten = ["CLC", "FMS", 10]
dclc_eleven = ["CLC", "SJG", 10]
dclc_twelve = ["CLC", "GRE", 11]
dclc_thirteen = ["CLC", "KHS", 1]
dclc_fourteen = ["CLC", "MHE", 8]
dclc_fifteen = ["CLC", "MMS", 1]
dclc_sixteen = ["CLC", "MtMS", 1]
dclc_seventeen = ["CLC", "NSE", 8]
dclc_eighteen = ["CLC", "NVE", 2.5]
dclc_nineteen = ["CLC", "OCE", 12]
dclc_twenty = ["CLC", "PJS", 1]
dclc_twentyone = ["CLC", "RCE", 1]
dclc_twentytwo = ["CLC", "RVE", 2]
dclc_twentythree = ["CLC", "RRE", 12.5]
dclc_twentyfour = ["CLC", "SMS", 9]
dclc_twentyfive = ["CLC", "TJE", 10]
dclc_twentysix = ["CLC", "VDLHS", 12.5]
dclc_twentyseven = ["CLC", "WRE", 2]
dclc_twentyeight = ["CLC", "WME", 1]
dcme_one = ["CME", "BSE", 13]
dcme_two = ["CME", "CSE", 14]
dcme_three = ["CME", "CVE", 2]
dcme_four = ["CME", "ESC", 9.5]
dcme_five = ["CME", "FLHS", 12]
dcme_six = ["CME", "EOE", 16]
dcme_seven = ["CME", "FHS", 12]
dcme_eight = ["CME", "FHE", 15]
dcme_nine = ["CME", "FMS", 13]
dcme_ten = ["CME", "SJG", 12]
dcme_eleven = ["CME", "GRE", 13]
dcme_twelve = ["CME", "KHS", 3]
dcme_thirteen = ["CME", "MHE", 6]
dcme_fourteen = ["CME", "MMS", 2]
dcme_fifteen = ["CME", "MtMS", 5]
dcme_sixteen = ["CME", "NSE", 10]
dcme_seventeen = ["CME", "NVE", 4]
dcme_eighteen = ["CME", "OCE", 14]
dcme_nineteen = ["CME", "PJS", 3]
dcme_twenty = ["CME", "RCE", 2]
dcme_twentyone = ["CME", "RVE", 3]
dcme_twentytwo = ["CME", "RRE", 15]
dcme_twentythree = ["CME", "SMS", 12]
dcme_twentyfour = ["CME", "TJE", 12]
dcme_twentyfive = ["CME", "VDLHS", 15]
dcme_twentysix = ["CME", "WRE", 1]
dcme_twentyseven = ["CME", "WME", 3]
dcve_one = ["CVE", "BSE", 13]
dcve_two = ["CVE", "CSE", 14]
dcve_three = ["CVE", "ESC", 8]
dcve_four = ["CVE", "FLHS", 10.5]
dcve_five = ["CVE", "EOE", 15]
dcve_six = ["CVE", "FHS", 11]
dcve_seven = ["CVE", "FHE", 13]
dcve_eight = ["CVE", "FMS", 11]
dcve_nine = ["CVE", "SJG", 12]
dcve_ten = ["CVE", "GRE", 12]
dcve_eleven = ["CVE", "KHS", 2]
dcve_twelve = ["CVE", "MHE", 5]
dcve_thirteen = ["CVE", "MMS", 3]
dcve_fourteen = ["CVE", "MtMS", 4]
dcve_fifteen = ["CVE", "NSE", 9]
dcve_sixteen = ["CVE", "NVE", 2]
dcve_seventeen = ["CVE", "OCE", 13]
dcve_eighteen = ["CVE", "PJS", 3]
dcve_nineteen = ["CVE", "RCE", 2]
dcve_twenty = ["CVE", "RVE", 4]
dcve_twentyone = ["CVE", "RRE", 14]
dcve_twentytwo = ["CVE", "SMS", 10.5]
dcve_twentythree = ["CVE", "TJE", 11]
dcve_twentyfour = ["CVE", "VDLHS", 14]
dcve_twentyfive = ["CVE", "WRE", 2]
dcve_twentysix = ["CVE", "WME", 3]
dkhs_one = ["KHS", "BSE", 10]
dkhs_two = ["KHS", "CSE", 10]
dkhs_three = ["KHS", "ESC", 5]
dkhs_four = ["KHS", "FLHS", 8]
dkhs_five = ["KHS", "EOE", 13]
dkhs_six = ["KHS", "FHS", 8]
dkhs_seven = ["KHS", "FHE", 11]
dkhs_eight = ["KHS", "FMS", 9]
dkhs_nine = ["KHS", "SJG", 9]
dkhs_ten = ["KHS", "GRE", 10]
dkhs_eleven = ["KHS", "MHE", 7]
dkhs_twelve = ["KHS", "MMS", 3]
dkhs_thirteen = ["KHS", "MtMS", 2]
dkhs_fourteen = ["KHS", "NSE", 7]
dkhs_fifteen = ["KHS", "NVE", 2.5]
dkhs_sixteen = ["KHS", "OCE", 13]
dkhs_seventeen = ["KHS", "PJS", 2]
dkhs_eighteen = ["KHS", "RCE", 1]
dkhs_nineteen = ["KHS", "RVE", 2]
dkhs_twenty = ["KHS", "RRE", 11.5]
dkhs_twentyone = ["KHS", "SMS", 8]
dkhs_twentytwo = ["KHS", "TJE", 9]
dkhs_twentythree = ["KHS", "VDLHS", 11.5]
dkhs_twentyfour = ["KHS", "WRE", 2]
dkhs_twentyfive = ["KHS", "WME", 1]
dmhe_one = ["MHE", "BSE", 16]
dmhe_two = ["MHE", "CSE", 16]
dmhe_three = ["MHE", "ESC", 11]
dmhe_four = ["MHE", "FLHS", 14]
dmhe_five = ["MHE", "EOE", 19]
dmhe_six = ["MHE", "FHS", 14]
dmhe_seven = ["MHE", "FHE", 17]
dmhe_eight = ["MHE", "FMS", 15]
dmhe_nine = ["MHE", "SJG", 15]
dmhe_ten = ["MHE", "GRE", 16]
dmhe_eleven = ["MHE", "MMS", 9]
dmhe_twelve = ["MHE", "MtMS", 8]
dmhe_thirteen = ["MHE", "NSE", 13]
dmhe_fourteen = ["MHE", "NVE", 4]
dmhe_fifteen = ["MHE", "OCE", 19]
dmhe_sixteen = ["MHE", "PJS", 8]
dmhe_seventeen = ["MHE", "RCE", 8]
dmhe_eighteen = ["MHE", "RVE", 7]
dmhe_ninenteen = ["MHE", "RRE", 15]
dmhe_twenty = ["MHE", "SMS", 14]
dmhe_twentyone = ["MHE", "TJE", 16]
dmhe_twentytwo = ["MHE", "VDLHS", 15]
dmhe_twentythree = ["MHE", "WRE", 6]
dmhe_twentyyfour = ["MHE", "WME", 9]
dmms_one = ["MMS", "BSE", 13]
dmms_two = ["MMS", "CSE", 13]
dmms_three = ["MMS", "ESC", 8]
dmms_four = ["MMS", "FLHS", 11]
dmms_five = ["MMS", "EOE", 16]
dmms_six = ["MMS", "FHS", 11]
dmms_seven = ["MMS", "FHE", 15]
dmms_eight = ["MMS", "FMS", 12]
dmms_nine = ["MMS", "SJG", 12]
dmms_ten = ["MMS", "GRE", 13]
dmms_eleven = ["MMS", "MtMS", 2]
dmms_twelve = ["MMS", "NSE", 10]
dmms_thirteen = ["MMS", "NVE", 3.5]
dmms_fourteen = ["MMS", "OCE", 16]
dmms_fifteen = ["MMS", "PJS", 1]
dmms_sixteen = ["MMS", "RCE", 1]
dmms_seventeen = ["MMS", "RVE", 2]
dmms_eighteen = ["MMS", "RRE", 13.5]
dmms_nineteen = ["MMS", "SMS", 11]
dmms_twenty = ["MMS", "TJE", 12]
dmms_twentyone = ["MMS", "VDLHS", 13.5]
dmms_twentytwo = ["MMS", "WRE", 2]
dmms_twentythree = ["MMS", "WME", 1]
dmts_one = ["MtMS", "BSE", 10]
dmts_two = ["MtMS", "CSE", 11]
dmts_three = ["MtMS", "ESC", 5.5]
dmts_four = ["MtMS", "FLHS", 9]
dmts_five = ["MtMS", "EOE", 14]
dmts_six = ["MtMS", "FHS", 9]
dmts_seven = ["MtMS", "FHE", 12]
dmts_eight = ["MtMS", "FMS", 10]
dmts_nine = ["MtMS", "SJG", 9]
dmts_ten = ["MtMS", "GRE", 11]
dmts_eleven = ["MtMS", "NSE", 7]
dmts_twelve = ["MtMS", "NVE", 3]
dmts_thirteen = ["MtMS", "OCE", 14]
dmts_fourteen = ["MtMS", "PJS", 2]
dmts_fifteen = ["MtMS", "RCE", 1]
dmts_sixteen = ["MtMS", "RVE", 2]
dmts_seventeen = ["MtMS", "RRE", 11.5]
dmts_eighteen = ["MtMS", "SMS", 9]
dmts_nineteen = ["MtMS", "TJE", 10]
dmts_twenty = ["MtMS", "VDLHS", 11.5]
dmts_twentyone = ["MtMS", "WRE", 4]
dmts_twentytwo = ["MtMS", "WME", 1]
dnve_one = ["NVE", "BSE", 12]
dnve_two = ["NVE", "CSE", 12.5]
dnce_three = ["NVE", "ESC", 8]
dnce_four = ["NVE", "FLHS", 11]
dnce_five = ["NVE", "EOE", 15]
dnce_six = ["NVE", "FHS", 10.5]
dnce_seven = ["NVE", "FHE", 13.5]
dnce_eight = ["NVE", "FMS", 11.5]
dnce_nine = ["NVE", "SJG", 11]
dnce_ten = ["NVE", "GRE", 12.5]
dnce_eleven = ["NVE", "NSE", 9]
dnce_twelve = ["NVE", "OCE", 15]
dnce_thirteen = ["NVE", "PJS", 4]
dnce_fourteen = ["NVE", "RCE", 2]
dnce_fifteen = ["NVE", "RVE", 4]
dnce_sixteen = ["NVE", "RRE", 14]
dnce_seventeen =["NVE", "SMS", 11]
dnce_eighteen = ["NVE", "TJE", 11]
dnce_nineteen = ["NVE", "VDLHS", 14]
dnce_twenty = ["NVE", "WRE", 2.5]
dnce_twentyone = ["NVE", "WME", 3]
dpjs_one = ["PJS", "BSE", 12]
dpjs_two = ["NVE", "CSE", 13]
dpjs_three = ["NVE", "ESC", 8]
dpjs_four = ["NVE", "FLHS", 11]
dpjs_five =["NVE", "EOE", 16]
dpjs_six = ["NVE", "FHS", 11]
dpjs_seven = ["NVE", "FHE", 14]
dpjs_eight = ["NVE", "FMS", 12]
dpjs_nine = ["NVE", "SJG", 11]
dpjs_ten = ["NVE", "GRE", 13]
dpjs_eleven = ["NVE", "NSE", 9]
dpjs_twelve = ["NVE", "OCE", 16]
dpjs_thirteen = ["NVE", "RCE", 1]
dpjs_fourteen = ["NVE", "RVE", 1]
dpjs_fifteen = ["NVE", "RRE", 14]
dpjs_sixteen = ["NVE", "SMS", 11]
dpjs_seventeen = ["NVE", "TJE", 11]
dpjs_eighteen = ["NVE", "VDLHS", 14]
dpjs_nineteen =["NVE", "WRE", 2]
dpjs_twenty = ["NVE", "WME", 2]
drce_one = ["RCE", "BSE", 11]
drce_two = ["RCE", "CSE", 12]
drce_three = ["RCE", "ESC", 7]
drce_four = ["RCE", "FLHS", 10]
drce_five = ["RCE", "EOE", 15]
drce_six = ["RCE", "FHS", 10]
drce_seven = ["RCE", "FHE", 13]
drce_eight = ["RCE", "FMS", 11]
drce_nine = ["RCE", "SJG", 11]
drce_ten = ["RCE", "GRE", 12]
drce_eleven = ["RCE", "NSE", 9]
drce_twelve = ["RCE", "OCE", 15]
drce_thirteen = ["RCE", "RVE", 2]
drce_fourteen = ["RCE", "RRE", 13]
drce_fifteen = ["RCE", "SMS", 10]
drce_sixteen = ["RCE", "TJE", 11]
drce_seventeen = ["RCE", "VDLHS", 13]
drce_eighteen = ["RCE", "WRE", 1]
drce_nineteen = ["RCE", "WME", 1]
drve_one = ["RVE", "BSE", 11]
drve_two = ["RVE", "CSE", 12]
drve_three = ["RVE", "ESC", 7]
drve_four = ["RVE", "FLHS", 10]
drve_five = ["RVE", "EOE", 16]
drve_six = ["RVE", "FHS", 10]
drve_seven = ["RVE", "FJE", 13]
drve_eight = ["RVE", "FMS", 11]
drve_nine = ["RVE", "SJG", 10]
drve_ten = ["RVE", "GRE", 12]
drve_eleven = ["RVE", "NSE", 8]
drve_twelve = ["RVE", "OCE", 13]
drve_thirteen = ["RVE", "RRE", 13]
drve_fourteen = ["RVE", "SMS", 10]
drve_fifteen = ["RVE", "TJE", 11]
drve_sixteen = ["RVE", "VDLHS", 13]
drve_seventeen = ["RVE", "WRE", 2]
drve_eighteen = ["RVE", "WME", 1]
dwre_one = ["WRE", "BSE", 12]
dwre_two = ["WRE", "CSE", 13]
dwre_three = ["WRE", "ESC", 9]
dwre_four = ["WRE", "FLHS", 11]
dwre_five = ["WRE", "EOE", 16]
dwre_six = ["WRE", "FHS", 11]
dwre_seven = ["WRE", "FHE", 14]
dwre_eight = ["WRE", "FMS", 11]
dwre_nine = ["WRE", "SJG", 11]
dwre_ten = ["WRE", "GRE", 13]
dwre_eleven = ["WRE", "NSE", 9]
dwre_twelve = ["WRE", "OCE", 16]
dwre_thirteen = ["WRE", "RRE", 15]
dwre_fourteen = ["WRE", "SMS", 11]
dwre_fifteen = ["WRE", "TJE", 12]
dwre_sixteen = ["WRE", "VDLHS", 15]
dwre_seventeen = ["WRE", "WME", 3]
dwme_one = ["WME", "BSE", 11]
dwme_two = ["WME", "CSE", 12]
dwme_three = ["WME", "ESC", 6.5]
dwme_fout = ["WME", "FLHS", 9.5]
dwme_five = ["WME", "EOE", 15]
dwme_six = ["WME", "FHS", 10]
dwme_seven = ["WME", "FHE", 13]
dwme_eight = ["WME", "FMS", 10]
dwme_nine = ["WME", "SJG", 10]
dwme_ten = ["WME", "GRE", 12]
dwme_eleven = ["WME", "NSE", 8]
dwme_twelve = ["WME", "OCE", 14]
dwme_thirteen = ["WME", "RRE", 12]
dwme_fourteen = ["WME", "SMS", 9.5]
dwme_fifteen = ["WME", "TJE", 11]
dwme_sixteen = ["WME", "VDLHS", 12]
dwme_seventeen = ["WME", "WRE", 3]



list_of_distances = [
    distance_one,
    distance_two,
    distance_three,
    distance_four,
    distance_five,
    distance_six,
    distance_seven,
    distance_eight,
    distance_nine,
    distance_ten,
    distance_eleven,
    distance_twelve,
    distance_thirteen,
    distance_fourteen,
    distance_fifteen,
    distance_sixteen,
    distance_seventeen,
    distance_eighteen,
    distance_nineteen,
    distance_twenty,
    distance_twentyone,
    distance_twentytwo,
    distance_twentythree,
    distnace_twentyfour,
    distance_twentyfive,
    distance_twentysix,
    distance_twentyseven,
    distance_twentyeight,
    distance_twentynine,
    distance_thirty,
    distance_thirtyone,
    distance_thirtytwo,
    distance_thirtythree,
    distance_thirtyfour,
    distance_thirtyfive,
    distance_thirtysix,
    distance_thirtyseven,
    distance_thirtyeight,
    distance_thirtynine,
    distance_fourty,
    distance_fortyone,
    distance_fortytwo,
    distance_fortythree,
    distance_fortyfour,
    distance_fortyfive,
    distance_fortysix,
    distance_fortyseven,
    distance_fortyeight,
    distance_fortynine,
    distance_fifty,
    distance_fiftyone,
    distance_fiftytwo,
    distance_fiftythree,
    distance_fiftyfour,
    distance_fiftyfive,
    distance_fiftysix,
    distance_fiftyseven,
    distance_fiftyeight,
    distance_fiftynine,
    distance_sixty,
    distance_sixtyone,
    distance_sixtytwo,
    distance_sixtythree,
    distance_sixtyfour,
    distance_sixtyfive,
    distance_sixtysix,
    distance_sixtyeight,
    distance_sixtynine,
    distance_seventy,
    distance_seventyone,
    distance_seventytwo,
    distance_seventythree,
    distance_seventyfour,
    distance_seventyfive,
    distance_seventysix,
    distance_seventyseven,
    distance_seventyeight,
    distance_seventynine,
    distance_eighty,
    distance_eightyone,
    distance_eightytwo,
    distance_seventythree,
    distance_seventyfour,
    distance_seventyfive,
    distance_seventysix,
    distance_seventyseven,
    distance_seventyeight,
    distance_seventynine,
    distance_eighty,
    distance_eightyone,
    distance_eightytwo,
    distance_eightythree,
    distance_eightyfour,
    distance_eightyfive,
    distance_eightysix,
    distance_eightyseven,
    distance_eightyeight,
    distance_eightynine,
    distance_ninety,
    distance_ninetyone,
    distance_ninetytwo,
    distance_ninetythree,
    distance_ninetyfour,
    distance_ninetyfive,
    distance_ninetysix,
    distance_ninetyseven,
    distance_ninetyeight,
    distance_ninetynine,
    distance_hundred,
    distance_hundredone,
    distance_hundredtwo,
    distance_hundredthree,
    distance_hundredfour,
    distance_hundredfive,
    distance_hundredsix,
    distance_hundredseven,
    distance_hundredeight,
    distance_hundrednine,
    distance_hundredten,
    distance_hundredeleven,
    distance_hundredtwelve,
    distance_hundredthirteen,
    distance_hundredfourteen,
    distance_hundredfifteen,
    distance_hundredsixteen,
    distance_hundredseventeen,
    distance_hundredeighteen,
    distance_hundrednineteen,
    distance_hundredtwenty,
    distance_hundredtwentyone,
    distance_hundredtwentytwo,
    distance_hundredtwentythree,
    distance_hundredtwentyfour,
    distance_hundredtwentyfive,
    distance_hundredtwentysix,
    distance_hundredtwentyseven,
    d_one,
    d_two,
    d_three,
    d_four,
    d_five,
    d_six,
    d_seven,
    d_eight,
    d_nine,
    d_ten,
    d_eleven,
    d_twelve,
    d_thirteen,
    d_fourteen,
    d_fifteen,
    d_sixteen,
    d_seventeen,
    d_eighteen,
    d_ninenteen,
    d_twenty,
    d_twentyone,
    d_twentytwo,
    d_twentythree,
    d_twentyfour,
    d_twentyfive,
    d_twentysix,
    d_twentyseven,
    d_twentyeight,
    d_twentynine,
    d_thirty,
    d_thirtyone,
    dcge_one,
    dcge_two,
    dcge_three,
    dcge_four,
    dcge_five,
    dcge_six,
    dcge_seven,
    dcge_eight,
    dcge_nine,
    dcge_ten,
    dcge_eleven,
    dcge_twelve,
    dcge_thirteen,
    dcge_fourteen,
    dcge_fifteen,
    dcge_sixteen,
    dcge_seventeen,
    dcge_eighteen,
    dcge_nineteen,
    dcge_twenty,
    dcge_twentyone,
    dcge_twentytwo,
    dcge_twentythree,
    dcge_twentfour,
    dcge_twentyfive,
    dcge_twentysix,
    dcge_twentyseven,
    dcge_twentyeight,
    dcge_twentynine,
    dcge_thirty,
    dchs_one,
    dchs_two,
    dchs_three,
    dchs_four,
    dchs_five,
    dchs_six,
    dchs_seven,
    dchs_eight,
    dchs_nine,
    dchs_ten,
    dchs_eleven,
    dchs_twelve,
    dchs_thirteen,
    dchs_fourteen,
    dchs_fifteen,
    dchs_sixteen,
    dchs_seventeen,
    dchs_eighteen,
    dchs_nineteen,
    dchs_twenty,
    dchs_twentyone,
    dchs_twentytwo,
    dchs_twentythree,
    dchs_twentyfour,
    dchs_twentyfive,
    dchs_twentysix,
    dchs_twentyseven,
    dchs_twentyeight,
    dchs_twentynine,
    dclc_one,
    dclc_two,
    dclc_three,
    dclc_four,
    dclc_five,
    dclc_six,
    dclc_seven,
    dclc_eight,
    dclc_nine,
    dclc_ten,
    dclc_eleven,
    dclc_twelve,
    dclc_thirteen,
    dclc_fourteen,
    dclc_fifteen,
    dclc_sixteen,
    dclc_seventeen,
    dclc_eighteen,
    dclc_nineteen,
    dclc_twenty,
    dclc_twentyone,
    dclc_twentytwo,
    dclc_twentythree,
    dclc_twentyfour,
    dclc_twentyfive,
    dclc_twentysix,
    dclc_twentyseven,
    dclc_twentyeight,
    dcme_one,
    dcme_two,
    dcme_three,
    dcme_four,
    dcme_five,
    dcme_six,
    dcme_seven,
    dcme_eight,
    dcme_nine,
    dcme_ten,
    dcme_eleven,
    dcme_twelve,
    dcme_thirteen,
    dcme_fourteen,
    dcme_fifteen,
    dcme_sixteen,
    dcme_seventeen,
    dcme_eighteen,
    dcme_nineteen,
    dcme_twenty,
    dcme_twentyone,
    dcme_twentytwo,
    dcme_twentythree,
    dcme_twentyfour,
    dcme_twentyfive,
    dcme_twentysix,
    dcme_twentyseven,
    dcve_one,
    dcve_two,
    dcve_three,
    dcve_four,
    dcve_five,
    dcve_six,
    dcve_seven,
    dcve_eight,
    dcve_nine,
    dcve_ten,
    dcve_eleven,
    dcve_twelve,
    dcve_thirteen,
    dcve_fourteen,
    dcve_fifteen,
    dcve_sixteen,
    dcve_seventeen,
    dcve_eighteen,
    dcve_nineteen,
    dcve_twenty,
    dcve_twentyone,
    dcve_twentytwo,
    dcve_twentythree,
    dcve_twentyfour,
    dcve_twentyfive,
    dcve_twentysix,
    dkhs_one,
    dkhs_two,
    dkhs_three,
    dkhs_four,
    dkhs_five,
    dkhs_six,
    dkhs_seven,
    dkhs_eight,
    dkhs_nine,
    dkhs_ten,
    dkhs_eleven,
    dkhs_twelve,
    dkhs_thirteen,
    dkhs_fourteen,
    dkhs_fifteen,
    dkhs_sixteen,
    dkhs_seventeen,
    dkhs_eighteen,
    dkhs_nineteen,
    dkhs_twenty,
    dkhs_twentyone,
    dkhs_twentytwo,
    dkhs_twentythree,
    dkhs_twentyfour,
    dkhs_twentyfive,
    dmhe_one,
    dmhe_two,
    dmhe_three,
    dmhe_four,
    dmhe_five,
    dmhe_six,
    dmhe_seven,
    dmhe_eight,
    dmhe_nine,
    dmhe_ten,
    dmhe_eleven,
    dmhe_twelve,
    dmhe_thirteen,
    dmhe_fourteen,
    dmhe_fifteen,
    dmhe_sixteen,
    dmhe_seventeen,
    dmhe_eighteen,
    dmhe_ninenteen,
    dmhe_twenty,
    dmhe_twentyone,
    dmhe_twentytwo,
    dmhe_twentythree,
    dmhe_twentyyfour,
    dmms_one,
    dmms_two,
    dmms_three,
    dmms_four,
    dmms_five,
    dmms_six,
    dmms_seven,
    dmms_eight,
    dmms_nine,
    dmms_ten,
    dmms_eleven,
    dmms_twelve,
    dmms_thirteen,
    dmms_fourteen,
    dmms_fifteen,
    dmms_sixteen,
    dmms_seventeen,
    dmms_eighteen,
    dmms_nineteen,
    dmms_twenty,
    dmms_twentyone,
    dmms_twentytwo,
    dmms_twentythree,
    dmts_one,
    dmts_two,
    dmts_three,
    dmts_four,
    dmts_five,
    dmts_six,
    dmts_seven,
    dmts_eight,
    dmts_nine,
    dmts_ten,
    dmts_eleven,
    dmts_twelve,
    dmts_thirteen,
    dmts_fourteen,
    dmts_fifteen,
    dmts_sixteen,
    dmts_seventeen,
    dmts_eighteen,
    dmts_nineteen,
    dmts_twenty,
    dmts_twentyone,
    dmts_twentytwo,
    dnve_one,
    dnve_two,
    dnce_three,
    dnce_four,
    dnce_five,
    dnce_six,
    dnce_seven,
    dnce_eight,
    dnce_nine,
    dnce_ten,
    dnce_eleven,
    dnce_twelve,
    dnce_thirteen,
    dnce_fourteen,
    dnce_fifteen,
    dnce_sixteen,
    dnce_seventeen,
    dnce_eighteen,
    dnce_nineteen,
    dnce_twenty,
    dnce_twentyone,
    dpjs_one,
    dpjs_two,
    dpjs_three,
    dpjs_four,
    dpjs_five,
    dpjs_six,
    dpjs_seven,
    dpjs_eight,
    dpjs_nine,
    dpjs_ten,
    dpjs_eleven,
    dpjs_twelve,
    dpjs_thirteen,
    dpjs_fourteen,
    dpjs_fifteen,
    dpjs_sixteen,
    dpjs_seventeen,
    dpjs_eighteen,
    dpjs_nineteen,
    dpjs_twenty,
    drce_one,
    drce_two,
    drce_three,
    drce_four,
    drce_five,
    drce_six,
    drce_seven,
    drce_eight,
    drce_nine,
    drce_ten,
    drce_eleven,
    drce_twelve,
    drce_thirteen,
    drce_fourteen,
    drce_fifteen,
    drce_sixteen,
    drce_seventeen,
    drce_eighteen,
    drce_nineteen,
    drve_one,
    drve_two,
    drve_three,
    drve_four,
    drve_five,
    drve_six,
    drve_seven,
    drve_eight,
    drve_nine,
    drve_ten,
    drve_eleven,
    drve_twelve,
    drve_thirteen,
    drve_fourteen,
    drve_fifteen,
    drve_sixteen,
    drve_seventeen,
    drve_eighteen,
    dwre_one,
    dwre_two,
    dwre_three,
    dwre_four,
    dwre_five,
    dwre_six,
    dwre_seven,
    dwre_eight,
    dwre_nine,
    dwre_ten,
    dwre_eleven,
    dwre_twelve,
    dwre_thirteen,
    dwre_fourteen,
    dwre_fifteen,
    dwre_sixteen,
    dwre_seventeen,
    dwme_one,
    dwme_two,
    dwme_three,
    dwme_fout,
    dwme_five,
    dwme_six,
    dwme_seven,
    dwme_eight,
    dwme_nine,
    dwme_ten,
    dwme_eleven,
    dwme_twelve,
    dwme_thirteen,
    dwme_fourteen,
    dwme_fifteen,
    dwme_sixteen,
    dwme_seventeen
]



## Extract data from PDF
def pdf_extract():
    mileage_pdf = sys.argv[1]
    pdf_reader = PdfReader(open(mileage_pdf, "rb"))

    dict_of_all_fields = pdf_reader.get_form_text_fields()

    ## Create a while loop that will create a  string name for all 26 rows of "STOPS MADE"
    ## after name is created, it will increment the counter c by 1, and return the value
    ## for that field fuck yeah B)

    total_distance = []
    first_travel = []
    c = 1
    while c < 27:
        ## Get the keys for the value of the "first site" and for the first "travel"
        temp_name = str("STOPS MADERow"+str(c))
        temp_namee = str("FROM FIRST PLACE OF WORKRow"+str(c))
        my_field_value = (dict_of_all_fields[temp_name])
        field_value = (dict_of_all_fields[temp_namee])
        ## Now I want to take that str value and turn it into a list that
        ## can be used with a different loop I have
        if field_value is None and my_field_value is None:
            if c <= 9:
                print("Row "+str(c)+" total miles:     0")
            else:
                print("Row "+str(c)+" total miles:    0")
        if field_value == my_field_value:
            if c <= 9:
                print("Row "+str(c)+" total miles:     0")
            else:
                print("Row "+str(c)+" total miles:    0")
            
        
        else:
            real_list = my_field_value.split(", ")
            first_travel.append(field_value)
            first_travel.append(real_list[0])
            ## Loop to check the distance from start site to first travel site
            for z in list_of_distances:

                if first_travel[0] in z:

                    if first_travel[1] in z:

                        total_distance.append(z[2])


            ## List comprehension to get the pair of sites
            list_of_pairs = [[real_list[i], real_list[i + 1]] for i in range(len(real_list) - 1)]

            ## Loop to check the distance to all the travel sites
            for x in list_of_pairs:

                for y in list_of_distances:

                    if x[0] in y:

                        if x[1] in y:

                            total_distance.append(y[2])
            ## if statement purely for cosmetic purposes, if the counter c <10, it
            ## will print with 5 'spaces' after "total miles:" and if it is >9, it
            ## will print with 4 'spaces' after "total miles:"
            if c <= 9:

                print("Row "+str(c)+" total miles:     "+str(round(sum(total_distance), 2)))

            else:

                print("Row "+str(c)+" total miles:    "+str(round(sum(total_distance), 2)))


        ## Have to clear the contents of the lists before
        ## the next iteration
        first_travel.clear()
        total_distance.clear()
        c += 1
    if c >= 27:
        print("Congratulations!! You just saved 15 minutes!! Go take a break now ;)")
    return ""


print(pdf_extract())
