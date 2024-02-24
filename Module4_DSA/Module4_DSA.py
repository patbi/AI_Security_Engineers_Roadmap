"""
* DATA STRUCTURES:

	Why we need to use data structure ?

	- Data structures: to store in an efficient way
	
	Why to use data structures ?

	- We often have the intuition --> if we want to make an algorithm fast,
		we have to optimize it
	- Avoid nested for loops
	- Make every calculation as fast as possible
	- But algorithms can be boosted up by proper data structures
	- Data structures make sure the running time will be better
	- Dijkstra algorithm
	- Without a proper data structure (heap / priority queue ) the running
		time would be quadratic // O(N²) 
	- Priority queue approach makes sure the running time will be far
		better // O(N*logN)
"""



"""
* Difference between Data structures and Abstract Data Types (ADT)


- Abstract data types:

	- Basically this is the model(logical description) for a certain data structure
	- It is like a supertype in programming (so an interface in Java)
	- We just define what methods / functions the data structure will have,
		so we define the basic behavior
	- IMPORTANT: it is just the model, ADT does not specify the concrete implementation
		or programming language
	- "Basically what the user knows"
	- For example: stack --> push() pop() peek()

	abstract data types(1-Stack, 2-Queue, 3-Priority queue, 4-Dictionary / hashmap)
	data structures (1-array,linked list. 2-array,linked list. 3-heap. 4-array)

- Data structure:

	- The concrete implementation, the actual representation of the data
	- The aim is to be able to store and retrieve data in an efficient manner
	- What we want: to be able to insert / find items in O(1) time complexity and to be able to retrieve items in O(1) as well
	- For example: arrays, linked lists, banary trees ...

"""



"""
* How to install python

url: https://www.python.org/downloads/
"""


"""
1 - Arrays Getting Started: in python: data structures

A collection of elements / values
each identified by an array index or key.

	- index starts at zero
	- because of the indexes: random access is possible


* Multidimensional arrays: it can prove to be very important in mathematical related computations (matrixes)
	- numbers[][] two dimensional array
	- First parameter: row index, Second parameter: column index


* Arrays:

- Arrays are data structures in order to store items of the same type
- We use indices as keys 
- Arrays can have as many dimensions as we want: one or two dimensional arrays are quite popular
- For example:storing a matrix --> two dimensional array
- Dynamic array: when the size of the array is changing dynamically
- Applications: looking tables / hashtables, heaps


* Advantages:
- We can use random access because of the keys: getItem(int index)
		will return the value with the given key very fast // O(1)
- Very easy to implement and to use 
- Very fast data struxture
- We should use arrays in applications when we want to add items over and over again and we want to take items with given indexes~ it will be fast


* Disadvantages:
- We have to now the size of the array at compile-time: so it is not so dynamic data structure
- If it is full: we have to create a bigger array and have to copy the values one by one // reconstructing an array is 0(N) operation
- It is not able to store items with different types

"""


"""
* Arrays all operations in python

	- Arrays operation: add
		We can keep adding values to the array as far the array is not full
		So: when adding new values to the list, we just have to insert it with the next index --> very fast O(1) operation
	
	- Arrays operation: insert item
		We would like to insert a given value with a given index
		So: it is a bit more problematic, sometime we have to shift lots of values in order to be able to insert the new one ~ O(N) time complexity

		Add new item: O(1)
		Insert item to a given index: O(N)

	
	- Arrays operation: remove items
		removeLast(): We would like to remove the last item, it is very simple, just remove it // O(1) time complexity
		
		remove(1) - Arrays operation: remove items with given index we would like to remove a value with a given, it is not that simple, we may have to shift items // O(N) time complexity
		So: overall complexity will be linear O(N)
	

		removing last item: O(1)
		removing first item,middle item: O(N)
"""



"""
* Arrays in Python
"""

#numbers = [25.5,20,10,40,30,50,70];
#random indexing --> O(1) get items if we know the index

#print(numbers[5]);
#numbers[5] = 100;
#numbers[5] = 'Thenavigo';
#print(numbers[5]);

#for num in numbers:
#    print(num);

#for i in range(len(numbers)):
#    print(numbers[i]);

#print(numbers[0:2]);


#O(N) search running time
#maximum = numbers[0];
#for num in numbers:
#    if num > maximum:
#        maximum = num;

#print(maximum);



"""
2 - Linked list in python

- Linked lists are composed of nodes and references / pointers pointing from one node to the other.
The last reference is pointing to a NULL

	* A single node:
		- contains data --> integer, double or custom object 
		- contains a reference pointing to the next node in the linked list

	class Node {
		data
		Node nextNode


		...
	}


- Each node is composed of a data and a reference/link to the next node in the sequence
- Simple and very common data structure
- They can be used to implement several other common data types: stacks, queues
- Simple linked lists by themselves do not allow random access to the data // so we can not use indexes ..getItem(int index)
- Many basic operations such as obtaining the last node of the list or finding a node that
	contains a given data or locating the place where a new node should be inserted --require sequential scanning of most or all of the list elements


	* Advantages:
	
	- Linked lists are dynamic data structures (arrays are not)
	- It can allocate the needed memory in run-time
	- Very efficient if we want to manipulate the first elements
	- Easy implementation
	- Can store items with different sizes: an array assumes every element to be exactly the same
	- It's easier for a linked list to grow organically. An array's size needs to be known ahead of time, or re-created when it needs to grow



	* Disadvantages:
	- Waste memory because of the references
	Nodes in a linked list must be read in order from the beginning as linked lists have sequential access (array items can reached via indexes in O(1) time)
	- Difficulties arise in linked lists when it comes to reverse traversing.
	Singly linked lists are extremely difficult to naigate backwards.
	- Solution: doubly linked lists --> easier to read, but memory is wasted is allocating space for a back pointer
"""


