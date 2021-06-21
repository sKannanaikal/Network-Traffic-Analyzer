import geoip2.database
import optparse
import pyshark

def analyze(wireshark_capture, database):
	for packet in wireshark_capture.sniff_continuously(packet_count=10):
		try:
			destination_address = packet.ip.dst
			destination_location = locateIP(destination_address, database)
			source_address = packet.ip.src
			source_location = locateIP(source_address, database)
			print('[+] Packet from {src_addr} located in {src_loc} -> Packet sent to {dest_addr} located in {dest_loc}'.format(src_addr=source_address, src_loc=source_location, dest_addr=destination_address, dest_loc=destination_location))
		except:
			print("[-] Failed to process this packet's address")

def locateIP(ip, database):
	try:
		match = database.country(ip)
		location = match.country.name
		return location
	except:
		print('[-] Failed to identify a location for the given ip')
		return None

def main():
	with geoip2.database.Reader('database/GeoLite2-Country.mmdb') as database:
		print('[+] Opening up Database the software will be utilizing the GeoLite2-Country Database')
		#command = optparse.OptionParser('usage%prog -f <capture>')
		#command.add_option('-f', dest='capture', type='string', help='specify the file that will be parsed')
		file = open('captures/capture1.pcapng')
		netInt = 'en0'
		wireshark_capture = pyshark.LiveCapture(interface=netInt)
		print('[+] Wireshark capture found will proceed to processing the file')
		analyze(wireshark_capture, database)

if __name__ == "__main__":
	main()