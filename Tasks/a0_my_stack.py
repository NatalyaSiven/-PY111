"""
My little Stack
"""
from typing import Any

my_stack1 = []

def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global my_stack1
	my_stack1.append(elem)
	print(elem)
	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global my_stack1
	if my_stack1:
		return my_stack1.pop()
	else:
		return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global my_stack1
	print(ind)
	if ind >= 0:
		return my_stack1[-ind-1]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global my_stack1
	my_stack1 = []
	return None

# if __name__ == "__main__":
# 	push(3)
# 	push(15)
# 	push(3)
# 	push(-5)
# 	push(3)
# 	push(150)
# 	pop()
# 	push(30)
# 	peek(3)
# 	clear()
# 	print(my_stack1)