"""
* Linked list operations: insertion

	- Inserting items at the beginning of the linked list: very simple, we just have to update the references --> O(1) time complexity

	linkedList.insertAtStart(10);
	linkedList.insertAtStart(4);
	linkedList.insertAtStart(-5);

	- Inserting items at the end of the linked list: not thatvery simple, we have to traverse the whole linked list to find the last node.
		How do we find the last node ? We know the last node is pointing to a NULL.

		Plus we have to update the references when we get there O(N) time complexity

			- Insert at the beginning O(1)
			- Inserting at the end O(N)

* Linked list operations: remove

	- Remove item at the beginning of the list is always very fast: we do not have to search the item, we just have to update the references accordingly O(1) time complexity

linkedList.removeStart()

	- Remove item at a given point of the list is not always very fast: we have to searLinked list operations: insertionh for the given item whiLinked list operations: insertionh may take lot of time
		if the item is at the end of the list O(N) time complexity
linkedList.remove(10)

		- Remove items at the beginning: O(1)
		- Remove items at given positions: O(N) in the main

"""


"""
* Doubly linked list in python

	- Problems with linked lists:
	
	Fo example: 12 --> 4 --> 123 --> (-7) --> 25 --> NULL

	We can get from 4 to 25 because we just have to hop to the next nodes BUT we can not go from 25 to 4 because the references are in the opposite directions

	- Solution: doubly linked list --> Node class has two references, one pointing to the next node, one pointing to the previous node.

	12 <-- 4 <-- 123 <-- (-7) <-- 25 
					  --> NULL
	12 --> 4 --> 123 -->  (-7) --> 25 	
"""



"""
* linked lists vs arrays

	1) Search:

	- Search operation yields the same result for both data structure
	- ArrayList search operation is pretty fast compared to the LinkedList search operation
	- We can use random access with arrays: getItem(int index) which is O(1) time complexity
	- LinkedList performance is O(N) time complexity
	- So the conclusion: ArrayList is better for this operation
	- Why ?
	- ArrayList maintains index based system for its elements as it uses array data structure implicity which makes it faster for searching an element in the list
	- On the other hand LinkedList requires the traversal through all the items for searching an element


	2) Deletion:

	- LinkedList remove operation takes O(1) time if we remove items from the beginning and usually this is the case
	- ArrayList: removing first element ( so at the beginning ) takes O(N) time, removing the last item takes O(1) times
	- But on average: we have to reconstruct the array when removing
	- So the conclusion: LinkedList is better for this operation
	- Why ?
	- LinkedList basically operates with pointers: removal only requires change in the pointer location which can be done very fast


	3) Memory management:

	- Arrays do not need any extra memory
	- LinkedLists on the other hand do need extra memory because of the references / pointers
	- So in this aspect: arrays are better, they are memory friendly 



			   LinkedList         Arrays
Search                      O(N)               O(1)
Insert at the start         O(1)               O(N)
Insert at the end           O(N)               O(1)
Waste space                 O(N)               0

"""


"""
* Linked list insertion implementation in python

"""

class Node(object):

	def __init__(self, data):
		self.data = data;
		self.nextNode = None;


class LinkedList(object):

	def __init__(self):
		self.head = None;
		self.size = 0;


	#O(1)
	def insertStart(self, data):
		self.size = self.size + 1;
		newNode = Node(data);

		if not self.head:
			self.head = newNode;
		else:
			newNode.nextNode = self.head;
			self.head = newNode;

	#Linked list implementation in python (remove)

	def remove(self, data):
		if self.head is None:
			return;

		self.size = self.size - 1;

		currentNode = self.head;
		previousNode = None;

		while currentNode.data != data:
			previousNode = currentNode;
			currentNode = currentNode.nextNode;

		if previousNode is None:
			self.head = currentNode.nextNode;
		else:
			previousNode.nextNode = currentNode.nextNode;



	#O(1)
	def size1(self):
		return self.size;


	# O(N) not good
	def size2(self):
		actualNode = self.head;
		size = 0;


		while actualNode is not None:
			size+=1;
			actualNode = actualNode.nextNode;

		return size;

	#Linked list implementation in python (travese)

	def insertEnd(self, data):

		self.size = self.size + 1;
		newNode = Node(data);
		actualNode = self.head;

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode;

		actualNode.nextNode = newNode;


	def traverseList(self):
		actualNode = self.head;

		while actualNode is not None:
			print("%d " % actualNode.data);
			actualNode = actualNode.nextNode;


#Linked list implementation testing in python
linkedlist = LinkedList();

linkedlist.insertStart(12);
linkedlist.insertStart(125);
linkedlist.insertStart(4);
linkedlist.insertEnd(48);

linkedlist.traverseList();
print(linkedlist.size1());

linkedlist.remove(48);
linkedlist.remove(12);
linkedlist.remove(125);
linkedlist.remove(4);

print(linkedlist.size1());



"""
* Doubly linked list in python

Problems with linked lists:

	12 <-- 4 <-- 123 <-- (-7) <-- 25 
					  --> NULL
	12 --> 4 --> 123 -->  (-7) --> 25 



We can get from 4 to 25 because we just have to hop to the next node BUT we can
not go from 25 to 4 because the references are in the opposite directions.

Solution: doubly linked list --> Node class has two references, one pointing to the next node, one pointing to the previous node


Ok we can get from eveywhere to everywhere BUT it is not so memory friendly,
we have to store lots of references

BUT there is no need to track the previous node during traversal

"""





