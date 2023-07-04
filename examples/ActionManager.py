from time import time as _time

__all__ = [
    "ActionManager"
]

class _Action:
    """
    delay : float
        Delay in seconds.
    do_once : Callable[[], NoneType]
    """
    def __init__(self, delay, do_once):
        self.delay      = delay
        self.do_once    = do_once

class ActionManager:
    """
    _action_chain : List[_Action]
    _begin : float
        Time in seconds.
    _end : float
        Time in seconds.
    """
    def __init__(self):
        self._action_chain  = []
        self._begin         = 0.0
        self._end           = 0.0

    def add(self, delay, do_once):
        """
        delay : float
            Minimal delay in seconds between actions. Only one action can be executed per update.
        do_once : Callable[[], NoneType]
        """
        self._action_chain.append(_Action(delay, do_once))

    def reset(self):
        self._begin = _time()
        self._end = self._begin

    def update(self):
        """
        If there is at least one action, executes latest added, and removes it from chain.
        """
        self._end = _time()

        if len(self._action_chain) > 0:
            action = self._action_chain[0]
            action.delay -= (self._end - self._begin)
            if action.delay <= 0.0:
                action.do_once()
                self._action_chain.pop(0)

        self._begin = self._end