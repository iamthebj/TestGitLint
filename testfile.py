import urllib
import requests
import subprocess

#owner = 'iamthebj'
#repo = 'testgit'

# url = "https://api.github.com/repos/%s/%s/pulls/%s/files"%(owner, repo, pull_number)
print(url)
r = requests.get(url)
a = r.json()
raw = (a[0]['raw_url'])
filename = (a[0]['filename']).split("/")
file = filename[-1]

re = urllib.request.urlopen('%s'%raw)
#returned_value = os.system("start \"\" %s" %raw)
data = re.read()
dst = open("%s"%file, "wb")
dst.write(data)
dst = open("%s"%file, "r")

