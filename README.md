MetaEnum
========

Better constants and enumerations.

Works with Python 2 and 3 :)

![PyPi Version](https://pypip.in/v/MetaEnum/badge.png) ![Downloads](https://pypip.in/d/MetaEnum/badge.png)

Usage
=====
```python
>>> from metaenum import MetaEnum
>>> class FOO(MetaEnum):
...     BAZ = (0, 'bazik')
...     BAR = 1
>>> FOO.BAZ
0
>>> FOO.BAR
1
>>> FOO.BAZ_name
'BAZ'
>>> FOO.BAZ_verbose
'bazik'
>>> FOO.get_verbose(FOO.BAZ)
'bazik'
>>> FOO.get_verbose(FOO.BAR)
None
>>> FOO.as_choices()
[(0, 'bazik'), (1, None)]
>>> FOO.by_name('BAZ')
0
>>> FOO.by_verbose('bazik')
1
```

