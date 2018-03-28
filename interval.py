"""
========
Interval

Interval tree implementation in Python.

Interval trees hold intervals in tree structure 
so that overlaps can be observed faster.

"""
import sys
ver = sys.version_info.major 
# If 2 change property logic TODO

class InvalidInterval(Exception):
    pass

class Interval(object):
    """ Interval class for holding interval boundaries """
    def __init__(self, l, r):
        if l > r:
            raise InvalidInterval
        self._l = l
        self._r = r

    @property
    def left(self):
        return self._l

    @property
    def right(self):
        return self._r

    def check_overlap(self, other):
        if self.right > other.left or self.left < other.right:
            return True
        return False

class Node(object):
    """ Node structure holds an interval """
    def __init__(self, interval):
        self._interval = interval
        self._parent = None
        self._left_node = None
        self._right_node = None
        self._maxval = interval.right

    @property
    def interval(self):
        """ Interval getter """
        return self._interval

    @property
    def parent(self):
        """ Parent node getter """
        return self._parent

    @property
    def left_node(self):
        """ Left node getter """
        return self._left_node

    @property
    def right_node(self):
        """ Right node getter """
        return self._right_node

    @property
    def maxval(self):
        """ Max value in subtree getter """
        return self._maxval

    @parent.setter
    def parent(self, value):
        """ Parent node setter """
        self._parent = value

    @left_node.setter
    def left_node(self, value):
        """ Left node setter """
        self._left_node = value
        value.parent = self
        self.maxval = max(self.maxval, value.maxval)
    
    @right_node.setter
    def right_node(self, value):
        """ Right node setter """
        self._right_node = value
        value.parent = self
        self.maxval = max(self.maxval, value.maxval)
    
    @right_node.deleter
    def right_node(self):
        """ Right node deleter """
        self._right_node = None
    
    @left_node.deleter
    def left_node(self):
        """ Left node deleter """
        self._left_node = None

    @maxval.setter
    def maxval(self, value):
        """ Max value in subtree setter """
        self._maxval = value

class IntervalTree(object):
    """
    Generic abstract tree structure.
    """
    
    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        """ Tree root getter """
        return self._root
    
    @root.setter
    def root(self, val):
        """ Tree root setter """
        self._root = val
    
    def add(self, node):
        """ Tree add rule """
        pass
    
    def remove(self, node):
        """ Tree remove rule """
        pass

    def check_overlap(self, node):
        """ Check if node overlaps """
        pass

class IntervalBSTree(IntervalTree):
    """ 
    Interval tree structure that uses simple 
    Binary Search Tree as underlying tree.

    Supports adding, removing and checking overlaps.
    """
    def add(self, node):
        """ 
        BST Tree add rule 
        Add according to left value of interval
        """
        self._add(self.root, node)

    def _add(self, parent, node):
        pl = parent.interval.left
        nl = node.interval.left
        if pl > nl:
            if parent.left_node == None:
                parent.left_node = node
            else:
                self._add(parent.left_node, node)
        else: 
            if parent.right_node == None:
                parent.right_node = node
            else:
                self._add(parent.right_node, node)

    def remove(self, node):
        """ 
        BST Tree remove rule 
        Search according to left value of interval
        """
        self._remove(self.root, node)

    def _remove(self, parent, node):
        pl = parent.interval.left
        nl = node.interval.left
        if parent == node:
            # We have found target node
            gp = parent.parent # get target parent
            while node.right_node != None:
                node = node.right_node # get rightmost node 
            if parent == node: # if they are the same
                if node == gp.left_node:
                    del gp.left_node
                else:
                    del gp.right_node
                return
            parent = node # allocate rightmost
            parent.parent = gp
            return

        if pl > nl:
            if parent.left_node == None:
                return None
            else:
                self._remove(parent.left_node, node)
        else: 
            if parent.right_node == None:
                return None
            else:
                self._remove(parent.right_node, node)

    def check_overlap(self, interval):
        """ 
        Check if node overlaps 
        Steps:
            pass
        """
        if self.root == None:
            return None
        else:
            pass

class IntervalAVLTree(IntervalTree):
    """ 
    Interval tree structure that uses simple 
    AVL Tree as underlying tree.

    Supports adding, removing and checking overlaps.
    """
    def add(self, node):
        """ BST Tree add rule """
        pass
    
    def remove(self, node):
        """ BST Tree remove rule """
        pass

    def check_overlap(self, node):
        """ Check if node overlaps """
        pass

class IntervalRBTree(IntervalTree):
    """ 
    Interval tree structure that uses simple 
    Red Black Tree as underlying tree.

    Supports adding, removing and checking overlaps.
    """
    def add(self, node):
        """ BST Tree add rule """
        pass
    
    def remove(self, node):
        """ BST Tree remove rule """
        pass

    def check_overlap(self, node):
        """ Check if node overlaps """
        pass

bintrees_enabled = False
# if Python 3
if ver == 3:
    import importlib
    bintrees_enabled = importlib.util.find_spec("bintrees") != None
# if Python 2
if ver == 2:
    import imp
    try:
        imp.find_module("bintrees")
        bintrees_enabled = True
    except ImportError:
        bintrees_enabled = False

print(bintrees_enabled)
if bintrees_enabled:
    import bintrees
    class IntervalBSTreeBintreesAdapter:
        NotImplemented

    class IntervalRBTreeBintreesAdapter:
        NotImplemented

    class IntervalAVLTreeBintreesAdapter:
        NotImplemented
