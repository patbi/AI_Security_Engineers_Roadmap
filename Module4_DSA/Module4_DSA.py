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
* Binary search tree-delete.

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

			   Average case         Worst case
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
class Node(object);
	def __init__(self, data):
		self.data = data;
		self.leftChild = Home;
		self.rightChild = Home;




"""
* AVL tree in data structure python
"""


"""
* Priority queue in data structure
"""


"""
* Heap in data structure
"""


"""
* Associated array in python
"""



"""
* Hashtable in data structure
"""



"""
* Hashtable in data structure
"""


"""
* Hashtable collision
"""


"""
* Hashtable dynamic resizing
"""


"""
* Hashfunction linear probing python
"""



"""
* Linear probing insert implementation in python
"""



"""
* Linear probing retrieve implementation in python
"""


"""
* Dictionary in python
"""


"""
* Tries-ternary search tree in data structure
"""



"""
* Insertion in tries in data structure-python
"""


"""
* Searching in tries in data structure-python
"""



"""
* Application in tries in data structure
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