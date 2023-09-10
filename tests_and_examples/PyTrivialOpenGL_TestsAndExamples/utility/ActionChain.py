import time as _time

__all__ = [
    "ActionChain"
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

class ActionChain:
    """
    _action_chain : List[_Action]
    _begin : float
        Time in seconds.
    _end : float
        Time in seconds.
    """
    def __init__(self):
        self._actions       = []
        self._begin         = 0.0
        self._end           = 0.0

    def add(self, delay, do_once):
        """
        delay : float
            Minimal delay in seconds between actions. Only one action can be executed per update.
        do_once : Callable[[], NoneType]
        """
        self._actions.append(_Action(delay, do_once))

    def reset(self):
        self._begin = _time.perf_counter()
        self._end = self._begin

    def try_execute(self):
        """
        If there is at least one action and its delay expired, executes latest added, and removes it from chain.
        """
        self._end = _time.perf_counter()

        if len(self._actions) > 0:
            action = self._actions[0]
            action.delay -= (self._end - self._begin)
            if action.delay <= 0.0:
                action.do_once()
                self._actions.pop(0)

        self._begin = self._end

    def is_empty(self):
        """
        Returns (bool).
        """
        return len(self._actions) == 0