"""
* Stack in python

	- It is an abstract data type (interface)
	- Basic operations: pop(), push(), and peek()
	- LIFO structure: last in first out
	- In most high level languages, a stack can be easy implemented either with arrays or linked lists
	- A number of programming languages are stack-oriented, meaning they define most basic operations (adding two numbers, printing a character) as taking their arguments from the stack, and placing any return values back on the stack


-- Push operation: put the given item to the top of the stack very simple operation, can be done in O(1)
stack.push(10000);

-- Pop operation: we take the last item we have inserted to the top of the stack (LIFO) very simple operation, can be done in O(1)
stack.pop();

-- Peek operation: return the item from the top of the stack without removing it very simple operation, can be done in O(1)
stack.peek();


-- Applications:

	- In stack-oriented programming languages
	- Graph algorithms: depth-first search can be implemented with stacks (or with recursion)
	- Finding Euler-cycles in a graph
	- Finding strongly connected components in a graph
"""


"""
* Stack in memory

	- Most important application of stacks: stack memory
	- It is a special region of the memory (in the RAM)
	- A call stack is an abstract data type that stores information about the active subroutines / methods / functions of a computer program
	- The details are normally hidden and automatic in high-level programming
	- Why is it good ?
	- It keeps track of the point to which each active subroutine should return control when it finishes executing
	- Stores temporary variables created by each function
	- Every time a function declares a new variable it is pushed onto the stack
	- Every time a function exits all of the variables - pushed onto the stack by that function - are freed --> all of its variables are popped off of the stack // and lost forever
	- Local variables: they are on the stack, after function returns they are lost
	- Stack memory is limited.
	diff(limited in size, fast access, local variables, space is managed efficiently by CPU, variables cannot be resized)

* Heap memory:
	- The heap is a region of memory that is not managed automatically for you
	- This is a large region of memory // unlike stack memory
	- C: malloc() and calloc() function // with pointers
	- Java: reference types and objects are on the heap
	- We have to deallocate these memory chunks: because it is not managed automatically
	- If not: memory leak
	- Slower because of the pointers
	diff(no size limits, slow access, objects, memory may be fragmented, variables can be resized // realloc())
"""



"""
* Stack and recursion

	- There are several situations when recursive methods are quite handy
	- For example: DFS, traversing a binary search tree, looking for an item in a linked list ...
	- What's happening in the background ?
	- All the recursive algorithms can be transformed into a simple method with stacks
	- IMPORTANT: if we use recursion, the OS will use stacks anyways

-- Depth-first search:

#recursion

public void dfs(Vertex vertex) {
	vertex.setVisited(true);
	printf(vertex);
	for(Vertex v: vertex.neighbours()) {
		if(!v.isVisited()) {
			dfs(v);
		}
	}
}	


#iterative approach with stack

public void dfs(Vertex vertex) {
	Stack stack;
	stack.push(vertex);

	while(!stack.isEmpty()){
		actual = stack.pop();
		for(Vertex v: actual.neighbours()) {
			if(!v.isVisited()) {
				v.setVisited(true);
				stack.push(v);
			}
		}
	}
}


-- Factorial: with recursion

public void factorial(int n) {
	if(n==0)
		return 1;
	return n*factorial(n-1);
}

This is the factorial function with Recursive implementation
n! = n*(n-1)*...*2*1

For example: 4! = 4*3*2*1 = 24
"""


"""
* Stack implementation in python
	- It is an abstract data type (interface)
	- Basic operations: pop(), push() and peek()
	- LIFO structure: last in first out
	- In most high level languages, a stack can be easy implemented either with arrays or linked lists
	- A number of programming languages are stack-oriented, meaning they define most basic operations (adding two numbers, printing a character) as taking their arguments from the stack, and placing any return values back on the stack



"""


class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def sizeStack(self):
		return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print(stack.sizeStack())
print("Peek:", stack.peek())
print(stack.sizeStack())



"""
* Queue in python
	- It is an abstract data type (interface)
	- Basic operations: enqueue() and dequeue(), peek()
	- FOFO structure: first in first out
	- It can be implemented with dynamic arrays as well as with linked lists
	- Important when implementing BFS algorithm for graphs

Enqueue operation: we just simply add the new item to the end of the queue

queue.enqueue(20);

Dequeue operation: we just simply remove the item starting at the beginning of the queue // FIFO structure	
queue.dequeue();


Applications:
	- When a resource is shared with several consumers (threads): we store them in a queue
	- For example: CPU scheduling
	- When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes
	- For example: IO buffers
	- Operationel research applications or stochastic models relies heavily on queues

"""

#queue implementation in python
class Queue:
	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def sizeQueue(self):
		return len(self.queue)

