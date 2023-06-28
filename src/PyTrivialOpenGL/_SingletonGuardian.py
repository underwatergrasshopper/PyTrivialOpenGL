"""
Provides singleton functionality to class.
"""

class _SingletonGuardian:
    """
    _is_instance_exist : bool
    _target_class_name : str
    """
    def __init__(self, target_class_name):
        """
        target_class_type : str
        """
        self._is_instance_exist     = False
        self._target_class_name     = target_class_name
        
    def count_as_created_instance(self):
        """
        Should be called only inside __init__ method.
        """
        if self._is_instance_exist:
            raise RuntimeError("Can not create more than one instance of singleton class '%s'." % self._target_class_name)
        self._is_instance_exist = True