import urllib2

url = "http://finance.yahoo.com/d/quotes.csv?s=XOM+EK+JNJ+MSFT&f=snd1l1ohgvwdyr"


def down_data(address):
    response = urllib2.urlopen(address)
    fin = response.read()
    fin_str = str(fin)
    lines = fin_str.split("\\n")
    destination = r'myData.csv'
    fout = open(destination, "w")
    for line in lines:
        fout.write(line + '\n')
    fout.close()

    down_data(url)
