# Given a list of login attempts, count how many login attempts each ip address has.
# Print all IP addresses that have 3 or more failed attempts 
# Return them as a list 

login_attempts = [
    {"username": "ryan",    "ip_address": "192.168.1.10",  "success": False},
    {"username": "ryan",    "ip_address": "192.168.1.10",  "success": False},
    {"username": "ryan",    "ip_address": "192.168.1.10",  "success": True},

    {"username": "admin",   "ip_address": "192.168.1.11",  "success": False},
    {"username": "admin",   "ip_address": "192.168.1.11",  "success": False},
    {"username": "guest",   "ip_address": "192.168.1.11",  "success": False},
    {"username": "admin",   "ip_address": "192.168.1.11",  "success": False},
    {"username": "admin",   "ip_address": "192.168.1.11",  "success": True},

    {"username": "sara",    "ip_address": "10.0.0.5",      "success": False},
    {"username": "sara",    "ip_address": "10.0.0.5",      "success": False},
    {"username": "sara",    "ip_address": "10.0.0.5",      "success": False},
    {"username": "sara",    "ip_address": "10.0.0.5",      "success": False},
    {"username": "sara",    "ip_address": "10.0.0.5",      "success": True},

    {"username": "liam",    "ip_address": "10.0.0.8",      "success": True},
    {"username": "liam",    "ip_address": "10.0.0.8",      "success": False},
    {"username": "liam",    "ip_address": "10.0.0.8",      "success": True},

    {"username": "mia",     "ip_address": "172.16.0.2",    "success": False},
    {"username": "mia",     "ip_address": "172.16.0.2",    "success": True},
    {"username": "mia",     "ip_address": "172.16.0.2",    "success": False},
    {"username": "mia",     "ip_address": "172.16.0.2",    "success": False},

    {"username": "noah",    "ip_address": "203.0.113.7",   "success": False},
    {"username": "noah",    "ip_address": "203.0.113.7",   "success": False},
    {"username": "noah",    "ip_address": "203.0.113.7",   "success": False},
    {"username": "noah",    "ip_address": "203.0.113.7",   "success": True},

    {"username": "olivia",  "ip_address": "203.0.113.9",   "success": True},
    {"username": "olivia",  "ip_address": "203.0.113.9",   "success": True},
    {"username": "olivia",  "ip_address": "203.0.113.9",   "success": False},

    # "Password spray"-ish pattern: many usernames from one IP failing
    {"username": "admin",   "ip_address": "198.51.100.23", "success": False},
    {"username": "ryan",    "ip_address": "198.51.100.23", "success": False},
    {"username": "sara",    "ip_address": "198.51.100.23", "success": False},
    {"username": "liam",    "ip_address": "198.51.100.23", "success": False},
    {"username": "mia",     "ip_address": "198.51.100.23", "success": False},
    {"username": "noah",    "ip_address": "198.51.100.23", "success": False},
    {"username": "olivia",  "ip_address": "198.51.100.23", "success": False},
    {"username": "guest",   "ip_address": "198.51.100.23", "success": False},

    # Mixed normal traffic
    {"username": "ryan",    "ip_address": "192.168.1.12",  "success": True},
    {"username": "ryan",    "ip_address": "192.168.1.12",  "success": True},
    {"username": "ryan",    "ip_address": "192.168.1.12",  "success": False},

    {"username": "sara",    "ip_address": "10.0.0.12",     "success": True},
    {"username": "sara",    "ip_address": "10.0.0.12",     "success": True},
    {"username": "sara",    "ip_address": "10.0.0.12",     "success": True},

    {"username": "admin",   "ip_address": "172.16.0.9",    "success": False},
    {"username": "admin",   "ip_address": "172.16.0.9",    "success": False},
    {"username": "admin",   "ip_address": "172.16.0.9",    "success": False},

    {"username": "guest",   "ip_address": "172.16.0.10",   "success": True},
    {"username": "guest",   "ip_address": "172.16.0.10",   "success": False},

    {"username": "liam",    "ip_address": "203.0.113.55",  "success": False},
    {"username": "liam",    "ip_address": "203.0.113.55",  "success": False},
    {"username": "liam",    "ip_address": "203.0.113.55",  "success": False},
    {"username": "liam",    "ip_address": "203.0.113.55",  "success": False},

    {"username": "mia",     "ip_address": "198.51.100.88", "success": True},
    {"username": "mia",     "ip_address": "198.51.100.88", "success": True},
    {"username": "mia",     "ip_address": "198.51.100.88", "success": True},
]



new_dict = {}

for attempt in login_attempts: 
    if not attempt["success"]: 
        ip = attempt["ip_address"]

        new_dict[ip] = new_dict.get(ip, 0) + 1 


suspicious_ips = []
for key, value in new_dict.items():  # suspicious_ips = [ip for ip, count in new_dict.items() if count >= 3]
    if value >= 3: 
        suspicious_ips.append(key)

print("Suspicious IP Addresses:\n")
for ip in suspicious_ips: 
    print(ip)



        





        

