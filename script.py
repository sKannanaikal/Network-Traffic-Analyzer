import geoip2.database
import optparse

def readPCAP(file, database):
	packets = []
	return packets


def locateIP(ip, database):
	match = database.country(ip)
	location = match.country.name
	return location

def main():
	with geoip2.database.Reader('database/GeoLite2-Country.mmdb') as database:
		command = optparse.OptionParser('usage%prog -f <capture file>')
		command.add_option('-f', dest='capture', type='string', help='specify the file that will be parsed')
		file = command.capture
		readPCAP(file, database)
		
if __name__ == "__main__":
	main()