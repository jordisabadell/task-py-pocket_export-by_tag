import argparse
import requests
import json
from functions import saveItemToFileByTag

# ARGUMENTS
parser = argparse.ArgumentParser(description='This task export Pocket list to files grouped by tag.')
parser.add_argument('--consumerkey', dest='consumer_key', 
    help='Pocket consumer key.', type=str, required=True)
parser.add_argument('--accesstoken', dest='access_token', 
    help='Pocket access token.', type=str, required=True)
parser.add_argument('--outputfolder', dest='output_folder', 
    help='Output folder.', type=str, required=True)

args = parser.parse_args()
consumerKey = args.consumer_key
accessToken = args.access_token
outputFolder = args.output_folder

if not outputFolder.endswith("/"):
    outputFolder = outputFolder + "/"

# POST REQUEST
url = "https://getpocket.com/v3/get"
headers = {
    "somekey": "application/json"
}
params = {
    "consumer_key": consumerKey,
    "access_token": accessToken,
    "detailType": "complete"
}
data = requests.post(url, headers = headers, data = params)

# ITERATE RESULTS
if 'list' in data.json():    
    items = data.json()['list']
    for item in items:
        
        # get item
        values = items[item]
        url = values['given_url']
        title = values['given_title']
        tags = {}
        if 'tags' in values:
            tags = values['tags']    
        else:
            tags = {'__uncategorized__': ''}

        # save item
        for tag in tags:
            fileName = outputFolder + tag + ".txt"
            saveItemToFileByTag(fileName, title, url)