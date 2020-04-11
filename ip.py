import pygeoip, requests

my_ip_addr = requests.get('http://api.ipify.org').text

gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr(my_ip_addr)

print(res)
