"""
Python practice

"""
def twoToTheN(n,x=2):
	"""This function calculates 2^n given an input n. I did this by using exponentiation by squaring, making this run in log(n) time"""	
	if n==0:
		return 1
	elif n==1:
		return x
	elif n%2==0:
		return(twoToTheN((n/2),(x*x)))
	else:
		return(x*twoToTheN(((n-1)/2),(x*x)))
def mean(L):
	"""calculates the mean of a list"""
	y=0
	for item in L:
		y = y+item
	return ((float(y)/len(L))) 


def median(L):
	"""calculates the median of a givenlist"""
	z=len(L)
	x=L[z/2]
	y=L[((z/2)-1)]
	if z%2==0:
		ans=float((x+y))/2
		return ans
	else:
		return x

def bfs(tree,elem):
    """searches tree for elem in breadth first order"""
    q=[tree] #load tree into q
    while q: 
        temp=q.pop(0)#remove first branch
        value=temp[0]#analyze the first node of first branch
        print str(value)#print node
        if value==elem:#if element=node, return
            return True
        children=temp[1:]#pull all children of first node
        for child in children:
            q.append(child)#add children to end of list
    return False


def dfs(tree,elem):
    """searches tree for elem in depth first order"""
    q=[tree]
    while q:
        temp=q.pop()#remove LAST branch
        value=temp[0]#analyze first node of last branch
        print str(value)#print
        if value==elem:#if tlement=node, return
            return True
        children=temp[1:]
        for child in children:
            q.append(child)#add children to end of list
    return False


class TTTBoard:
	"""this is a class for a tic tac toe board game."""
	def __init__(self):
		self.board=["*","*","*","*","*","*","*","*","*"] #initialize board
	def __str__(self):
   		first=" ".join([self.board[0],self.board[1],self.board[2]])#create stars with spaces seperated by 3 lines
   		second= " ".join([self.board[3],self.board[4],self.board[5]])
   		third= " ".join([self.board[6],self.board[7],self.board[8]])
   		final="\n".join([first,second,third,])
   		return final+"\n"
   	def isFull(self):
   		"""determines whether board is full of players"""
   		for item in range(9):#if there is an open spot, return false
   			if self.board[item]=="*":
   				return False
		return True
	def makeMove(self,player,pos):
		"""move given player into spot on board"""
		if self.board[pos]=="*":
			self.board[pos]=player
			return True
		else: return False
	def hasWon(self,player):
		"""determines of a player has won given certain combinations"""
		return ((self.board[6] == player and self.board[7] == player and self.board[8] == player) or # across the bottom
    	(self.board[3] == player and self.board[4] == player and self.board[5] == player) or # across the middle
    	(self.board[0] == player and self.board[1] == player and self.board[2] == player) or # across the top
      	(self.board[6] == player and self.board[3] == player and self.board[0] == player) or # across left
      	(self.board[7] == player and self.board[4] == player and self.board[1] == player) or # across the middle
      	(self.board[8] == player and self.board[5] == player and self.board[2] == player) or # across the right 
      	(self.board[6] == player and self.board[4] == player and self.board[2] == player) or # diagonal
      	(self.board[8] == player and self.board[4] == player and self.board[0] == player)) # diagonal    
  	def gameOver(self):
  		"""determines whether the game is over or not"""
  		if (self.hasWon("X") or self.hasWon("O")) and self.isFull(): #if a player has won or board is full, game is over
  			return True
		else: 
			return False
	def clear(self):
		"""clears board"""
		self.board[0]="*" #restores board back to all stars
		self.board[1]="*"
		self.board[2]="*"
		self.board[3]="*"
		self.board[4]="*"
		self.board[5]="*"
		self.board[6]="*"
		self.board[7]="*"
		self.board[8]="*"




