#!/usr/bin/env python

import unittest

from pyspark.sql import SparkSession

from mmtfPyspark.datasets import advancedSearchDataset


class AdvancedSearchDatasetTest(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.master("local[*]") \
            .appName("AdvancedSearchDatasetTest") \
            .getOrCreate()

    def test1(self):
        query = (
            "<orgPdbQuery>"
            "<queryType>org.pdb.query.simple.StoichiometryQuery</queryType>"
            "<stoichiometry>A3B3C3</stoichiometry>"
            "</orgPdbQuery>"
        )

        ds = advancedSearchDataset.get_dataset(query)

        self.assertTrue(ds.filter("structureId = '1A5K'").count() == 1)

    def test2(self):
        query = (
            "<orgPdbQuery>"
            "<queryType>org.pdb.query.simple.TreeEntityQuery</queryType>"
            "<t>1</t>"
            "<n>9606</n>"
            "</orgPdbQuery>"
        )

        ds = advancedSearchDataset.get_dataset(query)

        self.assertTrue(ds.filter("structureChainId = '10GS.A' OR structureChainId = '10GS.B'").count() == 2)

    def tearDown(self):
        self.spark.stop()


if __name__ == '__main__':
    unittest.main()
