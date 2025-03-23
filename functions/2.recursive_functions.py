"""
Recursive are functions that call themselves either directly or indirectly in order to loop.

This functions allows us to traverse structures that have arbitrary  and upredictable shape and depth e.g:
    planning routes
    analyzing language
    crawling links on the web

Recursive functions can even be used as alternative to simple loops and iterations though they are not always the best choice in terms
of simplisity and performance.

"""

# Example 1: sumation of list. This a simple example of recursive function, loops would be more efficient saving memory and time
            # recursive functions requires fresh local scope for each call and also execution is slower than loopsbecause of multiple function calls
print("Example 1") 
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
   
print(sum_list([1,2,3,4,5]))

# recursion using ternary operator
def sum_list_ternary_operator(l):
    return 0 if not l else l[0] + sum_list_ternary_operator(l[1:])

print(sum_list_ternary_operator([1,2,3,4,5]))


# we can have a type-agnostic summing functions as long as list elements support addition e.g. strings concatenation

def sum_list_type_agnostic1(l):
    if len(l)== 1:
        return l[0]
    return l[0] + sum_list_type_agnostic1(l[1:])

print(sum_list_type_agnostic1(["k","e","l","v","i","n",]))


def sum_list_type_agnostic2(L):
    # print(f"Entry--> {L}")
    first, *rest = L
    print(f"rest--> {rest}")
    return first if not rest else first + sum_list_type_agnostic2(rest) # Use 3.X ext seq assign


print(sum_list_type_agnostic2([1,2,3,4,5]))
print(sum_list_type_agnostic2(["k","e","l","v","i","n","o"]))
print(sum_list_type_agnostic2("kefini"))

# Example 2: factorial
print("Example 2") 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
# However, recusion is best suited for arbitrary and unpredictable data structures.


# Example 3: sum of nested list
print("Example 3") 
lst = [1,[2,[3,4],5,6,[7,8]],9] # nested may take any shape and depth, very unpredictable. Loops can't cover all possibilities since they are arbitrary
# loops are not the best choice for this kind of structure because the depth of the list is unpredictable or this is
# ... not a linear list. Recursion is the best choice for this kind of structure

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

print(sumtree(lst))


# Example 4: Looping versus recursion


# Example 5: Recursion verses queues and stacks
# - python performs recursion using stack, each function call is placed on the stack and popped off when the function returns
# - stack is a last-in-first-out (LIFO) data structure
# - We can implement explicit stack or queue to simulate recursion and understand inner workings of recursion

def sumtree_stack(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot