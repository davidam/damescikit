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
from sklearn.datasets import fetch_lfw_people
from sklearn.datasets import fetch_20newsgroups
from sklearn.datasets import fetch_california_housing
from sklearn.datasets import fetch_rcv1

import collections
collections.Callable = collections.abc.Callable


class TddInPythonExample(unittest.TestCase):

    def test_iris(self):
        # https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
        data = load_iris()
        self.assertEqual(len(data), 8)

    def test_newsgroups(self):
        # https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html
        cats = ['alt.atheism', 'sci.space']
        newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)
        a = list(newsgroups_train.target_names)
        res1 = ['alt.atheism', 'sci.space']
        self.assertEqual(len(a),2)
        self.assertEqual(a,res1)        
        # newsgroups_train.filenames.shape
        # newsgroups_train.target.shape
        b = newsgroups_train.target[:10]
        res2 = np.array([0, 1, 1, 1, 0, 1, 1, 0, 0, 0])
        self.assertTrue(np.array_equal(b,res2))

    def test_california(self):
        # https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html
        housing = fetch_california_housing()
        # print(housing.data.shape, housing.target.shape)
        a = housing.feature_names[0:6]
        res1 = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']
        self.assertEqual(a, res1)

    def test_lfw(self):
        # https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people
        lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
        n = len(lfw_people)
        res = 5
        self.assertEqual(n,res)
        name = lfw_people.target_names[0]
        res = "Ariel Sharon"
        self.assertEqual(name,res)
        

