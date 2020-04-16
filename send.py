import requests
 
url = "https://www.fast2sms.com/dev/bulk"

policyno = input('Enter the policy Number ---> ')
amount = input('Enter the Amount ---> ')
due = input('Enter the Due Date ---> ')
mobile = input('Enter the Mobile Number ---> ')

msg = '\nShailendra Srivastava'+"\nPolicy Number - " +policyno+'\n'+"Amount - "+ amount+'\n'+"Due Date - " + due + '\n7897149018'
print(msg)

payload = "sender_id=FSTSMS&message="+"\n"+msg+"&language=english&route=p&numbers="+mobile
headers = {
 'authorization': "fxHXApVd4DwTnmIctQ5qFOB32ja69Gg0bMhYvKCJsPkENoSLZilHv8GO13baXnsh2gf06RLAz9Pi4DEc",
 'Content-Type': "application/x-www-form-urlencoded",
 'Cache-Control': "no-cache",
 }

response = requests.request("POST", url, data=payload, headers=headers)
 
print(response.text)
