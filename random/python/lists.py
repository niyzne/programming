# Original list
ip_addresses = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
print(ip_addresses)

# Modifying second list item (0-based indexing)
ip_addresses[1] = "10.0.0.254"
print(ip_addresses)

# add another thing to existing list
ip_addresses.append("192.168.1.50")
print(ip_addresses)

# Removing elements
ip_addresses.remove("192.168.1.1")
print(ip_addresses)
