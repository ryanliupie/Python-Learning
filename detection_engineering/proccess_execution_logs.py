'''
We are given process execution logs, we must write a function 
that detections suspicious process chains, where we will flag 
a user when powershell.exe is spawned by a browser and it later spawns cmd.exe
'''

logs = [
    {"user": "ryan", "process": "chrome.exe", "parent": "explorer.exe"},
    {"user": "ryan", "process": "powershell.exe", "parent": "chrome.exe"},
    {"user": "ryan", "process": "cmd.exe", "parent": "powershell.exe"},
    {"user": "ryan", "process": "notepad.exe", "parent": "explorer.exe"},
]

def process_execution_detection(logs): 
    browser_processes = {"chrome.exe", "firefox.exe", "edge.exe"}
    suspicious_users = set()

    for i in range(len(logs) - 1): 
        current = logs[i]
        next_event = logs[i + 1]

        if (
            current["process"] in browser_processes and 
            next_event["process"] == "powershell.exe" and 
            next_event["parent"] == current["process"] and 
            current["user"] == next_event["user"]
        ):
            if i + 2 < len(logs): 
                third_event = logs[i + 2]
            
            if (
                third_event["process"] == "cmd.exe" and 
                third_event["parent"] == "powershell.exe" and 
                third_event["user"] == current["user"]
            ): 
                suspicious_users.add(current["user"])
    
    return suspicious_users
        
print(process_execution_detection(logs))



