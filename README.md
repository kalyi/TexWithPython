# TexWithPython
Write LaTeX code with Python.

## How to use
```
$ python3
>>> import texpy
>>> doc = texpy.LatexDocument('mydocument.tex')
>>> doc.enablePreview()
>>> texpy.makeTabular([['1','2','3'], ['4','5','6']], out=doc)
>>> doc.writeDocument()
>>> quit()

$ cat mydocument.tex
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
