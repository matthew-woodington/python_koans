#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based slightly on the lambdas section of AboutBlocks in the Ruby Koans
#

from runner.koan import *


class AboutLambdas(Koan):
    def test_lambdas_can_be_assigned_to_variables_and_called_explicitly(self):
        def add_one(n): return n + 1
        # self.assertEqual(__, add_one(10))
        self.assertEqual(11, add_one(10))  # lambda returns its argument

    # ------------------------------------------------------------------

    def make_order(self, order):
        return lambda qty: str(qty) + " " + order + "s"

    def test_accessing_lambda_via_assignment(self):
        sausages = self.make_order('sausage')
        eggs = self.make_order('egg')

        # self.assertEqual(__, sausages(3))
        # self.assertEqual(__, eggs(2))
        self.assertEqual('3 sausages', sausages(3))
        self.assertEqual('2 eggs', eggs(2))

    def test_accessing_lambda_without_assignment(self):
        self.assertEqual('39823 spams', self.make_order('spam')(39823))
