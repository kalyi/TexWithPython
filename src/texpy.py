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


def makeTabular(tableData, out=sys.stdout, rowNames=[], colNames=[],
                colFormat='c', colSep='|',
                leftSep='|', rightSep='|'):
    cols = max(len(colNames), max(len(row) for row in tableData))
    rows = max(len(rowNames), len(tableData))
    withRowNames = len(rowNames) > 0

    tabularFormatString = (leftSep
                           + ('l|' if withRowNames else '')
                           + colSep.join(colFormat for _ in range(0, cols))
                           + rightSep)
    out.write('\\begin{tabular}{%s}\n' % tabularFormatString)
    if len(colNames) > 0:
        out.write('\\hline\n')
        if withRowNames:
            out.write(' & ')
        out.write(' & '.join(colNames))
        out.write(' & ' * (cols - len(colNames)))
        out.write('\\\\\n')
        out.write('\\hline\n')
    if withRowNames:
        rowNames.extend((rows - len(rowNames)) * ' ')
    for row in range(0, len(tableData)):
        if withRowNames:
            out.write(rowNames[row] + ' & ')
        out.write(' & '.join(item for item in tableData[row]))
        out.write(' & ' * (cols - len(tableData[row])))
        out.write(' \\\\\n')
    if withRowNames:
        out.write('\\\\\n'.join(rowNames[emptyRow] + ' & '
                                + (' & ' * (cols - 1)) for emptyRow in
                                range(len(tableData), rows)))
    else:
        out.write('\\\\\n'.join(' & ' * (cols - 1) for _ in
                                range(len(tableData), rows)))
    if rows > len(tableData):
        out.write('\\\\\n')
    out.write('\hline\n\\end{tabular}\n')
    out.flush()
