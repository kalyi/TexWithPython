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

'''Create TikZ plots in Python'''

import random


def tikzPlot(doc, datasets,
             visualizeAs=['line'],
             xAttr='x', yAttr='y',
             xLabel='x axis', yLabel='y axis',
             datasetStyles=[],
             datasetLabels=[],
             nlAlways=False):
    requiredPackages = ['graphicx', 'xcolor', 'tikz']
    requiredTikzLibs = ['datavisualization', 'plotmarks']
    for p in requiredPackages:
        doc.addPackage(p)
    for t in requiredTikzLibs:
        doc.addTikzLibrary(t)

    nl = '%\n' if nlAlways else ''
    colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'purple']
    numDatasets = len(datasets)
    dnames = ['d' + str(i) for i in range(0, numDatasets)]
    dvisualize = visualizeAs
    fill = 'line' if len(visualizeAs) == 0 else visualizeAs[0]
    dvisualize += [fill] * (numDatasets - len(visualizeAs))
    dstyles = datasetStyles
    for i in range(len(datasetStyles), numDatasets):
        dstyles.append(random.choice(colors))

    doc.beginTikzPicture()
    doc.addContent('\\datavisualization [')
    doc.addContent(nl)
    doc.addContent('scientific axes,')
    doc.addContent(nl)
    doc.addContent('x axis={')
    doc.addContent(nl)
    doc.addContent('attribute = %s,' % xAttr)
    doc.addContent(nl)
    doc.addContent('label = {%s},' % xLabel)
    doc.addContent(nl)
    doc.addContent('},')
    doc.addContent('y axis={')
    doc.addContent(nl)
    doc.addContent('attribute = %s,' % yAttr)
    doc.addContent(nl)
    doc.addContent('label = {%s},' % yLabel)
    doc.addContent(nl)
    doc.addContent('},')
    for d in range(0, len(datasets)):
        doc.addContent(nl)
        doc.addContent('visualize as %s=%s,' % (dvisualize[d], dnames[d]))
        doc.addContent(nl)
        if d < len(datasetLabels) and datasetLabels[d] is not None:
            doc.addContent('%s={style={%s},label in legend={text=%s}},' % (
                dnames[d], dstyles[d], datasetLabels[d]))
        else:
            doc.addContent('%s={style={%s}},' % (dnames[d], dstyles[d]))
    doc.addContent(nl)
    doc.addContent(']\n')

    for d in range(0, len(datasets)):
        doc.addContent('data [separator=\\space,set=%s] {\n' % dnames[d])
        doc.addContent('%s %s\n' % (xAttr, yAttr))
        for x, y in datasets[d]:
            doc.addContent('%s %s\n' % (x, y))
        doc.addContent('}\n')
    doc.addContent(';\n')
    doc.endTikzPicture()