queue = Queue()
queue.enqueue(150)
queue.enqueue(250)
queue.enqueue(350)
print(queue.sizeQueue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print(queue.sizeQueue())

"""
* Binary search tree python

	- Binary search trees are data structures
	- Keeps the keys in sorted order: so that lookup and other operations can use the principle of binary search
	- Each comparison allows the operations to skip over half of the tree, so that each lookup/insertion/deletion takes time proportional to the algorithms of the number of items stored in the tree
	- This is much better than the linear time O(N) required to find items by key in an unsorted array, but slower than the corresponding operations on hash tables


Sorted arrays(Inserting a new item is quite slow // o(N), Searching is quite fast with binary search // O(logN), Removing an item is slow // O(N))
Inserting a new item is very fast // O(1), Searching is sequential //O(N), Removing an item is fast because of the references // O(1)	

Binary search trees are going to make all of these operations quite fest, with O(log N) time complexity

"""



"""
* Binary search tree-insert

Insertion: we start at the root node. If the data we want to insert is greater than the root node we go to the right, if it is smaller, we go to the left

	binarySearchTree.insert(10);

Search: we start at the root node. If the data we want to find is greater than the root node we go to the right, if it is smaller, we go to the left until we find.

	binarySearchTree.find(10);
"""



"""
* Binary search tree-delete

Delete: soft delete --> we do not remove the node from the BST we just mark that it has been removed ~ not so efficient solution

In the main three possible cases:
	1.) The node we want to get rid of is a leaf node
	2.) The node we want to get rid of has a single child
	3.) The node we want to get rid of has 2 children
"""



"""
* Binary search tree-traversal in python
	1.) In-order traversal: we visit the left subtree + the root node + the right subtree recursively
	2.) Pre-order traversal: we visit the root + left subtree + the right subtree recursively
	3.) POst-order traversal: we visit the left subtree + right subtree + the root recursively
"""


"""
* Binary search tree running time

	        Average case           Worst case
Space           O(n)                   O(n)
Insert          O(log n)               O(n)
Delete          O(log n)               O(n)
Search          O(log n)               O(n)
	

What about the worst case scenarios ?
	- if the tree becomes unbalanced: the operations running times can be reduced to O(N) in the worst case
	- that why it is important to keep a tree as balanced as possible
"""



"""
* Binary search tree in python (BST)
"""


#Binary search tree insertion in python (BST)
class Node(object):
	def __init__(self, data):
		self.data = data;
		self.leftChild = None;
		self.rightChild = None;


class BinarySearchTree(object):

	def __init__(self):
		self.root = None;

	def insert(self, data):
		if not self.root:
			self.root = Node(data);

		else:
			self.insertNode(data, self.root);

	# O(LogN)  if the tree is balanced!!! --> it can reduced to O(N) --> AVL are needed
	def insertNode(self, data, node):
		if data < node.data:
			if node.leftChild:
				self.insertNode(data, node.leftChild);
			else:
				node.leftChild = Node(data);
		else:
			if node.rightChild:
				self.insertNode(data, node.rightChild);
			else:
				node.rightChild = Node(data);

	#Binary search tree travercing in python

	def getMinValue(self):
		if self.root:
			return self.getMin(self.root);

	def getMin(self, node):

		if node.leftChild:
			return self.getMin(node.leftChild);

		return node.data;

	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root);

	def getMax(self, node):

		if node.rightChild:
			return self.getMax(node.rightChild);

		return node.data;

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root);

	def traverseInOrder(self, node):

		if node.leftChild:
			self.traverseInOrder(node.leftChild);

		print("%s " % node.data);

		if node.rightChild:
			self.traverseInOrder(node.rightChild);


#Binary search tree testing
bst = BinarySearchTree();
bst.insert(10);
bst.insert(5);
bst.insert(15);
bst.insert(6);
print(bst.getMaxValue());
bst.traverse();



"""
* AVL tree in data structure python
	- Linked lists: quite easy to implement
		Stores lots of pointers
			O(N) search operation time complexity
			
	- Binary search trees: we came to conclusion that O(N) search complexity
		can be reduced to O(logN) time complexity
			But if the tree is unbalanced: these operations will become
				slower and slower
	
	- Balanced binary trees: AVL trees or red-black trees they are guaranteed to be balanced 
		Why is it good ? O(logN) is guaranteed
		
Conclusion: if we construct a binary search tree from a sorted array, we end up with a linkedlist
	O(logN) reduced to O(N)
"""


"""
* AVL tree rotation case
	
	- Case 1: rightRotate

		BEGIN rotateRight(Node node)
			Node tempLeftNode = node.getLeftNode()
			Node t = tempLeftNode.getRightNode()

			tempLeftNode.setRightNode(node)
			node.setLeftNode(t)

			node.updateheight()
			tempLeftNode.updateHeight()
		END
	
	- Case II leftRotate:

		BEGIN rotateLeft(Node node)

			Node tempRightNode = nodes.getRightNode()
			Node t = tempRightNode.getLeftNode()

			tempRightNode.setLeftNode(node)
			node.setRightNode(t)

			node.updateheight()
			tempRightNode.updateheight()
		END

	Case III: 
		- We have to make a left rotation an the node B (D-->B-->C)
		- We have to make a left rotation on the root node D (D-->C-->B)


	Case IV:
		- We have to make a left rotation on the root node D (D-->E-->F)

"""


"""
* AVL tree illustration
	- Link: https://www.programiz.com/dsa/avl-tree

"""


#AVL tree height balance implementation in python
class Node(object):

	def __init__(self, data):
		self.data = data;
		self.height = 0;
		self.leftChild = None;
		self.rightChild = None;

class AVL(object):
	
	def __init__(self):
		self.root = None;

	def insert(self, data):
		self.root = self.insertNode(data, self.root);

	def insertNode(self, data, node):

		if not node:
			return Node(data);

		if data < node.data:
			node.leftChild = self.insertNode(data, node.leftChild);
		else:
			node.rightChild = self.insertNode(data, node.rightChild);

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

		return self.settleViolation(data, node);

	#AVL tree violance implementation in python
	def settleViolation(self, data, node):
		balance = self.calcBalance(node);

		if balance > 1 and data < node.leftChild.data:
			print("Left left heavy situation...");
			return self.rotateRight(node);

		if balance < -1 and data > node.rightChild.data:
			print("Right right heavy situation...");
			return self.rotateLeft(node);

		if balance > 1 and data > node.leftChild.data:
			print("Left right heavy situation...");
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rightChild(node);

		if balance < -1 and data < node.rightChild.data:
			print("Right left heavy situation...");
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

	def calcHeight(self, node):

		if not node:
			return -1;
		
		return node.height;

	# if it returns value > 1 it means it is a left heavy tree --> right rotation
	# ......
	def calcBalance(self, node):

		if not node:
			return 0;

		return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

	def rotateRight(self, node):

		print("Rotating to the right on node ", node.data);

		tempLeftChild = node.leftChild;
		t = tempLeftChild.rightChild;

		tempLeftChild.rightChild = node;
		node.leftChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1;
		return tempLeftChild;


	def rotateLeft(self, node):
		print("Rotating to the left on node ", node.data);

		tempRightChild = node.rightChild;
		t = tempRightChild.leftChild;

		tempRightChild.leftChild = node;
		node.rightChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1;
		return tempRightChild;

