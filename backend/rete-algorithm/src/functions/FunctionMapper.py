#!/usr/bin/env python

"""
    TURTLE
    An expert system shell inspired by CLIPS syntax
    @author Claudio Greco, Daniele Negro, Marco Di Pietro
"""
import importlib
import os

from inspect import getmembers, isclass

from src.exceptions.Exceptions import EvaluateException
from src.functions.Predicates import Predicates
from src.functions.SpecialFunctions import SpecialFunctions


class FunctionMapper(object):
    """
    Class for the representation of a mapper of functions.
    In particular, it loads the modules containing
    the functions available to the user.
    """

    def __init__(self):
        self.__map = {}

    def get_method(self, name):
        predicate = Predicates()
        special_function = SpecialFunctions()

        predicates = {"eq": predicate.equal, "neq": predicate.not_equal, "<": predicate.less_than,
                      "<=": predicate.less_equal, ">": predicate.greater_than, ">=": predicate.greater_equal,
                      "and": predicate.logical_and, "or": predicate.logical_or, "not": predicate.not_equal}

        special_functions = {"printout": special_function.printout, "assert": special_function.assertion,
                             "retract": special_function.retract, "bind": special_function.bind,
                             "test": special_function.test, "strategy": special_function.strategy}

        try:
            if name in special_functions:
                return special_functions[name]
            elif name in predicates:
                return predicates[name]
            else:
                return self.__map[name]
        except KeyError:
            # Raises an exception in the case in which the function is not present.
            raise EvaluateException('Unable to find the function ' + name + '!')

    def load_class(self, name):
        # Saves the list of the names of the functions contained in the specified module.
        keys = name().get_names()

        for key in keys:
            # If the considered function of the module is not already present in the system,
            # then it saves a reference to that function in the dictionary.
            if not key in self.__map:
                self.__map[key] = name().get_method(key)

    def load_file(self, filename):
        # Saves the name and the extension of the file. It assumes that the class
        # to be loaded has the same name of the module (.py or .pyc file).
        mod_name, file_ext = os.path.splitext(os.path.split(filename)[-1])

        py_mod = None

        # If the file has .py extension, then it loads that module.
        if file_ext.lower() == '.py':
            py_mod = importlib.import_module(filename)

        # If the file has .pyc extension, then it loads that module.
        elif file_ext.lower() == '.pyc':
            py_mod = importlib.import_module(filename)

        else:
            raise EvaluateException('Unable to find the file ' + filename + '!')

        # Builds the list of the classes contained in the module.
        classes = [u for (v, u) in getmembers(py_mod, isclass) if v.startswith(mod_name)]

        # Loads the classes contained in the module.
        for c in classes:
            self.load_class(c)

    def load_directory(self, directory):
        # Specifies the directory which contains the modules to be loaded.
        os.chdir(directory)

        # Loads the .py and .pyc files found in the specified directory.
        for f in os.listdir('.'):
            if f.endswith('.py'):
                self.load_file(f)

            elif f.endswith('.pyc'):
                self.load_file(f)
