# TexWithPython
Write LaTeX code with Python.

## How to use
```
$ python3
>>> import texpy
>>> doc = texpy.LatexDocument('mytable.tex')
>>> doc.enablePreview()
>>> texpy.makeTabular(doc, [['1','2','3'], ['4','5','6']])
>>> doc.writeDocument()
>>> quit()

$ cat mytable.tex
\documentclass[]{article}
\usepackage[active,tightpage]{preview}
\begin{document}
\begin{preview}
\begin{tabular}{|c|c|c|}
1 & 2 & 3 \\
4 & 5 & 6 \\
\hline
\end{tabular}
\end{preview}
\end{document}
```
![The produced PDF.](/doc/mytable.png)

```
$ python3
>>> import texpy
>>> doc = texpy.LatexDocument('myplot.tex')
>>> doc.enablePreview()
>>> texpy.tikzPlot(doc, [[(1, 1), (2, 4), (3, 0), (4.5, 6.1), (5.5, 1)], [(0, 5), (2, -1), (4, 3), (5, 2)]], datasetStyles=['red', 'blue'], datasetLabels=['nonsense data', 'random data'], visualizeAs=['smooth line', 'line'], nlAlways=True)
>>> doc.writeDocument()
>>> quit()

$ cat myplot.tex
\documentclass[]{article}
\usepackage[active,tightpage]{preview}
\usepackage[]{graphicx}
\usepackage[]{xcolor}
\usepackage[]{tikz}
\usetikzlibrary{datavisualization,plotmarks}
\begin{document}
\begin{preview}
\begin{tikzpicture}[]
\datavisualization [%
scientific axes,%
x axis={%
attribute = x,%
label = {x axis},%
},y axis={%
attribute = y,%
label = {y axis},%
},%
visualize as smooth line=d0,%
d0={style={red},label in legend={text=nonsense data}},%
visualize as line=d1,%
d1={style={blue},label in legend={text=random data}},%
]
data [separator=\space,set=d0] {
x y
1 1
2 4
3 0
4.5 6.1
5.5 1
}
data [separator=\space,set=d1] {
x y
0 5
2 -1
4 3
5 2
}
;
\end{tikzpicture}
\end{preview}
\end{document}
```
![The produced PDF.](/doc/myplot.png)
