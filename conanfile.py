#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class ClaraConan(ConanFile):
    name = "clara"
    version = "1.1.4"
    description = "A simple to use, composable, command line parser for C++ 11 and beyond"
    url = "https://github.com/bincrafters/conan-clara"
    homepage = "https://github.com/catchorg/Clara"
    license = "BSL-1.0"
    source_subfolder = "source_subfolder"
    exports = ["LICENSE.md"]
    no_copy_source = True

    def source(self):
        source_url = "https://github.com/catchorg/Clara"
        tools.get("{0}/archive/v{1}.zip".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir.capitalize(), self.source_subfolder)

    def package(self):
        include_folder_src = os.path.join(self.source_subfolder, "single_include")
        self.copy(pattern="LICENSE.txt", dst="license", src=self.source_subfolder)
        self.copy(pattern="*.hpp", dst="include", src=include_folder_src)

    def package_id(self):
        self.info.header_only()
