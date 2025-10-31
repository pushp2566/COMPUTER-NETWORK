def ip_to_binary(ip_address: str) -> str:
    octets = ip_address.split('.')
    binary_octets = [format(int(o), '08b') for o in octets]
    return ''.join(binary_octets)

print(ip_to_binary("192.168.1.1"))

def get_network_prefix(ip_cidr: str) -> str:
    ip, prefix_length = ip_cidr.split('/')
    prefix_length = int(prefix_length)
    binary_ip = ip_to_binary(ip)
    return binary_ip[:prefix_length]

print(get_network_prefix("200.23.16.0/23"))

