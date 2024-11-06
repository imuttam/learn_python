import re

# Pattern to match IP addresses at the beginning of each line
ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
unique_ips = set()  # Set to store unique IP addresses

with open('./access.log') as file:
    for line in file:
        # Search for the IP address at the start of the line
        match = re.match(ip_pattern, line)
        if match:
            ip_address = match.group()  # Get the matched IP address
            unique_ips.add(ip_address)  # Add to set of unique IPs

# Print all unique IP addresses
# for ip in unique_ips:
#     print(ip)

print(len(ip_pattern))
