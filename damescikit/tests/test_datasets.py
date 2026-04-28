#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2026  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damescikit; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unittest
import numpy as np
from sklearn.datasets import load_iris
from sklearn.datasets import fetch_20newsgroups
import collections
collections.Callable = collections.abc.Callable


class TddInPythonExample(unittest.TestCase):

    def test_iris(self):
        data = load_iris()
        self.assertEqual(len(data), 8)

    def test_newsgroups(self):    
        cats = ['alt.atheism', 'sci.space']
        newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)
        a = list(newsgroups_train.target_names)
        res1 = ['alt.atheism', 'sci.space']
        self.assertEqual(len(a),2)
        self.assertEqual(a,res1)        
        # newsgroups_train.filenames.shape
        # newsgroups_train.target.shape
        b = newsgroups_train.target[:10]
        print(type(b))
        res2 = np.array([0, 1, 1, 1, 0, 1, 1, 0, 0, 0])
        print(res2)
        self.assertTrue(np.array_equal(b,res2))
