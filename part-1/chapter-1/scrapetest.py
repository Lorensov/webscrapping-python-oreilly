from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
	html = urlopen( "http://pythonscraping.com/exercises/exercise1.html" )
except HTTPError as e:
	print( "this is the error:" + e )
else:
	print( "End of Try/Catch!" )

if html is None:
	print( "URL not found :( " )
else:
	print( "here's your HTML :D" )
	
bsObj = BeautifulSoup( html.read() )
print( bsObj )