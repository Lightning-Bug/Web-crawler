
import urllib

url = "http://https://extranet.who.int/tme/generateCSV.asp?ds=dictionary"
#31st october

def download(url1):
    response = urllib.urlopen(url1)
    csv= response.read()
    csv_str = str(csv)
    lines= csv_str.split("\\n")
    dest_url = 'data.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line + "\\n")
    fx.close


download(url)
