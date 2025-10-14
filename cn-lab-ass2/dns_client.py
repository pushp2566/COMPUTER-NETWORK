import socket
import dns.resolver

domain = "example.com"

# Resolve IP
ip = socket.gethostbyname(domain)
if ip:
    print(f"IP of {domain} is {ip}")
else:
    print("Failed to resolve domain")

# DNS Records
resolver = dns.resolver.Resolver()

for record_type in ["A", "MX", "CNAME"]:
    answers = resolver.resolve(domain, record_type, raise_on_no_answer=False)
    if len(answers) > 0:
        print(f"{record_type} Records:")
        for rdata in answers:
            print(rdata.to_text())
    else:
        print(f"No {record_type} record found for {domain}")
