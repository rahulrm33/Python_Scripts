import argparse
from threading import *
from socket import *

def check_socket_connection(host, port):
  try:
      server_sock = socket(AF_INET, SOCK_STREAM)
      server_sock.settimeout(5)
      result = server_sock.connect((host, port))
      print('[+] {}/tcp open'.format(port))
  except Exception as exception:
      print('[-] {}/tcp closed, Reason:{}'.format(port, (str(exception))))
  finally:
      server_sock.close()
      
def portScanner(host, ports):
  try:
      ip = gethostbyname(host)
      print('[+] Scan Results for: ' + ip)
  except:
      print("[-] Cannot resolve {}: Unknown host".format(host))
      return
  for port in ports:
      t = Thread(target=check_socket_connection, args=(ip, int(port)))
      t.start()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('H', type=str, help='remote host name')
  parser.add_argument('P', type=str, nargs='*', help='port numbers')
  args = parser.parse_args()
  portScanner(args.H, args.P)

