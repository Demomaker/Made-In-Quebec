import sys
def getAllRepositories(filename):
    file = open(filename)
    fileString = file.read()
    file.close()
    repositories = fileString.splitlines()
    return repositories

def removeRepeatedRepositories(repositories):
    passRepositories = [""]
    for repository in repositories:
        if not repository in passRepositories :
            passRepositories.append(repository)
    return passRepositories

def getUsernamesFromRepositories(repositories):
    usernames = []
    for repository in repositories:
        usernames.append(repository.split("/")[0])
    usernames.sort()
    return usernames

def getMapOfUsernames(usernames):
    userdict = {}
    for username in usernames:
        if not username == "" :
            if username in userdict.keys() :
                userdict[username] = userdict[username]+1
            else :
                userdict[username] = 1
    return userdict

def getGitHubLinkForUsername(username):
    return "[" + username + "](" + "https://github.com/" + username + ")"

def writeUserMapToFile(outFile, userdict):
    userMapText = getUserMapInText(userdict)
    file = open(outFile, "w+")
    file.write("# Made-In-Quebec : \n")
    file.write("## FR \nMontre ce qui est fait au Québec.\nOutput de https://github.com/IonicaBizau/made-in \n")
    file.write("| Nom d'utilisateur | Nombre de répertoires |\n|:---:|:---:|\n")
    file.write(userMapText + "\n")
    file.write("## EN \nShowing off what is being made in Quebec.\nOutput from https://github.com/IonicaBizau/made-in \n")
    file.write("| Username | Number of repositories |\n|:---:|:---:|\n")
    file.write(userMapText)

    file.close()

def getUserMapInText(userMap) :
    total = 0
    outString = ""
    for user in userMap :
        total += userMap[user]
        outString += "| " + getGitHubLinkForUsername(user) + " | " + str(userMap[user]) + " |\n"
    outString += "| Total | " + str(total) + " |"
    return outString


def main(filename, outFile):
    repositories = getAllRepositories(filename)
    repositories = removeRepeatedRepositories(repositories)
    usernames = getUsernamesFromRepositories(repositories)
    usermap = getMapOfUsernames(usernames)
    writeUserMapToFile(outFile, usermap)



if __name__ == "__main__":
    fileName = sys.argv[1]
    outFile = sys.argv[2]
    main(fileName, outFile)