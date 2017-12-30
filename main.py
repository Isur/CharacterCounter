import datetime
import os
currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
reportFile = open('report/report.html', 'w')
html = """<html>
<head><title>Report</title>
<style>
body{background:#252525;color:#ACAC11; font-family: 'Trocchi', serif;font-weight: bold;}
.title{
    color: khaki;
    font-family: 'Trocchi', serif;
    font-size: 48px;
    font-weight: normal;
    line-height: 48px;
    margin: auto;
}
.div_table{height:75%;width:75%;margin:auto;overflow:auto;}
.titleText{
    
    color: #c0c0c0;
    font-family: 'Trocchi', serif;
    font-size: 32px;
    font-weight: normal;
    line-height: 48px;
    margin: auto;
    
    
}
.reportTable{
    margin: auto;
    background: #333333;
    border: solid khaki;
    text-align:center;
    overflow:auto;
}
.reportTable td{
    border: solid black thin;
    width: 75px;
}

table.reportTable > tbody > tr:first-child > td:first-child{
    background: grey;
    width:40px;
}

table.reportTable > tbody > tr > td:first-child, table.reportTable > tbody > tr:first-child{
    background: green;
    color:#d0d0d0;
}table.reportTable td:hover{
background: silver;
color: #333333;
}
</style>
</head>
<body><p align="center" class="title">Characters counter</p><p align="center" class="titleText">Report was generated:<br/> """
reportFile.write(html + str(currentTime) + """</p> """)

indir = 'output/'
firstFile = False
chars = []
count = []
allCount = []
reportFile.write("""<div class="div_table"><table class="reportTable">""")
reportFile.write("""<tr><td></td>""")
for files in os.walk(indir):
    for f in files[2]:
        link = "output\\"
        link += f
        reportFile.write("""<td>"""+f+"""</td>""")
        if firstFile == False:
            out = open(link,'r')
            for linesF in out:
                chars.append(linesF[:1])
                firstFile = True
            out.close()
        out = open(link,'r')
        for lines in out:
            count.append((str(lines[6:])).strip("\n"))
        allCount.append(count)
        count = []
        out.close()

reportFile.write("""</tr>""")
try:
    chars[0]="Space"
except IndexError:
    print("Maybe there is no files?")
for x in range(0,len(chars)):
    reportFile.write("""<tr><td>"""+chars[x]+"""</td>""")
    for y in range(0,len(allCount)):
        reportFile.write("""<td>"""+allCount[y][x]+"""</td>""")
    reportFile.write("""</tr>""")


reportFile.write("""</table></div></body></html>""")        
reportFile.close()


