import requests, json
 
cookie = 'cooki'
 
getMessagesUrl = 'https://privatemessages.roblox.com/v1/messages?messageTab=Inbox'
archiveMessageUrl = 'https://privatemessages.roblox.com/v1/messages/archive'
 
XCSRF_Token = None
def loadXCSRF_Token():
    auth_response = requests.post('https://auth.roblox.com/v1/logout', headers={'cookie': f'.ROBLOSECURITY={cookie}' + ';'})
    if 'x-csrf-token' in auth_response.headers:
        global XCSRF_Token
        XCSRF_Token = auth_response.headers['x-csrf-token']
    else:
        print('exit')
        exit()
loadXCSRF_Token()
 
page = 0
messages = requests.get(getMessagesUrl, headers={'cookie': f'.ROBLOSECURITY={cookie}', 'Content-Type': 'application/json', 'X-CSRF-TOKEN': XCSRF_Token})
while True:
	currentMessageIds = {'messageIds': []}
	for x in messages.json()['collection']:
		currentMessageIds['messageIds'].append(x['id'])

	r = requests.post(archiveMessageUrl, data=json.dumps(currentMessageIds), headers={'cookie': f'.ROBLOSECURITY={cookie}', 'Content-Type': 'application/json', 'X-CSRF-TOKEN': XCSRF_Token})
	print('Page:'+str(page), r.json())
 
	page = page + 1
	messages = requests.get(getMessagesUrl + '&pageNumber=' + str(page), headers={'cookie': f'.ROBLOSECURITY={cookie}', 'Content-Type': 'application/json', 'X-CSRF-TOKEN': XCSRF_Token})
 
	loadXCSRF_Token()
