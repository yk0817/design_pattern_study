import os
import random
import sys
try:
    import ssl
except ImportError:
    ssl = None

_private = {}
_sessionIDkey = 0

def id():
    return _private[_sessionIDkey]

def reset(size=11):
    try:
        sessionId = os.urandom(size)
    except NotImplementedError:
        sessionId = ""
        while len(sessionId) < size:
            sessionId += str(random.random())[2:]
        sessionId = sessionId[:size].encode("utf-8")
    _private[_sessionIDkey] = sessionId
    return sessionId

reset()


if __name__ == '__main__':
    sessionId = id()
    print(len(sessionId),type(sessionId))
    print(sessionId)