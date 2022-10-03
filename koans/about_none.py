#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *

class AboutNone(Koan):

    def test_none_is_an_object(self):
        "Unlike NULL in a lot of languages"
        # https://docs.python.org/3/c-api/none.html
        # none is an object that has no values
        # self.assertEqual(__, isinstance(None, object))
        self.assertEqual(True, isinstance(None, object))


    def test_none_is_universal(self):
        "There is only one None"
        # https://www.pythontutorial.net/advanced-python/python-none/#:~:text=The%20None%20is%20a%20singleton,one%20None%20object%20at%20runtime.&text=It's%20a%20good%20practice%20to,compare%20a%20value%20with%20None%20.
        # none is a singleton object of the NoneType class, which means Python creates only one None object at runtime
        # self.assertEqual(____, None is None)
        self.assertEqual(True, None is None)

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the block below.

        Don't worry about what 'try' and 'except' do, we'll talk about this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            ex2 = ex

        # What exception has been caught?
        #
        # Need a recap on how to evaluate __class__ attributes?
        #
        #     https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

        # self.assertEqual(__, ex2.__class__)
        self.assertEqual(AttributeError, ex2.__class__)

        # What message was attached to the exception?
        # (HINT: replace __ with part of the error message.)

        # https://docs.python.org/3/library/exceptions.html
        # self.assertRegex(ex2.args[0], __)
        self.assertRegex(ex2.args[0], 'NoneType' )

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        # self.assertEqual(__, None is not 0)
        # self.assertEqual(__, None is not False)
        self.assertEqual(True, None is not 0)
        self.assertEqual(True, None is not False)