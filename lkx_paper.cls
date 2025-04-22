\ProvidesClass{lkx_paper}[2025/04/20 Paper Class]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[11pt,letterpaper]{article}
\RequirePackage{expl3,xparse,xstring}
\ExplSyntaxOn

% Font / Layout
\usepackage[margin=1in, includefoot]{geometry}
\usepackage[T1]{fontenc}
\usepackage{mlmodern}
\usepackage{microtype}
\usepackage[indent]{parskip}

% Page Numbers
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Title
\def\@author{}
\def\@date{}
\RenewDocumentCommand{\title}{m}{\def\@title{\textsc{#1}}}
\AtBeginDocument{\maketitle\thispagestyle{fancy}}

% Colors
\usepackage{xcolor}
\definecolor{lkxemph}{RGB}{11, 88, 169}

% Lists
\usepackage[shortlabels]{enumitem}
\setlist[enumerate]{topsep=1ex,itemsep=1ex,partopsep=1ex,parsep=1ex}
\setlist[itemize]{topsep=1ex,itemsep=1ex,partopsep=1ex,parsep=1ex}

% Consistent bold math
\NewCommandCopy{\oldbfseries}{\bfseries}
\renewcommand{\bfseries}{\oldbfseries\boldmath}

% Bibliography
\usepackage[
	style=numeric,
	natbib=true,
	isbn=false,
	url=false,
	doi=false,
	eprint=false
]{biblatex}
\AtEveryBibitem{
	\clearfield{note}
	\clearfield{month}
}
\DeclareFieldFormat{labelnumber}{\normalfont #1}
\renewcommand*\mkbibbrackets[1]{\normalfont [#1]}

\NewDocumentCommand{
	\lkxbib}{m}{\bibliography{#1}{}
	\AtEndDocument{\renewcommand\bibname{References} 
	\vspace{1em}
	\printbibliography[title=References, heading = subbibliography]}}

% General math
\usepackage{amsmath, amssymb}

% Theorem environments
\usepackage{amsthm}
\usepackage{thmtools}

\declaretheoremstyle[
	headfont=\bfseries,
	bodyfont=\slshape,
	headpunct={.},
	postheadspace=0.5em
]{theoremstyle}

\declaretheorem[style=theoremstyle, name=Theorem]{theorem}
\declaretheorem[style=theoremstyle, name=Proposition]{proposition}
\declaretheorem[style=theoremstyle, name=Lemma]{lemma}
\declaretheorem[style=theoremstyle, name=Corollary]{corollary}

\renewcommand{\qed}{\hfill$\blacksquare$}

% Misc
\newcommand{\defn}[1]{{\itshape\color{lkxemph} #1}}
\newcommand{\todo}[1]{{\bf\color{red}{#1}}}

% cleveref (must be loaded last)
\usepackage{bookmark}
\hypersetup{colorlinks=true,
	linkcolor=lkxemph,
	citecolor=lkxemph,
	filecolor=lkxemph,
	urlcolor=lkxemph}

\usepackage[capitalize,nameinlink,noabbrev]{cleveref}
\renewcommand{\chapterautorefname}{Chapter}
\renewcommand{\sectionautorefname}{Section}
\renewcommand{\subsectionautorefname}{Section}
\crefname{equation}{}{}
\crefformat{equation}{\normalfont{#2(#1)#3}}
