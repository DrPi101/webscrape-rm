Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
['Autocourse', '1962', 'Autocourse', '1967', 'Autocourse', '1968']
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Traceback (most recent call last):
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 10, in <module>
    print(kwr())
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 4, in kwr
    data = f.readlines().split()
AttributeError: 'list' object has no attribute 'split'
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Traceback (most recent call last):
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 10, in <module>
    print(kwr())
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 4, in kwr
    data = fn.split()
AttributeError: '_io.TextIOWrapper' object has no attribute 'split'
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
<_io.TextIOWrapper name='ebay_search.txt' mode='r+' encoding='UTF-8'>
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Traceback (most recent call last):
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 10, in <module>
    print(kwr())
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 4, in kwr
    data = fn()
TypeError: '_io.TextIOWrapper' object is not callable
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Traceback (most recent call last):
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 10, in <module>
    print(kwr())
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 6, in kwr
    return (data)
NameError: name 'data' is not defined
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962

>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962

Autocourse 1967

Autocourse 1968

Traceback (most recent call last):
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 10, in <module>
    print(kwr())
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 7, in kwr
    f.close()
NameError: name 'f' is not defined
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962

Autocourse 1967

Autocourse 1968

Traceback (most recent call last):
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 7, in <module>
    f.close()
NameError: name 'f' is not defined
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962

Autocourse 1967

Autocourse 1968

>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962 200

Autocourse 1967 222

Autocourse 1968 225

>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962 200

Autocourse 1967 222

Autocourse 1968 225

>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
['Autocourse 1962 200\n']
['Autocourse 1967 222\n']
['Autocourse 1968 225\n']
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
['Autocourse 1962 200\n']
['Autocourse 1967 222\n']
['Autocourse 1968 225\n']
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
['Autocourse', '1962']
['Autocourse', '1967']
['Autocourse', '1968']
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
['Autocourse', '1962']
['Autocourse', '1967']
['Autocourse', '1968']
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Traceback (most recent call last):
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 7, in <module>
    st = st.join(",")
AttributeError: 'list' object has no attribute 'join'
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Traceback (most recent call last):
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 7, in <module>
    st = st.join()
AttributeError: 'list' object has no attribute 'join'
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
['Autocourse', '1962']
['Autocourse', '1967']
['Autocourse', '1968']
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse,1962
Autocourse,1967
Autocourse,1968
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse1962
Autocourse1967
Autocourse1968
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962
Autocourse 1967
Autocourse 1968
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Traceback (most recent call last):
  File "/home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py", line 9, in <module>
    print[ls]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
['A', 'u', 't', 'o', 'c', 'o', 'u', 'r', 's', 'e', ' ', '1', '9', '6', '2']
['A', 'u', 't', 'o', 'c', 'o', 'u', 'r', 's', 'e', ' ', '1', '9', '6', '7']
['A', 'u', 't', 'o', 'c', 'o', 'u', 'r', 's', 'e', ' ', '1', '9', '6', '8']
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962
Autocourse 1967
Autocourse 1968
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962
Autocourse 1967
Autocourse 1968
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962 Autocourse 1962
Autocourse 1967 Autocourse 1967
Autocourse 1968 Autocourse 1968
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1968 Autocourse 1968
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962
Autocourse 1967
Autocourse 1968
>>> 
====== RESTART: /home/drpi/Python/WebScrapeRM/webscrape-rm/bin/test1.py ======
Autocourse 1962
Autocourse 1967
Autocourse 1968
>>> 
