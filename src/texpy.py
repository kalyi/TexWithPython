#!/usr/bin/env python3
# -*- coding: utf8; -*-
#
# Copyright (C) 2016 : Kathrin Hanauer
#
# Facilitate writing LaTeX code with Python.
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

'''Write LaTeX code with Python'''

import sys


def makeTabular(tableData, rowNames=[], colNames=[],
                colFormat='c', colSep='|',
                leftSep='|', rightSep='|',
                rowNameColFormat='l',
                out=sys.stdout, nlAlways=False):
    cols = max(len(colNames), max(len(row) for row in tableData))
    rows = max(len(rowNames), len(tableData))
    withRowNames = len(rowNames) > 0
    amp = '\n&\n' if nlAlways else ' & '
    nl = '\n\\\\\n' if nlAlways else ' \\\\\n'
    hline = '\\hline\n'
    rowNameFormat = rowNameColFormat + colSep

    tabularFormatString = (leftSep
                           + (rowNameFormat if withRowNames else '')
                           + colSep.join(colFormat for _ in range(0, cols))
                           + rightSep)
    out.write('\\begin{tabular}{%s}\n' % tabularFormatString)
    if len(colNames) > 0:
        out.write(hline)
        if withRowNames:
            out.write(amp)
        out.write(amp.join(colNames))
        out.write(amp * (cols - len(colNames) - 1))
        out.write(nl)
        out.write(hline)
    if withRowNames:
        rowNames.extend((rows - len(rowNames)) * ' ')
    for row in range(0, len(tableData)):
        if withRowNames:
            out.write(rowNames[row] + amp)
        out.write(amp.join(item for item in tableData[row]))
        out.write(amp * (cols - len(tableData[row]) - 1))
        out.write(nl)
    if withRowNames:
        out.write(nl.join(rowNames[emptyRow] + amp
                          + (amp * (cols - 1)) for emptyRow in
                          range(len(tableData), rows)))
    else:
        out.write(nl.join(amp * (cols - 1) for _ in
                          range(len(tableData), rows)))
    if rows > len(tableData):
        out.write(nl)
    out.write(hline)
    out.write('\\end{tabular}\n')
    out.flush()