"""
* AVL tree introduction

	- The running time of BST operations depends on the height of the binary search
		tree: we should keep the tree balanced in order to get the best performance
	- Thats why AVL trees came to be
	- 1962: invented by two russian computer scientist
	- In an AVL tree, the heights of the two child subtrees of any node differ by at most one
	- Another solution to the problem is a red-black trees
	- AVL trees are faster than red-black trees because they are more rigidly balanced BUT needs more work
	- Operating systems relies heavily on these data structures!!!
	- Most of the operations are the same as we have seen for binary search trees
	- Every node can have at most 2 children: the leftChild is smaller, the rightChild is greater than the parent node
	- The insertion operation is the same BUT on every insertion we have to check whether the tree is unbalanced or not
	- Delete operation is the same
	- Maximum / Minimum finding operations are the same as well.

	balancedTree.find(40);
	findMin();

	* Binary search trees

			   Average case         Worst case
Space                       O(N)               	   O(n)
Insert                      O(log n)               O(n)
Delete                      O(log n)               O(n)
Search                      O(log n)               O(n)


	* Balanced trees

			   Average case         Worst case
Space                       O(N)               	   O(n)
Insert                      O(log n)               O(log n)
Delete                      O(log n)               O(log n)
Search                      O(log n)               O(log n)

"""




# AVL tree rotation implementation in python
class Node(object):

	def __init__(self, data):
		self.data = data;
		self.height = 0;
		self.leftChild = None;
		self.rightChild = None;

class AVL(object):

	def __init__(self):
		self.root = None;

	def calcHeight(self, node):
		return -1;

		return node.height;

	def calcBalance(self, node):

		if not node:
			return 0;

		return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

	def rotateRight(self, node):

		print("Rotating to the right on node ", node.data);

		tempLeftChild = node.leftChild;
		t = tempLeftChild.rightChild;

		tempLeftChild.rightChild = node;
		node.leftChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1;
		return tempLeftChild;


	def rotateLeft(self, node):
		print("Rotating to the left on node ", node.data);

		tempRightChild = node.rightChild;
		t = tempRightChild.leftChild;

		tempRightChild.leftChild = node;
		node.rightChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1;
		return tempRightChild;





"""
* AVL tree application
	
	- We can use this data structure to sort items
	- We just have to insert the N items we want to sort
	- We have to make an in-order traversal -> it is going to yield the numerical or alphabetical ordering.

		* Insertion: O(N*logN)
		* In-order traversal: O(N)
		* Overall complexity: O(N*logN)

	--Applications:

		* Databases when deletions or insertions are not so frequent, but have to make a lot of look-ups
		* Look-up tables usually implemented with the help of hashtables BUT AVL tress support more operations in the main
		* We can sort with the help of AVL trees
		* Red-black trees are a bit more popular because for AVL trees we have to make several rotations ~ a bit slower

"""



"""
* AVL tree height introduction

	- AVL tree requires the heights of left and right child of every node to differ at most +1 or -1
	- | height(leftSubtree) - height(rightSubtree) | < = 1
	- We can maintain this property in O(logN) time which is quite fast
	- Insertion:

		1.) a simple BST insertion according to the keys
		2.) fix the AVL property on each insertion from insertion upward

	- There may be several violations of AVL property from the inserted node up to the root
	- We have to check them all   
"""


#AVL tree node implementation in python
class Node(object):

	def __init__(self, data):
		self.data = data;
		self.height = 0;
		self.leftChild = None;
		self.rightChild = None;

