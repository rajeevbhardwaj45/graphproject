# A simple representation of graph using Edge List
class Graph:
    def __init__( self, numvertex ):
        self.numvertex = numvertex
        self.vertices = []
        self.edgeList = []

    def set_vertex( self, vtx ):
        self.vertices.append(vtx)

    def set_edge( self, frm, to, cost=0 ):
        self.edgeList.append([frm, to])

    def get_vertex( self ):
        return self.vertices

    def get_edges( self ):
        return self.edgeList


# read the file to the Airport lists and the routes
f = open("inputPS12.txt", "r")

# To the Airports which separted as airports =
strAirports = f.readline()
strairportslists = strAirports.split("=")

# Split the Airports names which are separted by comma
lstairportNames = strairportslists[1].split(',')
lenAirports = len(lstairportNames)

# Create Graph class for Graph Edge Impementation and set the vertices as Airport name
G = Graph(lenAirports)
for i in range(lenAirports):
    lstairportNames[i] = lstairportNames[i].strip()
    G.set_vertex(lstairportNames[i])

# Read teh avilable airport paths which are identified as routes, Read the full paths till end of file. while reading each file
# seperate the strings which are comma sepearted and used to create the Edge
strRoutes = f.readline()
while strRoutes:
    strRoutes = f.readline()
    if (strRoutes == ''):
        break
    strRoutes = strRoutes.split(',')
    # G.set_edge(strRoutes[0].strip(),strRoutes[1].strip(),20)
    G.set_edge(strRoutes[0].strip(), strRoutes[1].strip())

f.close()

# flights to be added
nFlghts = []
# Avilable flights from starting airport.
yesFlights = []
# starting and destination airports.
edgeList = []
nVisited = []


# Recursive Function to find the minimum No: of Fights.
def flightsavilablesUsingList( strAirStpt, strAirdtpt, edgeList, nFlghts, yesFlight, nVisited ):
    bavailable = False

    for j in range(len(edgeList)):
        if (edgeList[j][1] == strAirdtpt):

            if (nVisited[j] == 0):
                nVisited[j] = 1
                if strAirdtpt in yesFlights:
                    bavailable = True
                    break
                else:
                    strAirdtpt = edgeList[j][0]

                    return flightsavilablesUsingList(strAirStpt, strAirdtpt, edgeList, nFlghts, yesFlight, nVisited)
            else:
                nVisited = [0] * len(edgeList)

    if (bavailable == False):
        if strAirdtpt not in yesFlights:
            nFlghts.append(strAirdtpt)
            yesFlights.append(strAirdtpt)
            G.set_edge(strAirStpt, strAirdtpt)

    return yesFlights, nFlghts, nVisited


def findMinFlightsusingList( strAirStpt ):
    edgeList = G.get_edges()
    nRows = len(edgeList)

    lstVertices = G.get_vertex()

    # Identify the Avilable routes of entered starting Airport and No avilable routes.
    for j in range(len(lstVertices)):
        noFlights = True
        for i in range(nRows):
            if (lstVertices[j] == edgeList[i][1]):
                noFlights = False
                break
        if (True == noFlights):
            nFlghts.append(lstVertices[j])
            yesFlights.append(lstVertices[j])
            G.set_edge(strAirStpt, lstVertices[j])

    for i in range(len(lstVertices)):
        nVisited = [0] * len(edgeList)
        if (lstVertices[i] != strAirStpt):
            flightsavilablesUsingList(strAirStpt, lstVertices[i], edgeList, nFlghts, yesFlights, nVisited)
            if lstVertices[i] not in yesFlights:
                yesFlights.append(lstVertices[i])

    nminFlights = len(nFlghts)
    print("The minimum flights that need to be added :", nminFlights)

    print("The flights that need to be added are:")

    # To Write to Output File.
    f = open("outputPS12.txt", "w")
    f.writelines("The minimum flights that need to be added =" + str(nminFlights) + "\n")
    f.writelines("The flights that need to be added are:" + "\n")
    for i in range(nminFlights):
        f.writelines("[" + strAirStpt + "," + nFlghts[i] + "]\n")
    f.close()

    print(nFlghts)


strAirportStpoint = input("Enter the starting Airport : ")
findMinFlightsusingList(strAirportStpoint)

