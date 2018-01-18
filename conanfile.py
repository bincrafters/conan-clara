#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class ClaraConan(ConanFile):
    name = "clara"
    version = "1.1.0"
    description = "A simple to use, composable, command line parser for C++ 11 and beyond"
    homepage = "https://github.com/catchorg/Clara"
    url = "https://github.com/bincrafters/conan-libname"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "https://raw.githubusercontent.com/catchorg/Clara/master/LICENSE"
    exports_sources = ["LICENSE.md"]
    no_copy_source = True
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/catchorg/Clara"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        os.rename("Clara-%s" % self.version, self.source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="license", src=self.source_subfolder)
        self.copy(pattern="*.hpp", dst="include", src=os.path.join(self.source_subfolder, "single_include"))

    def package_id(self):
        self.info.header_only()
