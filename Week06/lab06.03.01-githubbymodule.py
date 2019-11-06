from github import Github
import requests

g = Github("a348eca2e402afc861d44d03f84e547ab5668170")

#for repo in g.get_user().get_repos():
 #print(repo.name)

repo = g.get_repo("TommyVaughan/dataRepresentation")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

newContents = contentOfFile + " more stuff \n" 
#print (newContents) 

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents ,fileInfo.sha) 
print (gitHubResponse) 