class  AVL(object):

	def __init__(self):
		self.root = None;

	#AVL tree remove implementation in python
	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root);

	#AVL tree insertion implementation in python
	def insert(self, data):
		self.root = self.insertNode(data, self.root);

	def insertNode(self, data, node):

		if not node:
			return Node(data);

		if data < node.data:
			node.leftChild = self.insertNode(data, node.leftChild):
		else:
			node.rightChild = self.insertNode(data, node.rightChild);

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

		return self.settleViolation(data, node);

	def removeNode(self.data, node):

		if not node:
			return node;

		if data < node.data:
			node.leftChild = self.removeNode(data, node.leftChild);
		elif data > node.data:
			node.rightChild = self.removeNode(data, node.rightChild);
		else:

			if not node.leftChild and not node.rightChild:
				print("Removing a left node...");
				del node;
				return node;

			if not node.leftChild:
				print("Removing right child...");
				tempNode = node.rightChild;
				del node;
				return tempNode;
			elif not node.rightChild:
				print("Removing left child...");
				tempNode = node.leftChild;
				del node;
				return tempNode;

			print("Removing node with two children...");
			tempNode = self.getPredecessor(node.leftChild);
			node.data = tempNode.data;
			node.leftChild = self.removeNode(tempNode.data, node.leftChild);

		if not node:
			return node; # if the tree had just a single node

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

		balance = self.calcBalance(node);

		# doubly left heavy situation
		if balance > 1 and self.calcBalance(node.leftChild) >= 0:
			return self.rotateRight(node);

		# left right case
		if balance > 1 and self.calcBalance(node.leftChild) < 0:
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rotateRight(node);

		# right right case
		if balance < -1 and self.calcBalance(node.rightChild) <=0:
			return self.rotateLeft(node);

		# right left case
		if balance < -1 and self.calcBalance(node.rightChild) > 0:
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

		return node;

	def getPredecessor(self, node):

		if node.rightChild:
			return self.getPredecessor(node.rightChild);

		return node;

	def settleViolation(self, data, node):

		balance = self.calcBalance(node);

		if balance > 1 and data < node.leftChild.data:
			print("Left left heavy tree...");
			return self.rotateRight(node);

		if balance < -1 and data > node.rightChild.data:
			print("Right right heavy tree...");
			return self.rotateLeft(node);

		if balance > 1 and data > node.leftChild.data:
			print("Tree is left right heavy...");
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rotateRight(node);

		if balance < -1 and data < node.rightChild.data:
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

		return node;

	def settleViolation(self, data, node):

		balance = self.calcBalance(node);

		if balance > 1 and data < node.leftChild.data:
			print("Left left heavy tree...");
			return self.rotateRight(node);

		if balance < -1 and data > node.rightChild.data:
			print("Right right heavy tree...");
			return self.rotateLeft(node);

		if balance > 1 and data > node.leftChild.data:
			print("Tree is left right heavy...");
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rotateRight(node);

		if balance < -1 and data < node.rightChild.data:
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

		return node;

	def getPredecessor(self, node):

		if node.rightChild:
			return self.getPredecessor(node.rightChild);

		return node;

	def settleViolation(self, data, node):

		balance = self.calcBalance(node);

		if balance > 1 and data < node.leftChild.data:
			print("Left left heavy tree...");
			return self.rotateRight(node);

		if balance < -1 and data > node.rightChild.data:
			print("Right right heavy tree...");
			return self.rotateLeft(node);

		if balance > 1 and data > node.leftChild.data:
			print("Tree is left right heavy...");
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rotateRight(node);

		if balance < -1 and data < node.rightChild.data:
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

		return node;

	def calcHeight(self, node):

		if not node:
			return -1;

		return node.height;

	def calcBalance(self, node):

		if not node:
			return 0;

		return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root);

	def traverseInOrder(self, node):

		if node.leftChild:
			self.traverseInOrder(node.leftChild);

		print("% " % node.data);

		if node.rightChild:
			self.traverseInOrder(node.rightChild);

	def rotateRight(self, node):

		print("Rotating to the right on node ", node.data);

		tempLeftChild = node.leftChild;
		t = tempLeftChild.rightChild;

		tempLeftChild.rightChild = node;
		node.leftChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1;
		return tempLeftChild;

	def rotateLeft(self, node):
		print("Rotating to the left on node ", node.data);

		tempRightChild = node.rightChild;
		t = tempRightChild.leftChild;

		tempRightChild.leftChild = node;
		node.rightChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1;
		return tempRightChild;


#AVL Testing

av1 = AVL();
av1.insert(20);
av1.insert(10);
av1.insert(5);
av1.insert(7);
av1.insert(9);

av1.remove(10);
av1.remove(7);

av1.traverse();


"""
* Priority queue in data structure

	- It is an abstract data type such as stack or queue
	- BUT every item has an additional property: a priority value
	- In a priority queue, an element with high priority is served before an element with lower priority
	- Priority queues are usually implemented with heaps, but it can be implemented with self balancing trees as well
	- Very similar to queues with some modification: when we would like to get the next item --> the highest priority element is retrieved first.
		- No FIFO structure here

	-- Abstract Data Types: (Specification Interfaces ) < --- >  Data Structures (Concrete implementation)

	-- Operations:

		* insertWithPriority(data, priority) // sometimes we do not specify the priority
			
			this method will insert new item into the priority queue. We have to specify the data we want to insert and the priority associated with the given data
		
		* getHighestPriorityElement()

			Returns the element with highest priority: we have to reconstruct the heap 
			Max heap: returns maximum element
			Min heap: returns minimum element

		peek()

			Returns the element with highest priority: the structure of the heap does not change.

	-- Sorting:

		- The concept of priority queues naturally suggest a sorting algorithm
		- Insert all the elements to be sorted into a priority queue
		- Sequentially remove them: it will be the sorted order.
		- Why is it working ?
			- We have been discussing that priority queues rely heavily on priorities
			- We take out itemms --> the one with highest priority will be returned
			- Result sequency of decreasing priorities
			- This is the sorted order
			- For example: tree sort, heapsort


"""


"""
* Heap in data structure
	
	- It is baiscally a binary tree
	- Two main binary heap types: min and max heap
	- In a max heap, the keys of parent nodes are always greater than or equal to those of the children --> the highest key is in the root node
	- In a min heap, the keys of parent nodes are less than or equal to those of the children --> the lowest key is in the root node
	- It is complete: it cannot be unbalanced, We insert every new item to the next available place
	- Applications: Dijstra's algorithm, Prims algorithm
	- The heap is one maximally efficient implementation of a priority queue abstract data type
	- It has nothing to do with the pool of memory from which dynamically allocated memory is allocated

--- Heap properties:
	1.) Complete --> we construct the heap from left to right across each
		row // of course the last row may not be completely full
				There is no mising node from left to right in a layer

	2.) In a binary heap every node can have 2 children, left child and right child

	3.) Min heap --> the parent is always smaller than the values of the children

		Max heap --> the parent is always greater

		So: the root node will be the smallest/greatest value in the heap 
				// O(1) access

"""



