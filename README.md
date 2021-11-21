HackerRank Data Analytics Solutions
=================

[Challenges](https://www.hackerrank.com/contests/python-wbootcamp/challenges) of Data Analytics with Python by WoMakersCode 🦋

### ✏️ Todolist

<details><summary><b>✔️ Python If-Else</b></summary>

<b>Task</b>

Given an integer, , perform the following conditional actions:

- If <b>n</b> is odd, print <b>Weird</b>
If  is even and in the inclusive range of <b>2</b> to <b>5</b>, print <b>Not Weird</b>

- If <b>n</b> is even and in the inclusive range of <b>6</b> to <b>20</b> to , print <b>Weird</b>

- If <b>n</b> is even and greater than <b>20</b>, print <b>Not Weird</b>

<b>Input Format</b>

A single line containing a positive integer, <b>n</b>.

Solution: [python-if-else](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/python-if-else.py)
</details>

<details><summary><b>✔️ Say "Hello, World!" With Python</b></summary>

Here is a sample line of code that can be executed in Python:

```python
print("Hello, World!")
```
You can just as easily store a string as a variable and then print it to stdout:

```python
my_string = "Hello, World!"
print(my_string)
```

The above code will print Hello, World! on your screen. Try it yourself in the editor below!

<b>Input Format</b>

You do not need to read any input in this challenge.

<b>Output Format</b>

Print ```Hello, World!``` to stdout.

Solution: [hello-world](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/say-hello-world-with-python.py)
</details>

<details><summary><b>✔️ Arithmetic Operators</b></summary>

<b>Task</b>

The provided code stub reads two integers from STDIN, <b>a</b> and <b>b</b>. Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

<b>Example</b> 

Print the following:

```pyhton
8
-2
15
```

<b>Input Format</b>

- The first line contains the first integer, <b>a</b>.
- The second line contains the second integer, <b>b</b>.

Solution: [arithmetic-operators](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/arithmetic-operators.py)
</details>

<details><summary><b>✔️ Python: Division</b></summary>
<b>Task</b>

The provided code stub reads two integers,  <b>a</b> and <b>b</b>, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, <b>a</b> // <b>b</b>. The second line should contain the result of float division,  <b>a</b> / <b>b</b> .

No rounding or formatting is necessary.

<b>Example</b> 

```pyhton
a = 3
b = 5
```

- The result of the integer division <b>3</b> // <b>5</b> = <b>0</b>.
- The result of the float division is <b>3</b> / <b>5</b> = <b>0.6</b>.

<b>Print</b> 

```pyhton
0
0.6
```

Solution: [python-division](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/python-division.py)
</details>

<details><summary><b>✔️ Loops</b></summary>
<b>Task</b>

The provided code stub reads and integer, <b>n</b>, from STDIN. For all non-negative integers <b>i < n</b>, print <b>i²</b>.

<b>Example</b> 

<b>n = 3</b>

The list of non-negative integers that are less than <b>n = 3</b> is <b>[0,1,2]</b>. Print the square of each number on a separate line.

```pyhton
0
1
4
```

Solution: [loops](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/loops.py)
</details>

<details><summary><b>✔️ Print Function</b></summary>
<b>Task</b>

The included code stub will read an integer, <b>n</b>, from STDIN.

Without using any string methods, try to print the following:

<b>123 ... n</b>

Note that "<b>...</b>" represents the consecutive values in between.

<b>Example</b>

<b>n = 5</b>

Print the string <b>12345</b>.

Solution: [print-function](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/print-function.py)
</details>

<details><summary><b>✔️ Find the Runner-Up Score!</b></summary>
<b>Task</b>

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given <b>n</b> scores. Store them in a list and find the score of the runner-up.

<b>Input Format</b>

The first line contains <b>n</b>. The second line contains an array <b>A[]</b> of <b>n</b> integers each separated by a space.

<b>Explanation</b> 

Given list is <b>[2,3,6,6,5]</b>. The maximum score is <b>6</b>, second maximum is <b>5</b>. Hence, we print <b>5</b> as the runner-up score.

Solution: [find-the-runner-up-score](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/find-the-runner-up-score.py)
</details>

<details><summary><b>✔️ Lists</b></summary>
<b>Task</b>

Consider a list (list = []). You can perform the following commands:

1. `insert i e`: Insert integer <b>e</b> at position <b>i</b>.
2. `print`: Print the list.
3. `remove e`: Delete the first occurrence of integer <b>e</b>.
4. `append e`: Insert integer <b>e</b> at the end of the list.
5. `sort`: Sort the list.
6. `pop`: Pop the last element from the list.
7. `reverse`: Reverse the list.

Initialize your list and read in the value of <b>n</b> followed by <b>n</b> lines of commands where each command will be of the <b>7</b> types listed above. Iterate through each command in order and perform the corresponding operation on your list.

<b>Example</b>

```
N = 4
append 1
append 2
insert 3 1
print
```

- <b>append 1</b>: Append <b>1</b> to the list, <b>arr = [1]</b>.
- <b>append 2</b>: Append <b>2</b> to the list, <b>arr = [1,2]</b>.
- <b>insert 3 1</b>: Insert <b>3</b> at index <b>1</b>, <b>arr = [1,3,2]</b>.
- <b>print</b>: Print the array.

Solution: [lists](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/lists.py)
</details>

<details><summary><b>✔️ Tuples</b></summary>
<b>Task</b>

Given an integer, <b>n</b>, and <b>n</b> space-separated integers as input, create a tuple, <b>t</b>, of those <b>n</b> integers. Then compute and print the result of <b>hash(t)</b>.

<b>Note:</b> [hash()](https://docs.python.org/3/library/functions.html) is one of the functions in the <b>__builtins__</b> module, so it need not be imported.

Solution: [tuples](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/tuples.py)
</details>

<details><summary><b>✔️ Set .discard(), .remove() & .pop()</b></summary>
<b>.remove(x)</b>

This operation removes element <b>x</b> from the set.
If element <b>x</b> does not exist, it raises a <b>KeyError</b>.
The .remove(x) operation returns <b>None</b>.

<b>Example</b>

```python
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0
```

---

<b>.discard(x)</b>

This operation removes element <b>x</b> from the set.
If element <b>x</b> does not exist, it <b>does not</b> raise a <b>KeyError</b>.
The .discard(x) operation returns <b>None</b>.

<b>Example</b>

```python
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
```

---

<b>.pop()</b>

This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a <b>KeyError</b>.

<b>Example</b>

```python
>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
```

---

<b>Task</b>

You have a non-empty set <b>s</b>, and you have to execute <b>N</b> commands given in <b>N</b> lines.

The commands will be pop, remove and discard.

Solution: [set-discard-remove-e-pop](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/blob/main/solutions/py-set-discard-remove-pop.py)
</details>

<br>

> [Challenges to solve](https://github.com/leticiacamposs2/hackerrank-data-analytics-solutions/tree/challenges-to-solve)