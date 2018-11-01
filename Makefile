pdf: kapzik.pdf

kapzik.pdf: kapzik.tex
	latex kapzik.tex
	pdflatex kapzik.tex

view: kapzik.pdf
	xreader kapzik.pdf

clean:
	rm -f *.aux *.dvi *.log *.out *.pdf *.toc
