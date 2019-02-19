##
#Author: Will Roden
#CSC-544 Network Programming Project
#
#Purpose: This program simulates Dynamic Source Routing (DSR) by creating random nodes on a canvas, randomly selecting two nodes 
#to be the source and destination nodes, then finding the shortest path between the two nodes by simulating broadcast messages (RREQ) 
#and unicast replies (RREP). This program will generate a window utilizing Turtle Graphics and draw an animation of the simulation. 
#This program will also report on the terminal each broadcast/unicast message sent and received by and to whom, and the shortest path 
#between the source and destination nodes. To end the program, simply click inside the graphic's window.
##
from random import randint
import turtle
import math

class Node:
	def __init__(self, index, coordinates, range = 70):
		self.index = index
		self.x, self.y = coordinates
		self.range = range
		self.haveBroadcast = False
		self.neighbors = []
		self.receivedFrom = []
		self.destReceived = False
		self.hopCount = 9999
	
	def isInRange(self, other):
		if math.sqrt(((self.getX() - other.getX())**2) + ((self.getY() - other.getY())**2)) <= (self.range + other.range):
			return True
		else:
			return False
					
	def setNeighbors(self, nodeList):
		nodeNeighborsList = []
		for node in nodeList:			
			if node != self and node.isInRange(self):
				nodeNeighborsList.append(node.getIndex())
		self.neighbors = nodeNeighborsList	
					
	def drawNode(self, color = 'black'):
		turtle.color(color)
		turtle.penup()
		turtle.setposition(self.getX(), self.getY())
		turtle.pendown()
		turtle.dot()
		turtle.write(self.index, move = False, align = "center")
		turtle.penup()
		turtle.sety(self.getY() - 70)
		turtle.pendown()
		turtle.circle(70)
		turtle.penup()
		
	def getHopCount(self):
		return self.hopCount
		
	def setHopCount(self, hc):
		self.hopCount = hc
	
	def getNeighbors(self):
		return self.neighbors
	
	def broadcast(self):		
		self.setHaveBroadcast(True)
		
	def receivedBroadcast(self, index):
		self.receivedFrom.append(index)
		
	def getHaveBroadcast(self):
		return self.haveBroadcast
		
	def setHaveBroadcast(self, tf):
		self.haveBroadcast = tf
		
	def getReceivedFrom(self):
		return self.receivedFrom
		
	def getIndex(self):
		return self.index
		
	def setIndex(self, i):
		self.index = i
		
	def getX(self):
		return self.x
		
	def setX(self, x):
		self.x = x
		
	def getY(self):
		return self.y
		
	def setY(self, y):
		self.y = y
		
	def getRange(self):
		return self.range
		
	def setRange(self, r):
		self.range = r
		
	def getDestReceived(self):
		return self.destReceived
	
	def setDestReceived(self, tf):
		self.destReceived = tf

def RREQ(nodeList, source, destination):
'''This function simulates an RREQ from the source node to find the destination node'''
    current = source
    q = [current]
    nodeList[current].setHopCount(0)    
    while len(q) > 0:
        if current == destination:            
            nodeList[current].setDestReceived(True)
        elif not nodeList[current].getHaveBroadcast():
            nodeList[current].broadcast()
            print("Node " + str(current) + " sent a RREQ broadcast message")
            for node in nodeList[current].getNeighbors():
                nodeList[node].receivedBroadcast(current)
                print("Node " + str(node) + " received a RREQ broadcast message from " + str(current))
                q.append(node)
                if nodeList[node].getHopCount() > nodeList[current].getHopCount() + 1:
                    nodeList[node].setHopCount(nodeList[current].getHopCount() + 1)        
        current = q.pop(0)
	
def RREP(nodeList, current, source):
'''This function simulates an RREP response that determines the shortest path between nodes'''
    path = [current]
    while current != source:
        received = nodeList[current].getReceivedFrom()        
        hops = 9999
        for node in received:
            if nodeList[node].getHopCount() < hops:
                hops = nodeList[node].getHopCount()
                shortestPath = node
        path.append(shortestPath)		
        current = shortestPath
    return path
	
def drawPath(path, nodeList):
'''This function draws the calculated shortest path between two nodes'''
	turtle.color('red')
	turtle.pensize(1.5)
	turtle.penup()
	count = 0
	for index in path:		
		turtle.setposition(nodeList[index].getX(), nodeList[index].getY())
		turtle.pendown()
		if index != path[len(path) - 1]:
			print("Node " + str(index) + " sent a RREP unicast message to " + str(path[count + 1]))
		else:
			print("Node " + str(index) + " received a RREP message from " + str(path[count - 1]))
		count += 1
		
def makeEveryNodeHaveANeighbor(nodeList, coordinateList):
'''Ensures that every node in the simulation will have another node within range.'''
	hadToChangeNode = True
	while hadToChangeNode:
		hadToChangeNode = False
		for node in nodeList:
			if node.getNeighbors() == []:
				hadToChangeNode = True
				x = randint(-250,250)
				y = randint(-250,250)
				coordinates = x, y 
				if coordinates not in coordinateList:
					node.setX(x)
					node.setY(y)					
		for node in nodeList:
			node.setNeighbors(nodeList)	
		
def main():
	count = 0
	coordinateList = []	
	while count < 50:
		x = randint(-250,250)
		y = randint(-250,250)
		coordinates = x, y 
		if coordinates not in coordinateList:
			coordinateList.append(coordinates)
			count += 1	
	nodeList = []
	for i in range(len(coordinateList)):
		nodeList.append(Node(i, coordinateList[i]))
	for node in nodeList:
		node.setNeighbors(nodeList)
	makeEveryNodeHaveANeighbor(nodeList, coordinateList)	
	source = randint(0, len(nodeList)-1)
	dest = source
	while dest == source:
		dest = randint(0, len(nodeList)-1)
	print("Source Node:",source,"\nDestination Node:", dest)	
	RREQ(nodeList, source, dest)	
	if nodeList[dest].getDestReceived():
		path = RREP(nodeList, dest, source)
		print("\nPath back to Source Node:", path, end="\n\n")
	else:
		print("Destination didn't receive message")
		path = None

#---------------------------Drawing-----------------------------------
	
	win = turtle.Screen()	
	turtle.setup(701,701)
	turtle.delay(0)
	turtle.hideturtle()
	for node in nodeList:
		if node.getIndex() == source or node.getIndex() == dest:
			color = 'red'
		else:
			color = 'black'
		node.drawNode(color)
	if path != None:
		drawPath(path, nodeList)	
	win.exitonclick()	
	
		
if __name__ == '__main__':
	main()
