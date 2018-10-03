import requests
import json
data= json.dumps({'name': 'newrepo','description':'demo repo'})
r=requests.post('https://api.github.com/user/repos',data=data,auth=('kevalrathod','Aculasrepero@123'))
print(r.status_code)
print(r.json())
