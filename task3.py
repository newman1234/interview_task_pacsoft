from urllib.request import urlopen, Request
import json
from bs4 import BeautifulSoup

ret_list = []

url = 'https://scholar.google.com/scholar?oi=bibs&hl=en&cites=7127218252840885994'

# Manmade headers to avoid blocking from server
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
'Cookie':'SIDCC=AE4kn7-sb3158tSfdsb42eOPBmCpwro5A4TitfWL7VL4Mh3DV-aLBWr8Bnq3hYLy67hSKP_Yhss; 1P_JAR=2017-12-19-12; NID=119=qayf2Elv2f5rowsclx1WTItm28lWcRL1G-Y_rFvHuJySkxn45aKGQD5WB2D7P0-qYdb5iPGQULUxj8L_EX9b357iIWKYAWvxbVjLB1dqRA6UrAPOa-4RH8jLXpmARi_-rFepT_y6OWsuz4kfGXZ_BvDO3FN0mkl3lu_Y2JnHyd_AtDTV2AKBUkYwxh5iMcRoHsZqPHoADzjMLymyxBdVuzozdj46wKXjvI_I-8A4DCfm4-Xl0zGeN6Z5PSqDsGSvqPHPiMmj4WUUbIlF2G5yTeSaHbb3Z9Oq2c5gNivsLK9s56Z-9_k0-xXcAnSE8U7RlfsjQzj2ulWt5LcWfx2eYj2hrQMZTg; ANID=AHWqTUnVd7vmi5mf7itikA-MeKsX12bJXvDdE5cXpKXfTcJh63hzaLpSPEtxc8_t; SID=QgW7Q3gOjs2Mz4MWUSOJARRKH6rAUZC3GvuD3jKR1v9zvTSS1n4rpMhVGwyvgqHRhk3UxQ.; APISID=g8yvWAuP5s5gHAIE/Aze2PdHhOxGbtMcu-; HSID=ARAq2Ccpb3X4YA3iQ; SAPISID=QRLS_aJ570mPNtS3/AEd-rVb1zJ2W-j38B; SSID=AgDXdH4YTNM1aGmyr; GSP=LM=1501688168:S=sC9E1CA6LKGaXct5'}

req = Request(url, headers=headers)
res = urlopen(req)
html_doc = res.read().decode('utf-8')
soup = BeautifulSoup(html_doc, 'html.parser')
for a_tag in soup.select('h3.gs_rt > a'):
    ret_list.append(a_tag.string)

print({'paper_title':ret_list})