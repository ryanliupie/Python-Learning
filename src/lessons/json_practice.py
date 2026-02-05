import json 

string1 = '''{
    "people": [
      {
        "name": "Bob Lion", 
        "phone": "354-234-4675", 
        "emails": ["boblion@gmail.com", "dudecoolguy@gmail.com"], 
        "has_license": false
      }, 
      {
        "name": "Jane Doe", 
        "phone": "465-567-5476", 
        "emails": null, 
        "has_license": true      
      }
    ]
}'''

data = json.loads(string1) #lets us load the json document so we can work with it (string)

