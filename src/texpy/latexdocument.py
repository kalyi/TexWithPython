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
    def __init__(self, fileName='texpy.tex', partial=False):
        self.__filename = fileName
        self.__documentclass = 'article'
        self.__documentOptions = []
        self.__packages = []
        self.__packageOptions = {}
        self.__tikzlibs = []
        self.__preview = False
        self.__partial = partial
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
        self.__documentOptions.append(option)

    def isPartial(self):
        return self.__partial

    def setPartial(self, partial):
        self.__partial = partial

    def usesPackage(self, package):
        return package in self.__packages

    def hasPackageOption(self, package, option):
        return (self.usesPackage(package)
                and option in self.__packageOptions[package])

    def addPackage(self, package, options=[]):
        if not self.usesPackage(package):
            self.__packages.append(package)
            self.__packageOptions[package] = []
        for opt in options:
            if opt not in self.__packageOptions[package]:
                self.__packageOptions[package].append(opt)

    def usesTikzLibrary(self, tikzlib):
        return self.usesPackage('tikz') and tikzlib in self.__tikzlibs

    def addTikzLibrary(self, tikzlib):
        if tikzlib not in self.__tikzlibs:
            self.__tikzlibs.append(tikzlib)
        self.addPackage('tikz')

    def addContent(self, content):
        self.__content.append(content)

    def write(self, data):
        self.addContent(data)

    def flush(self):
        pass

    def beginTabular(self, formatString):
        self.addContent('\\begin{tabular}{%s}\n' % formatString)

    def endTabular(self):
        self.addContent('\\end{tabular}\n')

    def beginTikzPicture(self, options=''):
        self.addContent('\\begin{tikzpicture}[%s]\n' % options)

    def endTikzPicture(self):
        self.addContent('\\end{tikzpicture}\n')

    def _writeDocumentHeader(self, doc):
        doc.write('\\documentclass[%s]{%s}\n' % (
            ','.join(self.__documentOptions),
            self.__documentclass))
        for package in self.__packages:
            doc.write('\\usepackage[%s]{%s}\n' % (
                ','.join(self.__packageOptions[package]), package))
        if len(self.__tikzlibs) > 0:
            doc.write('\\usetikzlibrary{%s}\n' %
                      ','.join(t for t in self.__tikzlibs))
        doc.write('\\begin{document}\n')
        if self.__preview:
            doc.write('\\begin{preview}\n')

    def _writeRequiredPackages(self, doc):
        if len(self.__packages) > 0:
            doc.write('%' * 60 + '\n')
            doc.write('% Please make sure to use the following packages:\n')
            for package in self.__packages:
                options = self.__packageOptions[package]
                if len(options) > 0:
                    doc.write('%% %s with options %s\n' % (
                        package, ','.join(options)))
                else:
                    doc.write('%% %s\n' % package)
            if len(self.__tikzlibs) > 0:
                doc.write('%\n% and the following tikz libraries:\n')
                doc.write('% ' + ','.join(t for t in self.__tikzlibs) + '\n')
            doc.write('%' * 60 + '\n\n')

    def _writeDocumentFooter(self, doc):
        if self.__preview:
            doc.write('\\end{preview}\n')
        doc.write('\\end{document}\n')

    def writeDocument(self):
        with open(self.__filename, 'w') as doc:
            if not self.__partial:
                self._writeDocumentHeader(doc)
            else:
                self._writeRequiredPackages(doc)
            for c in self.__content:
                doc.write(c)
            if not self.__partial:
                self._writeDocumentFooter(doc)