"""
* Hashtable in data structure

	Arrays are just like that: if we know the index, the insert / retrieve operations can be done in O(1) time

	So arrays are going to solve our problem: the operations running time can be reduced to O(1)

	PROBLEM: we must transform the keys into array indexes, 
		// this is why hashfunctions came to be

	- Balanced BST --> we can achieve O(logN) time complexity for several operations including search
	- Can we do better ?
	- Yes, maybe we can reach O(1)
		This is why hashtables came to be

	- Array: if we know the index, the insertion and retrieval operations are very fast O(1).. that is what we are after

	Here wa want to search for a given item with a given key We have key-value pairs

		KEY ----------------> slot in set of buckets

	index = h(key) where h() is the hashfunction, it maps keys to indexes in the array.

In general: we have n items to be stored + m buckets in which we can store items
Problem: keys are not always nonnegative integers. We have to do prehashing in order to map string keys to indexes of an array.


How can we map a certain key to a slot in our array ? h(x) hashfunction is needed
	Hashing: we can map a certain key of any type(!!!) to a random array index.

	- if we have integer keys we just have to use the modulo operator to transform the number into the range [0,m-1] ~ quite easy

	- if the keys are strings: we can have the ASCII values of the character and make some transformation in order to end up with an index to the array


Hash function:

- Distribute the keys uniformly into buckets
- n: number of keys
- m: number of buckets // size of array
- h(x) = n % m (modulo operator)
	
	-- We should use prime numbers both for the size of the array and in our hash function to make sure the distribution of the generated indexes will be uniform.
	-- String keys: we could calculate the ASCII value for each character, add them up --> make % modulo

"""



"""
* Hashtable collision

	- Collision resolution with chaining: we put multiple entries into the same slot with the help of a linked list
		- If there are many collisions: O(1) complexity gets worse
		- It has an additional memory cost due to the references
	- Collision resolution with open addressing: better solution
	- If collision occurs, we find an empty slot instead
		- Linear probing: if a collision occures, we try the next slot ...if there is a collision too we keep trying the next slot until we find an empty slot
		- Quadratic probing: we trying slots 1,2,4,8...units far away
		- Rehashing: we hash the result again in order to find an empty slot



			   Average case         Worst case
Space                       O(n)               	   O(n)
Search                      O(1)               	   O(n)
Insert                      O(1)               	   O(n)
Delete                      O(1)               	   O(n)

"""


"""
* Hashtable dynamic resizing

	--Load factor: number of entries divided by the number of slots / buckets

	n/m this is the load factor. It is 0 if the hashtable is empty, it is 1 if the hashtable is full.

		- if the load factor is approximately 1 --> it means it is nearly full: the performance will decrease, the operations will be slow
		- if the load factor is approximately 0 --> it means it is nearly empty: there will be a lot of memory wasted

			SO: dynamic resizing is needed something.

	--Dynamic resizing:
		- Performance depends on the load factor: what is the number of entries and number of buckets ratio
		- Space-time tradeoff is important: the solution is to resize table, when its load factor exceeds given threshold
		- Java: when the load factor is greater than 0.75, the hashmap will be resized automatically
		- Python: the threashold is 2/3 ~ 0.66

			1.) hash values depend on table's size so hashes of entries are changed when resizing and algorithm can't just copy data from old storage to new one
			2.) resizing takes O(n) time to complete, where n is a number of entries in the table This fact may make dynamic-sized hash tables inappropriate for real-time applications


	-- Applications:

		- Databases: sometimes search trees, sometimes hashing is better
		- Counting given word occurence in a particular document
		- Storing data + lookup tables (password checks...)
		- Lookup tables in huge networks (lookup for IP addresses)
		- The hashing technique can be used for substring search
			(Rabin-karp algorithm)
"""


"""
* Hashfunction linear probing python
	
	key:apple
		-- > we can define the hashfunction: what is important that it should return
			an integer (the index of the arrayslot)
		-- > we can have the ASCII values for the characters
		-- > sum them up + use modulo operator to transform the final index into a valid range

		(a/p/p/l/e 97/112/112/108/101)
		97 + 112 + 112 + 108 + 101 = 530

		// we have to normalize it with the size of the underlying array

"""

class HashTable(object):

	def __init__(self):
		self.size = 10
		self.keys = [None] * self.size
		self.values = [None] * self.size

	# Linear probing insert implementation in python

	def put(self, key, data):

		index = self.hashfunction(key)

		while self.keys[index] is not None:
			if self.keys[index] == key:
				self.values[index] = data #update
				return

			# rehash try to find another slot
			index = (index+1)%self.size

		# insert
		self.keys[index] = key
		self.values[index] = data


	def get(self, key):

		index = self.hashfunction(key)

		while self.keys[index] is not None:
			if self.keys[index] == key:
				return self.values[index]

			index = (index+1) %self.size
		# it means the key is not present in the associative array
		return None


	def hashfunction(self, key):
		sum = 0
		for pos in range(len(key)):
			sum = sum + ord(key[pos])

		return sum%self.size

# Linear probing retrieve implementation in python
if __name__ == "__main__":

	table = HashTable()

	table.put("apple", 10)
	table.put("car", 20)
	table.put("tomatoe", 30)
	table.put("table", 40)

	print(table.get("table"))





# Dictionary in python
dict = {'Joe':14, 'Patbi':25, 'Emily':23}

#print(dict['Joe']) #O(1)

dict['Joe'] = 18

# print (dict['Joe'])

# dict.clear()
# del dict

#print( dict.items() )
#print( dict.keys() )

print( dict.items() )



