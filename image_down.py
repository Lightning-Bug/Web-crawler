import random
from urllib2 import urlopen
#import urllib2
import urllib

def down_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    #urllib2.Request(url, full_name)
    urllib.urlretrieve(url, full_name)

down_image("https://images5.alphacoders.com/568/568653.jpg")
down_image("https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjdwLL75ITWAhUlTo8KHaabB20QjRwIBw&url=http%3A%2F%2Fwww.qygjxz.com%2Fpic-hd.html&psig=AFQjCNFMWBFPSAvdTmbFzy2QaCgPThtOzA&ust=1504382846500952")