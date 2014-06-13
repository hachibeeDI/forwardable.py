
# Forwardable

pythoniac port forwardable from Ruby


## Installation

```bash
$ pip install https://github.com/hachibeeDI/forwardable/archive/master.zip
```


## Example

### delegator

```python
>>> from forwardable import Forwardable, def_delegator
>>> class Hoge(Forwardable):
...     startswith = def_delegator('aa')
...     endswith = def_delegator('aa')
...     balse = def_delegator('aa', 'replace')  # with proxy
...
...     def __init__(self):
...         self.aa = 'test hoge'

>>> h = Hoge()
>>> h.startswith('test')
True
>>> h.endswith('test')
False
>>> h.balse('test', 'is it greeeeet')
'is it greeeeet hoge'

```

### multi delegators

```python

>>> from forwardable import Forwardable, def_delegators
>>> class Foo(Forwardable):
...     _ = def_delegators('aa', ('startswith', 'endswith', 'replace', ))
...
...     def __init__(self):
...         self.aa = 'test hoge'

>>> f = Foo()
>>> f.startswith('test')
True
>>> f.endswith('test')
False
>>> f.replace('test', 'is it greeeeet')
'is it greeeeet hoge'

```


### use with Metaclass

```python

>>> from forwardable import _Forwardable, def_delegators
>>> class Foo(object):  # if PY3: class Foo(object, metaclass=_Forwardable):
...     __metaclass__ = _Forwardable
...     _ = def_delegators('aa', ('startswith', 'endswith', 'replace', ))
...
...     def __init__(self):
...         self.aa = 'test hoge'

>>> f = Foo()
>>> f.startswith('test')
True
>>> f.endswith('test')
False
>>> f.replace('test', 'is it greeeeet')
'is it greeeeet hoge'

```


## Testing

```bash
python tests.py
```
