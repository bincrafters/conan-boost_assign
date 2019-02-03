#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostAssignConan(base.BoostBaseConan):
    name = "boost_assign"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_assign"
    lib_short_names = ["assign"]
    header_only_libs = ["assign"]
    b2_requires = [
        "boost_array",
        "boost_config",
        "boost_core",
        "boost_move",
        "boost_mpl",
        "boost_preprocessor",
        "boost_ptr_container",
        "boost_range",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits"
    ]
