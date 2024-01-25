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
			self.head = currentNode.nexNode;
		else:
			previousNode.nextNode = currentNode.nextNode;



	#O(1)
	def size(self):
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




"""
- Stack in python
"""