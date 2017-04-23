"""
What if user leaves the group???
- Change check function for user (inside fileUpload)
"""
import pyrebase

from firebase import firebase

firebase = firebase.FirebaseApplication('https://learntogether-a250b.firebaseio.com')

# FILE UPLOAD FUNCTION
# Uploads to classes & checks for / adds users

def fileUpload(file):
    """
    unitList & unitStored & unitSimplify deals with particular user
    """
    def userFile(aFile):#'timetable-28464400.txt'
        unitFile = open(aFile, 'r')
        unitList = []

        #converts file into readable format (i.e. List)
        for line in unitFile:
            unitList.append(line)

        unitFile.close()
        unitStored = []
        #converts into usable name
        # 0 - Unit Code
        # 2 - Group
        # 3 - Session
        # 4 - Day && 5 - Time
        # 7 - Location
        #uniStored[4] = group
        #uniStored[5] = activity

        for i in range(1,len(unitList)):
            unitLine = unitList[i].strip().split("\t")
            unitName = unitLine[0].split("_")
            unitLine[0]=unitName[0]
            unitStrip = []
            unitStrip.append(unitLine[0])
            unitStrip.append(unitLine[2]+unitLine[3])
            unitStrip.append(unitLine[4]+unitLine[5])
            unitStrip.append(unitLine[7].replace("/","-"))
            unitStrip.append(unitLine[2])
            unitStrip.append(unitLine[3])
            unitStored.append(unitStrip)

        return unitStored

    def unitSimplify(aList):
        unitSimple = []
        for unit in aList:
            unitStore = unit[0]+"*"+unit[1]+"*"+unit[2]+"*"+unit[3]
            unitSimple.append(unitStore)
        return unitSimple

    unitOut = userFile(file)#'timetable-28464400.txt'

    unit = unitSimplify(unitOut) #every user has a unique "unit"

    # currentinclass = firebase.get("")

    user = ["swhhZrPWz6bT8y117abMEoPcZ7E2"] #swhhZrPWz6bT8y117abMEoPcZ7E2 #1ohqkJccSjeaUjTycaclF6eJSz43

    firebase.put("","users/"+str(user[0])+"/classes",unit)
    newUnit = [] #all units from single user
    for p in range(len(unit)):
        newUnit.append([])

    for x in range(len(unit)):
        newUnit[x].append(unitOut[x][0])
        newUnit[x].append(unitOut[x][4])
        newUnit[x].append(unitOut[x][5]+unitOut[x][2])

    # 0 - Unit Code
    # 1 - Group
    # 2 - Activity
    # 3 - Time
    # print(newUnit)
    # units = []
    # for i in range(len(newUnit)):
    #     for j in range(len(newUnit[i])):
    #         if newUnit[i] not in units:
    #             units.append([newUnit[i]])
    #
        # if [newUnit[i][0]] not in units: #change the fuck out of this in the future
        #     units.append([newUnit[i][0]])
        # print("1", units)

    # print(units)

    # d = {}
    # for each in units:
    #     d[]

        # currentTable = []
        # currentTable.append()

    # Makes Activity & Time into a table (Using previous newUnit [0] & [1] as "Index"
    """
    0. For Loop
    1. Check if equal unit code
    2. Check if group in specific unit code same
    3. Find old activities & firebase.get them
    4. Add old & new activities to single list (which corresponds to unit code & group)
    5. Upload list in accordance with unit/group/*


    table = []
    for n in range(len(unit)):
        table.append([newUnit[n][2] + newUnit[n][3]])
    print(table)
    """

    # Uploading Units to firebase: (Using Index as Directory & adds table at same index
    # for d in range(len(unit)):
    #     # firebase.put("", "units/" + str(newUnit[d][0]) + "/"+ str(newUnit[d][1])+'/',newUnit[d][2])
    #     print(newUnit[d][2])


    oldUsers = []
    for n in range(len(unit)):
        oldUsers.append([])
    temp = []

    for x in range(len(unit)):
        temp.append(firebase.get('','/classes/'+unit[x]+'/users/'))
        if temp[x] not in oldUsers[x] and temp[x] is not None:
            oldUsers[x].extend(temp[x])

        if user[0] not in oldUsers[x]:
            oldUsers[x].extend(user)

    #Uploading to firebase
    for i in range(len(unit)):
        dictionary = {'location': unitOut[i][3], 'time': unitOut[i][2], 'unitID': unitOut[i][0], 'group':unitOut[i][1],'users':oldUsers[i]}
        firebase.put("","/classes/"+str(unit[i]),dictionary)



fileUpload('timetable-10001000.txt')