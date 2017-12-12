#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class ClaraConan(ConanFile):
    name = "clara"
    version = "1.0.0"
    url = "https://github.com/bincrafters/conan-libname"
    description = "A simple to use, composable, command line parser for C++ 11 and beyond"
    license = "https://raw.githubusercontent.com/catchorg/Clara/master/LICENSE"
    exports_sources = ["LICENSE"]

    def source(self):
        source_url = "https://github.com/catchorg/Clara"
        tools.get("{0}/archive/master.zip".format(source_url))
        os.rename("Clara-master", "sources")

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="sources")
        self.copy(pattern="*.hpp", dst="include", src=os.path.join("sources", "single_include"))

    def package_id(self):
        self.info.header_only()
