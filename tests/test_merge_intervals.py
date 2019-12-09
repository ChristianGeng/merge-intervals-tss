#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import unittest
from merge_intervals_tss.merge_intervals import ArrayStack, Interval, merge_intervals

class TestMergeIntervals(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.input_intervals = [[25, 30], [2, 19], [14, 23], [4, 8]]
        self.input_intervals.sort(key=lambda tup: tup[0])
        self.outout_intervals = [[2, 23], [25, 30]]
        
        # print(my_stack)
        # for interval in self.input_intervals:
        #    my_stack.push(interval)

        """
        1. Sort the intervals based on increasing order of starting time.
        2. Push the first interval on to a stack.
        3. For each interval do the following
            a. If the current interval does not overlap with the stack  top, push it.
            b. If the current interval overlaps with stack top and ending time of current 
            interval is more than that of
        stack top, update stack top with the ending  time of current interval.
        4. At the end stack contains the merged intervals.
        """


    def test_your_code(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass
