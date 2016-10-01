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

'''Create a LaTeX table in Python'''


def makeTabular(doc, tableData, rowNames=[], colNames=[],
                colFormat='c', colSep='',
                leftSep='', rightSep='',
                rowNameColFormat='l',
                useBooktabs=True,
                nlAlways=False):
    cols = max(len(colNames), max(len(row) for row in tableData))
    rows = max(len(rowNames), len(tableData))
    withRowNames = len(rowNames) > 0

    amp = '\n&\n' if nlAlways else ' & '
    nl = '\n\\\\\n' if nlAlways else ' \\\\\n'
    rowNameFormat = rowNameColFormat + colSep

    if useBooktabs:
        toprule = '\\toprule\n'
        midrule = '\\midrule\n'
        bottomrule = '\\bottomrule\n'
        doc.addPackage('booktabs')
    else:
        toprule = '\\hline\n'
        midrule = '\\hline\n'
        bottomrule = '\\hline\n'

    tabularFormatString = (leftSep
                           + (rowNameFormat if withRowNames else '')
                           + colSep.join(colFormat for _ in range(0, cols))
                           + rightSep)
    doc.beginTabular(tabularFormatString)
    doc.addContent(toprule)
    if len(colNames) > 0:
        if withRowNames:
            doc.addContent(amp)
        doc.addContent(amp.join(colNames))
        doc.addContent(amp * (cols - len(colNames) - 1))
        doc.addContent(nl)
        doc.addContent(midrule)
    if withRowNames:
        rowNames.extend((rows - len(rowNames)) * ' ')
    for row in range(0, len(tableData)):
        if withRowNames:
            doc.addContent(rowNames[row] + amp)
        doc.addContent(amp.join(item for item in tableData[row]))
        doc.addContent(amp * (cols - len(tableData[row]) - 1))
        doc.addContent(nl)
    if withRowNames:
        doc.addContent(nl.join(rowNames[emptyRow] + amp
                               + (amp * (cols - 1)) for emptyRow in
                               range(len(tableData), rows)))
    else:
        doc.addContent(nl.join(amp * (cols - 1) for _ in
                               range(len(tableData), rows)))
    if rows > len(tableData):
        doc.addContent(nl)
    doc.addContent(bottomrule)
    doc.endTabular()
