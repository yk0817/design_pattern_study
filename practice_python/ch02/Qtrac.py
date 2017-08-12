import abc
import collections
import errno
import functools
import os
import sys

def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        generator = function(*args,**kwargs)
        next(generator)
        return generator
    return wrapper

if sys.version_info[:2] < (3,3):
    def remove_if_exists(filename):
        try:
            os.remove(filename)
        except OSError as err:
            if err.errno != errno.ENOENT:
                raise
else:
    def remove_if_exists(filename):
        pass

if sys.version_info[:2] >= (3,3):
    def has_methods(*methods):
        def decorator(Base):
            def __subclasshook__(Class,Subclass):
                if Class is Base:
                    attributes = collections.ChainMap(*(Superclass.__dict__
                                                         for Superclass in absSubclass.__mro__))
                    if all(method in attributes for method in methods):
                        return True
                return NotImplemented
            Base.__subclasshook__ = classmethod(__subclasshook__)
            return Base
        return decorator
else:
    def has_methods(*methods):
        def decorator(Base):
            def __subclasshook__(Class, Subclass):
                if Class is Base:
                    needed = set(methods)
                    for Superclass in Subclass.__mro__:
                        for meth in needed.copy():
                            if meth in Superclass.__dict__:
                                needed.discard(meth)
                        if not needed:
                            return True
                return NotImplemented
            Base.__subclasshook__ = classmethod(__subclasshook__)
            return Base
        return decorator

class Require(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(Class,Subclass):
        methods = set()
        for Superclass in Subclass.__mro__:
            if hasattr(Superclass,"required_methods"):
                methods |= set(Superclass.required_methods)
        attributes = collections.ChainMap(*(Superclass.__dict__
                                            for Superclass in Class.__mro__))
        if all(method in attributes for method in methods):
            return True
        return NotImplemented

def report(message="",error=False):
    if len(message) >= 70 and not error:
        message = message[:67] + "..."
    sys.stdout.write("\r{:70}{}".format(message, "\n" if error else ""))
    sys.stdout.flush()