"""
* Tries-ternary search tree in data structure

	- With the help of tries we can search and sort strings very very efficiently
	- The problem is that tries consume a lot of memory, so we should use ternary search trees instead which stores less references and null objects
	- TST stores characters or strings in nodes 
	- Each node has 3 children: less (left child), equal (middle child) or greater (right child)
	- Can we balance TST-s with rotations? Yes, but it does not worth the trouble
	- It can be used instead of hashmap: it is as efficient as hashing
	- Hashing need to examine the entire string key ...TST does not

In general we have as many pointers / edges from every node as the number of characters in the alphabet

We have to define an alphabet in advance + ALPHABET_SIZE
	For example: in english alphabet there are 26 characters, so ALPHABET_SIZE = 26--> 26 pointers from every node


	- TST supports sort operation
	- So: TST is better than hashing --> especially for search misses + flexible than BST (usually there is no perfect hash function)

	--- Conclusion: TST is faster than hashmap and more flexible than binary search trees

"""



"""
* Insertion in tries in data structure-python

	- PUT: with this operation we would like to insert a new element into the ternary search tree with a given key
		
		-- if the character is smaller alphabetically: we go to the left
		-- if the character is equal: we go to the middle child
		-- if the character is greater alphabetically: go to the right
"""


"""
* Searching in tries in data structure-python
	
	get: with this operation we would like to get an item from the ternary search tree with a given key

	IMPORTANT:
		- hashmap: we generate an index from the key with the hashfunction.
			We use every single character of the key

		- TST: we may come to the conclusion that there is no value with a given key 
			without considering every character 
			For example: we may return after the second character

		Conclusion: for mismatch --> TST is faster !!!
				For exemple: in LZW data compression there are several mismatches

"""



"""
* Application in tries in data structure

	- We should combine tries with TST
	- At the root: it is a trie with many many children
	- At lower levels it becomes a TST with 3 children only
	- This combination is quite efficient

-- TST vs hashing
	
	-- Hashing

		- Need to examine the entire key (because that is the way the hash function works)
		- Search hits and misses cost the same
		- The running time and performance relies heavily on the hashfunction
		- Does not support as many operations as TST (sorting)	

	-- TST

		- Works only for strings
		- Only examines just enough key characters
		- Search miss may only involve a few character
		- Support more operations ( sorting )
		- Faster than hashing ( for misses especially ) and more flexible than BST

	-- How do hashfunctions work?
		this is the key

		We have to transform the key into an array index ~ we can use ASCII values for the characters: sum them up + use % modulo operator to avoid index out of bound error !!!

	We Have To Examine Every character In The Key !!!

	-- Applications:

		- It can be used to implement the auto-complete feature very very efficiently
		- Can be used for spell-checkers
		- Near-neighbor searching ( of which a spell-check is a special case)
		- For databases especially when indexing by several non-key fields is desirable
		- Very important in package routing on WWW --> the router direct the packages in the direction of the longest prfix. It can be found very quickly with the hepl of TST-s
		- Prefix matching ~ google search
			- we can use DFS instead as well
"""


"""
* Implementation of tries in python
"""


"""
* Red black tree rotations-1 in data structure
"""


"""
* Red black tree rotations-2 in data structure
"""


"""
* Red black tree rotations-3 in data structure
"""



"""
* Red black tree rotations-4 in data structure
"""




"""
* Red black tree example in data structure
"""


"""
* Red black tree example-2 in data structure
"""


"""
* Red black tree vs AVL in data structure
"""



"""
* Graph in data structure
"""



"""
* Breadth first search in data structure
"""




"""
* Breadth first search implementation in python
"""



"""
* Depth first search in data structure
"""



"""
* Depth first search implementation in python
"""



"""
* BFS vs DFS in data structure
"""


"""
* Dijkstra algorithms in data structure
"""


"""
* Dijkstra algorithms logic in data structure
"""


"""
* Dijkstra algorithms real time example
"""


"""
* Dijkstra algorithms in python-1
"""


"""
* Dijkstra algorithms in python-2
"""


"""
* Dijkstra algorithms in python-3
"""


"""
* Bellman ford algorithms in data structure
"""



"""
* Bellman ford algorithms in python-1
"""




"""
* Bellman ford algorithms in python-2
"""


"""
* Bellman ford algorithms in python-3
"""


"""
* Shortest path algorithms
"""



"""
* Union find data structure
"""



"""
* Spanning tree in data structure
"""



"""
* Kruskal algorithms in python-1
"""



"""
* Kruskal algorithms in python-2
"""



"""
* Kruskal algorithms in python-3
"""



"""
* Kruskal algorithms in python-4
"""



"""
* Prims algorithms in python-2
"""



"""
* Prims algorithms in python-3
"""



"""
* Application of spanning tree
"""



"""
* Sorting algorithms in data structure
"""




"""
* Adaptive sorting algorithms
"""




"""
* Bubble sort in data structure
"""



"""
* Bubble sort in python
"""



"""
* Selection sort in data structure
"""



"""
* Selection sort in python
"""



"""
* Quicksort introduction-I
"""



"""
* Insertion sort in python
"""




"""
* Insertion sort in data structure
"""



"""
* Quicksort introduction-II
"""



"""
* Quicksort in python
"""




"""
* Merge sort importance in data structure
"""



"""
* Merge sort in data structure
"""




"""
* Merge sort in python
"""



"""
* Hybrid sorting algorithms
"""



"""
* Non comparison sorting
"""




"""
* Counting sort in data structure
"""


"""
* Radix sort in data structure
"""


"""
* Associated array in python
	
	- Associative arrays / maps / dictionaries are abstract data types !!!
	- Composed of a collection of key-value pairs where each key appears only once in the collection
	- Most of the times we implement associative arrays with hashtables but binary search trees can be used as well
	- The aim is to reach O(1) time complexity for most of the operations

		Supported operations:
			- Adding key-value pairs to the collection
			- Removing key-value pairs from the collection 
			- Update existing key-value pairs
			- Lookup of value associated with a given key
"""