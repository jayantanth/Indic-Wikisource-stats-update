import urllib2
import BeautifulSoup

url = "https://tools.wmflabs.org/phetools/statistics.php"
req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
con = urllib2.urlopen(req)
soup = BeautifulSoup.BeautifulSoup(con)
tables = soup.findChildren('table')
allrows = soup.findAll('tr')
x = len(allrows)
fle = open("two.txt",'a')
fle.write ("""Last update in Sept 2016, will be updated bi-monthly.

{|class="wikitable sortable"
<th colspan="7" style="text-align:center">Page namespace (Pages of Books)</th>
<th colspan="5" style="text-align:center">Main namespace (Article)</th>
!style="background: #efefef;"|'''language'''
!style="background: #ffffff;"|'''all pages'''
!style="background: #ffa0a0;"|'''not proof.'''
!style="background: #b0b0ff;"|'''problem.'''
!style="background: #ddd;"|'''w/o text'''
!style="background: #ffe867;"|'''proofread'''
!style="background: #90ff90;"|'''validated'''
!style="background: #efefef;"|'''all pages'''
!style="background: #90ff90;"|'''with scans'''
!style="background: #ffa0a0;"|'''w/o scans'''
!style="background: #ddd;"|'''disamb'''
!style="background: #efefef;"|'''percent'''
|-
""")
fle.close()
for i in range(0,x):
    if '<td>te</td>' in str(allrows[i]) or '<td>ta</td>' in str(allrows[i]) or '<td>ml</td>' in str(allrows[i]) or '<td>bn</td>' in str(allrows[i]) or '<td>kn</td>' in str(allrows[i]) or '<td>or</td>' in str(allrows[i]) or '<td>sa</td>' in str(allrows[i]) or '<td>as</td>' in str(allrows[i]) or '<td>mr</td>' in str(allrows[i]) or '<td>gu</td>' in str(allrows[i]):
        fle = open("two.txt",'a')
        fle.write (str(allrows[i]).replace('</td><td>',' || ').replace('<tr><td>','| ').replace('</td></tr>','')+'\n')
        fle.write (str('|-')+'\n')
        fle.close()
