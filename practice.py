login_attempts = [
    {"username": "ryan", "ip_address": "192.168.1.10", "success": False},
    {"username": "admin", "ip_address": "192.168.1.11", "success": False},
    {"username": "ryan", "ip_address": "192.168.1.10", "success": False},
    {"username": "ryan", "ip_address": "192.168.1.10", "success": True},
    {"username": "guest", "ip_address": "192.168.1.11", "success": False},
    {"username": "admin", "ip_address": "192.168.1.11", "success": False},
]



for line in login_attempts: 
    for key, value in line.items(): 
        if key == "success": 
            print(value)
                
    

