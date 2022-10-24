#!/home/joey/Ansible/py3.8.10 python
from datetime import date
import re
import sys
#import dnspython as dns
import dns.resolver

today = date.today().strftime("%Y%m%d")

resolver = dns.resolver.Resolver()
resolver.lifetime= 1
resolver.timeout= 0.5

DNS_SERVER = sys.argv[1]
DOMAIN_URL = sys.argv[2]

def getARecord(dnsServer, domainName):
    resolver.nameservers = [dnsServer]
    answers = resolver.resolve(domainName, 'A')
    result_list = []
    with open('/home/joey/Ansible/roles/firewall_cisco/others/dns-resolved-{}-{}.txt'.format(domainName, today), 'w')  as f:
        for answer in answers:
#            result_list.append(str(answer))
            print('[*] {} has IP'.format(domainName), answer, 'resolved.')
            f.write("{}\n".format(str(answer)))
        f.close()
#    return result_list

if __name__ == '__main__':
    getARecord(DNS_SERVER, DOMAIN_URL)