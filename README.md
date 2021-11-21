HackerRank Data Analytics Solutions
=================

[Challenges](https://www.hackerrank.com/contests/python-wbootcamp/challenges) of Data Analytics with Python by WoMakersCode 🦋

### ✏️ Todolist Challenges to Solve

<details><summary><b>❌ The Minion Game</b></summary>
Kevin and Stuart want to play the <b>'The Minion Game'</b>.

<b>Game Rules</b>

Both players are given the same string, <b>S</b>.
Both players have to make substrings using the letters of the string <b>S</b>.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

<b>Scoring</b>

A player gets `+1` point for each occurrence of the substring in the string <b>S</b>.

<b>For Example:</b>

String <b>S</b> = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

![](https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png)

Your task is to determine the winner of the game and their score.

<b>Function Description</b>

Complete the minion_game in the editor below.

minion_game has the following parameters:

- string string: the string to analyze

<b>Prints</b>

- string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

<b>Sample Input</b>

```python
BANANA
```

<b>Sample Output</b>

```python
Stuart 12
```

<b>Note:</b>
Vowels are only defined as `AEIOU`. In this problem, `Y` is not considered a vowel.
</details>

<details><summary><b>❌ Time Delta</b></summary>
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

```python
Day dd Mon yyyy hh:mm:ss +xxxx
```

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

<b>Explanation 0</b>

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is <b>7 x 3600</b> seconds or <b>25200</b> seconds.

Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or <b>24 x 3600 + 30 x 60 -> 88200</b>
</details>

<details><summary><b>❌ Find Angle MBC</b></summary>
![](https://s3.amazonaws.com/hr-challenge-images/9668/1440151155-10b2b748ee-rsz_1438840048-2cf71ed69d-findangle.png)

<b>ABC</b> is a right triangle, <b>90°</b> at <b>B</b>.

Therefore, <b>/ABC = 90°</b>.

Point <b>M</b> is the midpoint of hypotenuse <b>AC</b>.

You are given the lengths <b>AB</b> and <b>BC</b>.

Your task is to find <b>/MBC</b> (angle <b>0°</b>, as shown in the figure) in degrees.

<b>Examples:</b>


If angle is 56.5000001°, then output <b>57°</b>.

If angle is 56.5000000°, then output <b>57°</b>.

If angle is 56.4999999°, then output <b>56°</b>.

<b>0° < 0° < 90°</b>

<b>Sample Input</b>

```python
10
10
```

<b>Sample Output</b>

```python
45°
```
</details>

<details><summary><b>❌ Merge the Tools!</b></summary>
Consider the following:

- A string, <b>s</b>, of length <b>n</b> where <b>s = c0c1 ... cn-1</b>.
- An integer, <b>k</b>, where <b>k</b> is a factor of <b>n</b>.

We can split <b>s</b> into <b>n/k</b> substrings where each subtring, <b>Ti</b>, consists of a contiguous block of <b>k</b> characters in <b>s</b>. 

Then, use each <b>Ti</b> to create string <b>Ui</b> such that:

- The characters in  are a subsequence of the characters in <b>Ti</b>.
- Any repeat occurrence of a character is removed from the string such that each character in <b>Ui</b> occurs exactly once. In other words, if the character at some index <b>j</b> in <b>Ti</b> occurs at a previous index <b>< j</b> in <b>Ti</b>, then do not include the character in string <b>Ui</b>.

Given <b>s</b> and <b>k</b>, print <b>n/k</b> lines where each line <b>i</b> denotes string <b>Ui</b>.

<b>Example</b>

```python
s = 'AAABCDDE'
k = 3
```

There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so . The second substring has all distinct characters, so . The third substring has  different characters, so . Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

<b>Function Description</b>

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

- string s: the string to analyze
- int k: the size of substrings to analyze

<b>Prints</b>

Print each subsequence on a new line. There will be <b>n/k</b> of them. No return value is expected.

<b>Sample Input</b>

```python
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
```

<b>Sample Output</b>

```python
AB
CA
AD
```

<b>Explanation</b>

Split <b>s</b> into <b>n/k = 9/3 = 3</b> equal parts of length <b>k = 3</b>. Convert each <b>Ti</b> to <b>Ui</b> by removing any subsequent occurrences of non-distinct characters in <b>Ti</b>:

1. t0 = <b>"AAB"</b> -> u0 = <b>"AB"</b>
2. t1 = <b>"CAA"</b> -> u1 = <b>"CA"</b>
3. t2 = <b>"ADA"</b> -> u2 = <b>"AD"</b>

Print each  on a new line.
</details>

<details><summary><b>❌ Athlete Sort</b></summary>
You are given a spreadsheet that contains a list of <b>N</b> athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the <b>K</b>th attribute and print the final resulting table. Follow the example given below for better understanding.

![](https://s3.amazonaws.com/hr-assets/0/1514874268-6fabad07aa-AthleteSort2.png)

Note that <b>N</b> is indexed from <b>0</b> to <b>M - 1</b>, where <b>M</b> is the number of attributes.

<b>Note:</b> If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

<b>Explanation 0</b>

The details are sorted based on the second attribute, since <b>K</b> is zero-indexed.
</details>

<details><summary><b>❌ Default Arguments</b></summary>
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

---

Python supports a useful concept of default argument values. For each keyword argument of a function, we can assign a default value which is going to be used as the value of said argument if the function is called without it. For example, consider the following increment function:

```python
def increment_by(n, increment=1):
    return n + increment
```

The functions works like this:

```python
>>> increment_by(5, 2)
7
>>> increment_by(4)
5
>>>
```

Debug the given `function print_from_stream` using the default value of one of its arguments.

The function has the following signature:

```python
def print_from_stream(n, stream)
```

This function should print the first <b>n</b> values returned by `get_next()` method of `stream` object provided as an argument. Each of these values should be printed in a separate line.

Whenever the function is called without the `stream` argument, it should use an instance of EvenStream class defined in the code stubs below as the value of `stream`.

Your function will be tested on several cases by the locked template code.

<b>Explanation 0</b>

There are <b>3</b> queries in the sample.

In the first query, the function `print_from_stream(2, OddStream())` is exectuted, which leads to printing values <b>1</b> and <b>3</b> in separated lines as the first two non-negative odd numbers.

In the second query, the function `print_from_stream(3)` is exectuted, which leads to printing values <b>2,4</b> and <b>6</b> and  in separated lines as the first three non-negative even numbers.

In the third query, the function `print_from_stream(5, OddStream())` is exectuted, which leads to printing values <b>1,3,5,7</b> and <b>9</b> and  in separated lines as the first five non-negative odd numbers.
</details>

<details><summary><b>❌ Maximize It!</b></summary>
You are given a function <b>f(X) = X²</b>. You are also given <b>K</b> lists. The <b>I th</b> list consists of <b>N i</b> elements.

You have to pick one element from each list so that the value from the equation below is maximized:

`S = (f(X¹) + f(X²) + ... + f(X k)) % M`

<b>X i</b> denotes the element picked from the  list . Find the maximized value  obtained.

<b>%</b> denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

<b>Explanation</b>

Picking <b>5</b> from the <b>1</b>st list, <b>9</b> from the <b>2</b>nd list and <b>10</b> from the <b>3</b>rd list gives the maximum <b>S</b> value equal to <b>(5² + 9² + 10²) % 1000 = 206</b>.
</details>

<details><summary><b>❌ Validating Postal Codes</b></summary>
A valid postal code <b>P</b> have to fullfil both below requirements:

1. <b>P</b> must be a number in the range from <b>100000</b> to <b>999999</b> inclusive.
2. <b>P</b> must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

```python
121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.
```

Your task is to provide two regular expressions `regex_integer_in_range` and `regex_alternating_repetitive_digit_pair`. Where:

`regex_integer_in_range` should match only integers range from <b>100000</b> to <b>999999</b> inclusive

`regex_alternating_repetitive_digit_pair` should find alternating repetitive digits pairs in a given string.

Both these regular expressions will be used by the provided code template to check if the input string <b>P</b> is a valid postal code using the following expression:

```python
(bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
```

<b>Explanation 0</b>

1 1 0000 : (0, 0) and (0, 0) are two alternating digit pairs. Hence, it is an invalid postal code.

<b>Note:</b>

A score of <b>0</b> will be awarded for using 'if' conditions in your code.
You have to pass all the testcases to get a positive score.
</details>

<details><summary><b>❌ Matrix Script</b></summary>
Neo has a complex matrix script. The matrix script is a <b>N</b> X <b>M</b> grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

![matrix-script-decoded](https://s3.amazonaws.com/hr-challenge-images/12524/1442753362-1075bd12d9-Capture.JPG)

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
</details>

<details><summary><b>❌ Triangle Quest 2</b></summary>
You are given a positive integer <b>N</b>.
Your task is to print a palindromic triangle of size <b>N</b>.

For example, a palindromic triangle of size <b>5</b> is:

```python
1
121
12321
1234321
123454321
```

You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

<b>Note:</b>

Using anything related to strings will give a score of <b>0</b>.
Using more than one for-statement will give a score of <b>0</b>.
</details>

<details><summary><b>❌ Decorators 2 - Name Directory</b></summary>
Let's use decorators to build a name directory! You are given some information about <b>N</b> people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:

```python
Mr. Henry Davids
```

For Mary George, the output should be:

```python
Ms. Mary George
```

<b>Sample Input</b>

```python
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
```

<b>Sample Output</b>

```python
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
```

<b>Concept</b>

For sorting a nested list based on some parameter, you can use the itemgetter library. You can read more about it [here](http://stackoverflow.com/questions/409370/sorting-and-grouping-nested-lists-in-python?answertab=votes).
</details>

<details><summary><b>❌ Word Order</b></summary>
You are given <b>n</b> words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

<b>Note:</b> Each input line ends with a <b>"\n"</b> character.

<b>Explanation</b>

There are <b>3</b> distinct words. Here, <b>"bcdef"</b> appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are <b>"bcdef"</b>, <b>"abcdefg"</b> and <b>"bcde"</b> which corresponds to the output.
</details>

<details><summary><b>❌ Regex Substitution</b></summary>
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.

Learn more about [re.sub()](https://docs.python.org/2/library/re.html).

<b>Transformation of Strings</b>

Code

```python
import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
```

Output

```python
1 4 9 16 25 36 49 64 81
```

<b>Replacements in Strings</b>

Code

```python
import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment
```

Output

```python
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>
```

---

<b>Task</b>

You are given a text of <b>N</b> lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

```python
&& → and
|| → or
```

Both && and || should have a space " " on both sides.
</details>

<details><summary><b>❌ Reduce Function</b></summary>
Given a list of rational numbers,find their product.

<b>Concept</b>

The `reduce()` function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say `[1,2,3]` and you have to find its sum.

```python
>>> reduce(lambda x, y : x + y,[1,2,3])
6
```

You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:

```python
>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

>>> from fractions import gcd
>>> reduce(gcd, [2,4,8], 3)
1
```
</details>
