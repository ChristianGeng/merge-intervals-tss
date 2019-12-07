#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Interval(object):
    """
    baz = Interval(3.0, 5.0)
    """
    def __init__(self, two_tuple):

        if len(two_tuple) != 2:
            print("invalid data")
            raise Exception
        else:
            self.minTime = two_tuple[0]
            self.maxTime = two_tuple[1]

        if self.minTime > self.maxTime:  # not an actual interval
            raise ValueError(self.minTime, self.maxTime)

    def get_minTime(self):
        """ getter for begin of interval"""
        return self.minTime

    def get_maxTime(self):
        """ getter for end of interval"""
        return self.maxTime

    def set_max(self, value):
        """ set maximum value """
        self.maxTime = value

    def __repr__(self):
        return 'Interval(%r, %r)' % (self.minTime, self.maxTime)

    def duration(self):
        """
        Returns the duration/extent of the interval in seconds.
        """
        return self.maxTime - self.minTime

    def overlaps(self, other):
        """
        Tests whether self overlaps with the given interval. Symmetric.
        How elegant: http://www.rgrjr.com/emacs/overlap.html
        """
        return other.minTime < self.maxTime and self.minTime < other.maxTime


class Empty(Exception):
    '''Error attempting to access an element from an empty container.'''
    pass


class ArrayStack(object):
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__(self):
        '''Create an empty stack.'''
        self._data = []

    def update_top(self, interval):
        """ This is the most important function:
        it updates the 
        """
        max_to_set = interval.get_maxTime()
        self._data[-1].set_max(max_to_set)

    def __len__(self):
        '''Return the number of elements in the stack.'''
        return len(self._data)

    def __str__(self):
        """ print like one a line"""
        data = ''
        for x in reversed(self._data):
            data = '['+str(x.minTime)+'-'+str(x.maxTime)+']\n'
        return data

    def show_as_list(self):
        for x in self._data:
            data = '['+str(x.minTime)+'-'+str(x.maxTime)+']'
            print(data)

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return len(self._data) == 0

    def push(self, interval):
        '''Add interval to the top of the stack.'''
        self._data.append(interval)

        # new item stored at end of list
    def top(self):
        '''Return (but do not remove) the element at the top of the stack.
            Raise Empty exception if the stack is empty.
            '''
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
        # the last item in the list

    def pop(self):
        '''Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
