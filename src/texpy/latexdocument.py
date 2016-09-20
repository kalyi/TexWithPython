#!/usr/bin/env python3
# -*- coding: utf8; -*-
#
# Copyright (C) 2016 : Kathrin Hanauer
#
# This file is part of texpy (TexWithPython).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

'''A LaTeX document in Python'''


class LatexDocument:
    def __init__(self, fileName='texpy.tex'):
        self.__filename = fileName
        self.__documentclass = 'article'
        self.__documentoptions = []
        self.__packages = []
        self.__tikzlibs = []
        self.__preview = False
        self.__content = []

    def setFileName(self, fileName):
        self.__filename = fileName

    def enablePreview(self, previewOptions=['active',
                                            'tightpage']):
        self.__preview = True
        self.addPackage('preview', previewOptions)

    def setDocumentClass(self, docClass):
        self.__documentclass = docClass

    def addDocumentOption(self, option):
        self.__documentoptions.append(option)

    def addPackage(self, package, options=[]):
        self.__packages.append((package, options))

    def addTikzLibrary(self, tikzlib):
        self.__tikzlibs.append(tikzlib)
        if 'tikz' not in (p[0] for p in self.__packages):
            self.addPackage('tikz')

    def addContent(self, content):
        self.__content.append(content)

    def write(self, data):
        self.addContent(data)

    def flush(self):
        pass

    def writeDocument(self):
        with open(self.__filename, 'w') as doc:
            doc.write('\\documentclass[%s]{%s}\n' % (
                ','.join(self.__documentoptions),
                self.__documentclass))
            for package, options in self.__packages:
                doc.write('\\usepackage[%s]{%s}\n' % (
                    ','.join(options), package))
            if len(self.__tikzlibs) > 0:
                doc.write('\\usetikzlibrary{%s}\n' %
                          ','.join(t for t in self.__tikzlibs))
            doc.write('\\begin{document}\n')
            if self.__preview:
                doc.write('\\begin{preview}\n')
            for c in self.__content:
                doc.write(c)
            if self.__preview:
                doc.write('\\end{preview}\n')
            doc.write('\\end{document}\n')
