# Ściąga LaTeX — laboratoria 2–7

Zaliczenie: **TeXstudio + MiKTeX**, lokalnie. Silnik zawsze **LuaLaTeX**. Treść piszesz w `chapters/`, danych nie ruszasz w `config/project-style.sty`.

Szukaj w tym pliku przez Ctrl+F. Hasła na górze listy: `LuaLaTeX`, `biber`, `??`, `equation`, `tabular`, `lstinputlisting`, `tikzpicture`, `addplot`, `literatura.bib`, `\cref`, `\qty`.

Mapa folderów (nagłówki PDF 6 i 7 mają zły numer laboratorium; liczy się treść):

| Folder | Temat |
|---|---|
| latexlab-2 | szablon, metadane, kompilacja |
| latexlab-3 | sekcje, listy, pogrubienie, matematyka |
| latexlab-4 | tabele, rysunki, listingi Pythona |
| latexlab-5 | listing C, odwołania, bibliografia, spisy |
| latexlab-6 | schematy TikZ |
| latexlab-7 | wykresy PGFPlots + CSV |

Pakiety **już załadowane** przez `config/project-style.sty`: `amsmath`, `booktabs`, `tabularx`, `siunitx`, `graphicx`, `listings`, `tikz` (+ `positioning`, `arrows.meta`, `shapes.geometric`), `hyperref`, `cleveref`, `biblatex` (Biber, styl numeryczny, sortowanie alfabetyczne), `csquotes`, `babel` (polish).

Dopisujesz sam w `main.tex`, **po** `\usepackage{config/project-style}`:

```latex
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}

\usepackage{multirow}   % tylko gdy scalasz wiersze nagłówka
```

TikZ-a drugi raz nie dodawaj, jeśli styl już go wczytał. `pgfplots` w stylu **nie ma**.

---

## 0. Start w 60 sekund

1. Otwórz `main.tex`. Pierwsza linia: `% !TeX program = lualatex`.
2. TeXstudio: **Opcje → Konfiguruj TeXstudio → Zbuduj → Pokaż opcje zaawansowane → Kompilator domyślny = `txs:///lualatex`**.
3. Tytuł, autor, przedmiot: tylko `config/metadata.tex`. Zostaw `\projectstatus` jako `draft`.
4. Tekst: pliki w `chapters/`. Nowy rozdział = nowy plik zaczynający się od `\chapter{...}` i dopisany `\include{...}` **bez** `.tex`.
5. Kompilacja zwykła: LuaLaTeX. Po cytowaniach albo nowych odwołaniach:

```text
lualatex main.tex
biber main
lualatex main.tex
lualatex main.tex
```

W TeXstudio to kolejno: **LuaLaTeX → Biber → LuaLaTeX → LuaLaTeX**.

`latexmk` jest opcjonalny i na Windowsie chce Perla. PDF z samego LuaLaTeX to `main.pdf` w katalogu projektu. PDF z `latexmk` to `build/main.pdf`.

---

## 1. Gdzie co leży (lab 2)

```text
main.tex                  kolejność rozdziałów, NIC innego
config/metadata.tex       tytuł, autorzy, true/false spisów
config/project-style.sty  nie edytuj na zaliczeniu
chapters/*.tex            treść
literatura.bib            źródła
backmatter/               oświadczenie AI i wkład autorów
```

W `main.tex` wolno zmieniać tylko listę `\include` w sekcji rozdziałów. Reszty między `\begin{document}` a rozdziałami nie ruszaj.

Wyłączenie rozdziału: `%` przed `\include`. Dodanie:

```latex
\include{chapters/08-instrukcja-uzytkownika}
```

Plik `chapters/08-instrukcja-uzytkownika.tex` zaczyna się od:

```latex
\chapter{Instrukcja użytkownika}
```

Szybsza kompilacja (Overleaf; lokalnie też działa), w preambule `main.tex`:

```latex
\includeonly{chapters/01-wprowadzenie,chapters/04-realizacja}
```

Przed oddaniem zakomentuj `\includeonly` i skompiluj całość.

### Metadane — zmieniaj tylko tekst w `{ }`

```latex
\newcommand{\projectstatus}{draft}          % final wywala błąd, gdy brakuje danych
\newcommand{\projecttitle}{Tytuł}
\newcommand{\projectsubtitle}{}             % puste = brak podtytułu
\newcommand{\coursetitle}{Narzędzia informatyczne w praktyce inżynierskiej}
\newcommand{\projecttype}{Sprawozdanie z ćwiczenia laboratoryjnego}
\newcommand{\programme}{Informatyka}
\newcommand{\instructor}{dr inż. Marcin Kowol}
\newcommand{\projectauthors}{%
  Imię Nazwisko & 000000 \\
}
\newcommand{\projectpdfauthors}{Imię Nazwisko}   % bez & i bez \\
\newcommand{\submissiondate}{24.11.2026}
```

Kilku autorów:

```latex
\newcommand{\projectauthors}{%
  Anna Nowak & 123456 \\
  Jan Kowalski & 234567 \\
}
\newcommand{\projectpdfauthors}{Anna Nowak, Jan Kowalski}
```

Spisy — wartości to `true` albo `false`, bez cudzysłowów:

```latex
\newcommand{\showlistoffigures}{true}
\newcommand{\showlistoftables}{true}
\newcommand{\showlistoflistings}{true}
```

W `main.tex` spisy są już podpięte. Drugi raz `\listoffigures` nie dodawaj, jeśli te przełączniki są włączone. Samodzielnie (gdyby szablon ich nie miał):

```latex
\listoffigures
\listoftables
\lstlistoflistings
```

Znaki specjalne w tekście metadanych i w akapitach: `\%` `\&` `\_` `\#` `\$` `\{` `\}`. Przykład: `50\%`, `plik\_wynikowy`.

### Struktura dokumentu

```latex
\chapter{Tytuł rozdziału}       % 1
\section{Tytuł sekcji}          % 1.1
\subsection{Tytuł podsekcji}    % 1.1.1
\subsubsection{Jeszcze niżej}  % 1.1.1.1
```

Akapit = pusta linia. `\\` to łamanie wiersza (tabele, węzły TikZ), nie nowy akapit.

Załączniki, na końcu `main.tex` (już jest `\appendix`):

```latex
\appendix
\include{chapters/08-zalacznik-a}
```

Od `\appendix` kolejne `\chapter` dostają litery A, B, C.

---

## 2. Tekst, listy, matematyka (lab 3)

### Formatowanie

```latex
\textbf{pogrubienie}
\textit{kursywa}
\emph{wyróżnienie}      % zwykle kursywa; wewnątrz kursywy wraca do prostej
\texttt{kod w tekście}
\underline{podkreślenie}
```

W PDF ma być prawdziwa sekcja (`\section`), nie sam pogrubiony nagłówek.

### Listy

```latex
\begin{enumerate}
  \item Pierwszy krok.
  \item Drugi krok.
\end{enumerate}

\begin{itemize}
  \item prostota implementacji,
  \item niska efektywność dla dużych zbiorów.
\end{itemize}

\begin{description}
  \item[Bubble Sort] porównuje sąsiadów.
  \item[Insertion Sort] wstawia element w posortowaną część.
\end{description}
```

Numeracja a, b, c (pakiet `enumitem` jest w szablonie):

```latex
\begin{enumerate}[label=\alph*)]
  \item pierwszy
  \item drugi
\end{enumerate}
```

### Matematyka — ściąga znaków

W tekście: `\( ... \)` albo `$...$`. Osobny wiersz **bez** numeru: `\[ ... \]`. Osobny wiersz **z** numerem: środowisko `equation`.

```latex
\( a_i > a_{i+1} \)
\( O(n^2) \)
\( O(1) \)

\begin{equation}
  C(n) = \frac{n(n-1)}{2}
  \label{eq:porownania}
\end{equation}

\[
  S = \sum_{i=1}^{n} a_i
\]

\[
  f(x) = x^3 + 2x^2 - 5x, \qquad f'(x) = 3x^2 + 4x - 5
\]

\[
  \int_{0}^{1} x^2 \, dx = \frac{1}{3}
\]
```

| Chcesz | Piszesz |
|---|---|
| indeks | `a_i` `a_{i+1}` |
| potęga | `n^2` `x^{10}` |
| ułamek | `\frac{a}{b}` |
| suma | `\sum_{i=1}^{n} a_i` |
| całka | `\int_{0}^{1} x^2 \, dx` |
| pierwiastek | `\sqrt{x}` `\sqrt[3]{x}` |
| pochodna | `f'(x)` |
| tekst w wzorze | `\text{dla } n > 1` |
| odstęp | `\quad` `\qquad` `\,` |
| nierówności | `\leq` `\geq` `\neq` `\approx` |
| należenie | `\in` `\notin` |
| mnożenie | `\cdot` `\times` |
| nieskończoność | `\infty` `\lim_{n \to \infty}` |
| greckie | `\alpha` `\beta` `\Delta` `\pi` |
| nawiasy na wysokość | `\left( ... \right)` |
| wielokropek | `\ldots` `\cdots` |

Wiele równań z wyrównaniem (numer przy każdym wierszu):

```latex
\begin{align}
  f(x) &= x^2 - 2x - 3 \\
  f'(x) &= 2x - 2
\end{align}
```

Bez numerów: `align*` albo `equation*`.

Odwołanie do numeru równania: `\cref{eq:porownania}` → „równanie 1.1”. Na początku zdania: `\Cref{eq:porownania}`.

Jednostki (siunitx, polski przecinek):

```latex
\qty{12}{\volt}
\qty{883.7}{\milli\second}
\qty{100}{\percent}
\num{12497500}     % w PDF: 12 497 500
\num{0.4}          % w PDF: 0,4
```

W pliku CSV do wykresu zostaw **kropkę** (`0.4`). `\num` i `\qty` same zrobią przecinek.

---

## 3. Tabele (lab 4)

Podpis tabeli **nad** tabelą. `\label` **zaraz po** `\caption`. W tekście numer bierzesz z `\cref`, nigdy nie wpisujesz „Tabela 2” ręcznie.

Pięć kolumn, które mieszczą się w szerokości tekstu (`tabularx` + `booktabs` są w szablonie):

```latex
Zestawienie zawiera \cref{tab:porownanie}.

\begin{table}[htbp]
  \centering
  \caption{Porównanie przykładowych wyników dwóch algorytmów sortowania}
  \label{tab:porownanie}
  \begin{tabularx}{\textwidth}{@{}c *{4}{>{\centering\arraybackslash}X}@{}}
    \toprule
    Liczba elementów $n$
      & Bubble Sort czas [ms]
      & Insertion Sort czas [ms]
      & Bubble Sort porównania
      & Insertion Sort porównania \\
    \midrule
    100  & \num{0.4}   & \num{0.2}  & \num{4950}    & \num{2600} \\
    500  & \num{8.9}   & \num{4.1}  & \num{124750}  & \num{65000} \\
    1000 & \num{35.2}  & \num{16.3} & \num{499500}  & \num{260000} \\
    \bottomrule
  \end{tabularx}
\end{table}
```

Prosta tabela, gdy kolumn jest mało:

```latex
\begin{tabular}{lcc}
  \toprule
  Nazwa & Czas [ms] & Porównania \\
  \midrule
  Bubble Sort & 35,2 & 499500 \\
  Insertion Sort & 16,3 & 260000 \\
  \bottomrule
\end{tabular}
```

Specyfikacja kolumn: `l` lewo, `c` środek, `r` prawo, `p{3cm}` akapit o stałej szerokości, `X` rozciągana (tylko w `tabularx`). `|` rysuje pionową kreskę; w tym szablonie używa się `booktabs` bez pionowych kresek. `@{ }` ścina boczny margines komórki.

Linie: `\toprule` góra, `\midrule` środek, `\bottomrule` dół. `\hline` zostaw.

### Nagłówek dwupoziomowy

`\multicolumn` działa od razu. `\multirow` wymaga `\usepackage{multirow}` w `main.tex`.

```latex
\begin{tabular}{ccccc}
  \toprule
  \multirow{2}{*}{Liczba elementów}
    & \multicolumn{2}{c}{Czas wykonania [ms]}
    & \multicolumn{2}{c}{Liczba porównań} \\
  \cline{2-3} \cline{4-5}
    & Bubble & Insertion & Bubble & Insertion \\
  \midrule
  100 & 0,4 & 0,2 & 4950 & 2600 \\
  \bottomrule
\end{tabular}
```

`\multicolumn{2}{c}{tekst}` — 2 kolumny, wyśrodkowane. `\cline{2-3}` — kreska tylko pod kolumnami 2–3. `\multirow{2}{*}{tekst}` — komórka na 2 wiersze.

Tabela na wiele stron: środowisko `longtable` (pakiet jest). Podpis: `\caption{...}\\` na początku.

Gdy tabela jest za szeroka:

```latex
\begin{projectwidetable}
  \begin{tabular}{...}
    ...
  \end{tabular}
\end{projectwidetable}
```

---

## 4. Rysunki (lab 4)

Ścieżka jest liczona **od katalogu `main.tex`**, nie od pliku rozdziału.

Wariant szablonowy (sam dobiera szerokość do marginesów):

```latex
\projectgraphic[width=0.8\textwidth]{chapters/05-weryfikacja-i-wyniki/figures/wykres.png}
```

Wariant ze środowiskiem, podpisem i odwołaniem — tego chcą na zaliczeniu:

```latex
Zależność pokazuje \cref{fig:wykres-sortowania}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{%
    chapters/05-weryfikacja-i-wyniki/figures/wykres_sortowania.png}
  \caption{Przykładowa zależność czasu sortowania od liczby elementów}
  \label{fig:wykres-sortowania}
\end{figure}
```

Kolejność w rysunku: grafika, potem `\caption`, potem `\label`. Szerokość sensowna: `0.7\textwidth`–`0.85\textwidth`. `[htbp]` = tu, góra strony, dół strony, osobna strona.

Dwa obrazki obok siebie (`subcaption` jest w szablonie):

```latex
\begin{figure}[htbp]
  \centering
  \begin{subfigure}{0.48\textwidth}
    \centering
    \includegraphics[width=\linewidth]{figures/a.png}
    \caption{Wariant A}
    \label{fig:a}
  \end{subfigure}
  \hfill
  \begin{subfigure}{0.48\textwidth}
    \centering
    \includegraphics[width=\linewidth]{figures/b.png}
    \caption{Wariant B}
    \label{fig:b}
  \end{subfigure}
  \caption{Porównanie wariantów}
  \label{fig:oba}
\end{figure}
```

---

## 5. Kod źródłowy (lab 4 i 5)

Style gotowe w szablonie: `project-python`, `project-c`, `project-cpp`, `project-matlab`, `project-shell`. Mają już numerację wierszy (`numbers=left`), ramkę i podpis u góry. Polskich liter w listingu **nie** mapuj przez `literate`.

### Kod wklejony do `.tex`

```latex
Fragment pętli jest w \cref{lst:porownanie}.

\begin{lstlisting}[
  style=project-python,
  caption={Porównanie dwóch sąsiednich elementów},
  label={lst:porownanie}
]
if result[j] > result[j + 1]:
    result[j], result[j + 1] = result[j + 1], result[j]
\end{lstlisting}
```

### Kod z pliku (tego pilnują)

Python:

```latex
\lstinputlisting[
  style=project-python,
  caption={Sortowanie bąbelkowe},
  label={lst:bubble-sort}
]{chapters/04-realizacja/code/bubble_sort.py}
```

C (lab 5), język i numery wierszy:

```latex
Funkcję przedstawia \cref{lst:max-element}.

\lstinputlisting[
  style=project-c,
  language=C,
  numbers=left,
  caption={Wyszukiwanie największego elementu tablicy},
  label={lst:max-element}
]{chapters/04-realizacja/code/max_element.c}
```

Tylko wybrane linie (np. sama funkcja, bez `main`):

```latex
\lstinputlisting[
  style=project-c,
  firstline=1,
  lastline=12,
  caption={Sama funkcja max\_element},
  label={lst:max-fragment}
]{chapters/04-realizacja/code/max_element.c}
```

W podpisie listingu podkreślnik to `\_`. W kodzie wewnątrz `lstlisting` piszesz `_` normalnie.

Zmiana pliku `.py` / `.c` wchodzi do PDF po zapisaniu pliku i ponownej kompilacji. Kodu w `.tex` wtedy nie przepisujesz.

Inne opcje, gdyby kazali:

```latex
numbers=none          % wyłącz numery
basicstyle=\ttfamily\footnotesize
breaklines=true       % już jest w stylu project
frame=single
```

Język bez stylu projektu: `\begin{lstlisting}[language=Python]`.

`max_element` w tekście: `\texttt{max\_element}`.

---

## 6. Odwołania (lab 4 i 5)

| Obiekt | Etykieta | Po czym |
|---|---|---|
| tabela | `\label{tab:...}` | po `\caption` |
| rysunek | `\label{fig:...}` | po `\caption` |
| listing | `label={lst:...}` | w opcjach listingu |
| równanie | `\label{eq:...}` | wewnątrz `equation` |
| rozdział | `\label{chap:...}` | po `\chapter` |
| sekcja | `\label{sec:...}` | po `\section` |

```latex
\cref{tab:porownanie}     % tabela 3.1   (w środku zdania)
\Cref{fig:wykres}         % Rysunek 3.2  (początek zdania)
\ref{tab:porownanie}      % sam numer 3.1
\pageref{fig:wykres}      % numer strony
\cref{tab:a,tab:b}        % tabela 1.1 i 1.2
```

Szablon tłumaczy nazwy: tabela, rysunek, listing, równanie, rozdział. Dlatego na zaliczeniu pisz `\cref`, nie „Rys. 1”.

`??` w PDF: etykieta jest przed `\caption`, literówka w kluczu, albo brakuje drugiej kompilacji LuaLaTeX.

Każdy klucz w całym projekcie jest unikalny.

---

## 7. Bibliografia (lab 5)

Źródła tylko w `literatura.bib`. W tekście `\cite{klucz}`. Numerów `[1]` nie wpisujesz. Wykaz robi `\printprojectbibliography` (już jest w `main.tex`).

Kolejność w PDF: **alfabetycznie po nazwisku pierwszego autora**, potem rok, potem tytuł. To nie jest kolejność cytowań w tekście.

Autorów rozdziela angielskie `and`, także po polsku: `Jan Kowalski and Anna Nowak`. Organizacja jako autor: podwójne nawiasy `{{GNU Project}}`.

Po każdej zmianie `.bib`: LuaLaTeX, Biber, LuaLaTeX, LuaLaTeX. Zostawiony klucz `[gcc2026]` albo brak rozdziału „Literatura” = Biber nie poszedł.

### Strona / dokumentacja (`@online`) — obowiązkowe na lab 5

```latex
@online{gcc2026,
  author  = {{GNU Project}},
  title   = {GCC online documentation},
  year    = {2026},
  url     = {https://gcc.gnu.org/onlinedocs/},
  urldate = {2026-11-24}
}

@online{latexdocs2026,
  author  = {{LaTeX Project}},
  title   = {LaTeX documentation},
  year    = {2026},
  url     = {https://www.latex-project.org/help/documentation/},
  urldate = {2026-11-24}
}
```

`urldate` to data dostępu, format `RRRR-MM-DD`. Źródła mają być prawdziwe. Cytujesz publikację, nie Google Scholar. BibTeX ze Scholara sprawdzasz w oryginale.

### Książka, artykuł, manual

```latex
@book{lamport1994,
  author    = {Leslie Lamport},
  title     = {LaTeX: A Document Preparation System},
  edition   = {2},
  year      = {1994},
  publisher = {Addison-Wesley}
}

@article{knuth1998,
  author  = {Donald E. Knuth},
  title   = {Tytuł artykułu},
  journal = {Nazwa czasopisma},
  year    = {1998},
  volume  = {10},
  number  = {2},
  pages   = {1--12},
  doi     = {10.0000/przyklad}
}

@manual{listings2024,
  title   = {The Listings Package},
  year    = {2024},
  url     = {https://ctan.org/pkg/listings},
  urldate = {2026-11-24}
}
```

W tekście:

```latex
Składnię opisuje dokumentacja GCC \cite{gcc2026}.
Porównaj \cite{lamport1994,knuth1998}.
Szczegóły podaje \cite[s.~12]{lamport1994}.
```

Przecinek po każdym polu w `.bib`. Klucz (to przed przecinkiem w `@online{gcc2026,`) bez spacji i bez polskich znaków. Procent `%` w `.bib` komentuje resztę wiersza.

---

## 8. TikZ — schemat blokowy (lab 6)

Wykres i schemat rysujesz kodem, nie wklejasz PNG. Biblioteki `positioning`, `shapes.geometric`, `arrows.meta` są już w stylu.

Kształty z zajęć: `ellipse` (start/koniec), `rectangle` (operacja), `diamond` (warunek). Położenie: `below=of nazwa`. Strzałka: `-{Stealth}`. Powrót pętli: `-- ++(1.5,0) |-`.

Gotowiec sortowania bąbelkowego (wstaw w `figure`):

```latex
Schemat działania pokazuje \cref{fig:babelkowe}.

\begin{figure}[htbp]
  \centering
  \begin{tikzpicture}[
      node distance=9mm,
      startstop/.style={ellipse, draw, align=center, minimum width=2.6cm},
      process/.style={rectangle, draw, align=center, minimum width=3.6cm},
      decision/.style={diamond, draw, align=center, aspect=2.4, inner sep=1pt},
      every path/.style={-{Stealth}}
    ]
    \node[startstop] (start) {Start};
    \node[process, below=of start] (pobierz) {Pobierz tablicę};
    \node[process, below=of pobierz] (przebieg)
      {Wykonaj pełny przebieg\\porównań i zamian};
    \node[decision, below=14mm of przebieg] (warunek)
      {Czy wykonano\\zamianę?};
    \node[startstop, below=14mm of warunek] (koniec) {Koniec};

    \draw (start) -- (pobierz);
    \draw (pobierz) -- (przebieg);
    \draw (przebieg) -- (warunek);
    \draw (warunek) -- node[right] {Nie} (koniec);
    \draw (warunek.east) -- ++(1.6,0) |- (przebieg.east)
      node[pos=0.25, right] {Tak};
  \end{tikzpicture}
  \caption{Schemat blokowy sortowania bąbelkowego}
  \label{fig:babelkowe}
\end{figure}
```

Ściąga pozycji (biblioteka `positioning`):

```latex
below=of start
above=of start
right=of start
left=of start
below=12mm of start
```

Kotwice węzła: `.north` `.south` `.east` `.west`.

Podpis gałęzi na strzałce: `-- node[right] {Nie}`. Łamanie tekstu w węźle: `\\` oraz `align=center`.

Wariant z warunkiem `n < 2` (zadanie dodatkowe):

```latex
\node[decision, below=12mm of pobierz] (maly) {$n < 2$?};
\node[process, below=14mm of maly] (przebieg) {Pełny przebieg};
\draw (pobierz) -- (maly);
\draw (maly) -- node[right] {Nie} (przebieg);
\draw (maly.east) -- ++(1.8,0) node[above, pos=0.7] {Tak} |- (koniec.east);
```

Style globalne (jedna zmiana koloru aktualizuje wszystkie węzły tego typu). W preambule albo przed rysunkiem:

```latex
\tikzset{
  proces/.style={rectangle, draw, fill=blue!8, align=center, minimum width=3.4cm},
  decyzja/.style={diamond, draw, fill=orange!15, align=center, aspect=2.2, inner sep=1pt},
  terminator/.style={ellipse, draw, fill=green!12, align=center, minimum width=2.6cm}
}
```

Potem `\node[proces] ...`. Kolor: `fill=blue!10`, `draw=projectblue`. `projectblue` jest zdefiniowany w stylu szablonu.

Gdy schemat wychodzi za margines: zmniejsz `minimum width`, `node distance` i `aspect`, albo owiń w `\resizebox{0.95\textwidth}{!}{ ... }`.

Minimalny szkielet, gdy każą „od zera”:

```latex
\begin{tikzpicture}
  \node[ellipse, draw] (start) {Start};
  \node[rectangle, draw, below=of start] (krok) {Pobierz tablicę};
  \draw[-{Stealth}] (start) -- (krok);
\end{tikzpicture}
```

Bez `below=of` (gdyby biblioteki `positioning` nie było):

```latex
\node[rectangle, draw] at (0,-1.5) (krok) {Pobierz tablicę};
\draw[-{Stealth}] (start) -- (krok);
```

---

## 9. PGFPlots (lab 7)

W `main.tex` po stylu:

```latex
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
```

Wyrażenia w `\addplot` pisz z gwiazdką mnożenia: `x^2 - 2*x - 3`. Zakres: `domain=-2:4`. Gęstość krzywej: `samples=100`. Grubości: `thin`, `thick`, `very thick`. Siatka: `grid=major` albo `grid=both`.

### Funkcja

Z zajęć: \(f(x) = x^2 - 2x - 3\) dla \(x \in [-2, 4]\). Minimum w \(x = 1\), \(f(1) = -4\).

```latex
\begin{figure}[htbp]
  \centering
  \begin{tikzpicture}
    \begin{axis}[
        width=0.82\textwidth,
        height=7cm,
        xlabel={$x$},
        ylabel={$f(x)$},
        grid=both,
        scaled ticks=false,
        ymin=-5, ymax=6,
      ]
      \addplot[domain=-2:4, samples=101, very thick] {x^2 - 2*x - 3};
      \addplot[only marks, mark=*, mark size=2.5pt, red] coordinates {(1,-4)};
    \end{axis}
  \end{tikzpicture}
  \caption{Wykres funkcji $f(x) = x^2 - 2x - 3$}
  \label{fig:funkcja}
\end{figure}
```

`scaled ticks=false` wyłącza mnożnik typu \(\cdot 10^{3}\) przy osi.

### Dwie serie z CSV

Plik (kropka dziesiętna, przecinek jako separator kolumn), np. `dane_porownawcze.csv` obok `main.tex`:

```text
n,bubble_ms,insertion_ms,bubble_porownania,insertion_porownania
100,0.4,0.2,4950,2600
500,8.9,4.1,124750,65000
1000,35.2,16.3,499500,260000
2000,141.5,65.1,1999000,1040000
5000,883.7,406.4,12497500,6500000
```

Wykres czyta plik. Liczb do `\addplot` nie przepisuj.

```latex
\begin{figure}[htbp]
  \centering
  \begin{tikzpicture}
    \begin{axis}[
        width=0.88\textwidth,
        height=7.5cm,
        xlabel={Liczba elementów $n$},
        ylabel={Czas wykonania [ms]},
        grid=major,
        legend pos=north west,
        scaled ticks=false,
        xmin=0, xmax=5400,
        ymin=0,
      ]
      \addplot[very thick, mark=*, mark size=1.8pt]
        table[col sep=comma, header=true, x=n, y=bubble_ms]
        {dane_porownawcze.csv};
      \addplot[thick, dashed, mark=square*, mark size=2pt]
        table[col sep=comma, header=true, x=n, y=insertion_ms]
        {dane_porownawcze.csv};
      \legend{Bubble Sort, Insertion Sort}
    \end{axis}
  \end{tikzpicture}
  \caption{Przykładowe czasy wykonania algorytmów sortowania}
  \label{fig:czasy-sortowania}
\end{figure}
```

Odwołanie i jednostki w tekście:

```latex
\Cref{fig:czasy-sortowania} pokazuje czasy syntetyczne, nie pomiary.
Dla \(n = 5000\) Bubble Sort zajmuje \qty{883.7}{\milli\second}.
```

Zmiana liczby w CSV + kompilacja przesuwa punkt. Po teście przywróć oryginał.

### Warianty, o które mogą zapytać

Skala logarytmiczna (wszystkie \(y > 0\); zero na osi Y wtedy odpada):

```latex
\begin{axis}[ymode=log, xlabel={Liczba elementów $n$}, ylabel={Czas [ms]}, legend pos=north west]
  \addplot[very thick, mark=*]
    table[col sep=comma, x=n, y=bubble_ms] {dane_porownawcze.csv};
  \legend{Bubble Sort}
\end{axis}
```

Same punkty, bez linii:

```latex
\addplot[only marks, mark=*, mark size=2.5pt]
  table[col sep=comma, x=n, y=bubble_ms] {dane_porownawcze.csv};
```

Liczba porównań (te same kolumny CSV):

```latex
\addplot[very thick, mark=*]
  table[col sep=comma, x=n, y=bubble_porownania] {dane_porownawcze.csv};
\addplot[thick, dashed, mark=square*]
  table[col sep=comma, x=n, y=insertion_porownania] {dane_porownawcze.csv};
\legend{Bubble Sort, Insertion Sort}
```

Oś Y wtedy podpisz `Liczba porównań` i podnieś `ymax` (wartości idą w miliony) albo włącz `scaled ticks`.

Inna legenda, gdy nie chcesz `\legend`:

```latex
\begin{axis}[legend entries={Bubble Sort, Insertion Sort}, legend pos=north east]
```

Pozycje legendy: `north west`, `north east`, `south east`, `outer north east`.

Znaczniki: `mark=*`, `mark=square*`, `mark=triangle*`, `mark=o`, `mark=diamond*`. Linie: `solid`, `dashed`, `dotted`. Kolory: `blue`, `red`, `orange`, `projectblue`, `blue!70`.

Wykres w osobnym pliku `wykres-czasy.tex` (sam `tikzpicture`, bez `\documentclass`) i w rozdziale:

```latex
\input{wykres-czasy.tex}
```

`\input` wstawia w miejscu wywołania. `\include` zaczyna nową stronę i nie bierze rozszerzenia.

---

## 10. Kolejność, która nie wywala kompilacji

Tabela:

```text
\begin{table} → \centering → \caption → \label → \begin{tabular} → dane → \end{tabular} → \end{table}
```

Rysunek / TikZ / wykres:

```text
\begin{figure} → \centering → obrazek albo tikzpicture → \caption → \label → \end{figure}
```

Listing: `caption` i `label` w nawiasie kwadratowym opcji, plik na końcu w `{ }`.

Cytowanie: najpierw rekord w `.bib`, potem `\cite{klucz}`, potem Biber.

---

## 11. Pułapki z laboratoriów

| Objaw | Co zrobić |
|---|---|
| „Ten szablon wymaga LuaLaTeX”, `OT1`, `Invalid UTF-8` w `main.vrb` | kompilator to pdfLaTeX; przestaw na LuaLaTeX i skompiluj od zera |
| w tekście `[gcc2026]` zamiast `[1]` | uruchom Biber, potem dwa razy LuaLaTeX |
| brak rozdziału Literatura | to samo + sprawdź, czy `\cite` w ogóle jest w tekście |
| `??` | `\label` po `\caption`, zgodny klucz, druga kompilacja |
| `File ... not found` | ścieżka od `main.tex`; sprawdź katalog i rozszerzenie |
| `Undefined control sequence` przy `\addplot` | brak `\usepackage{pgfplots}` |
| `Undefined control sequence` przy `\multirow` | brak `\usepackage{multirow}` |
| wykres CSV pusty / błąd tabeli | `col sep=comma`, nazwy kolumn jak w pierwszym wierszu, kropka w liczbach |
| skala log wywala się | w danych jest 0 albo liczba ujemna |
| polskie znaki w listingu rozsypane | zostań przy LuaLaTeX; nie dodawaj `literate` |
| `final` przerywa kompilację | wróć na `draft` albo uzupełnij metadane |
| `\projectpdfauthors` z `&` albo `\\` | tam jest zwykły tekst, przecinki |
| dwa razy ten sam `\label` | zmień jeden klucz |
| rysunek sam na stronie z wielką dziurą | zmniejsz `width`, zmień `[htbp]` na `[ht]` |
| numer tabeli wpisany słownie | zamień na `\cref{tab:...}` |
| literatura jako lista w rozdziale | przenieś do `.bib` i `\cite` |
| schemat jako PNG | przerób na `tikzpicture` |
| wykres jako PNG | przerób na `axis` + `\addplot` |

Komunikat czytaj od pierwszej linii z `!` albo `error`. Poprawiasz plik, który edytor wskazuje, i kompilujesz znowu.

---

## 12. Dokument od zera (gdyby nie dali szablonu)

Na zajęciach zawsze był szablon. Gdyby kazali pusty plik, minimalna preambuła pod te 6 laborek:

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[polish]{babel}
\usepackage{amsmath,booktabs,tabularx,siunitx,graphicx,listings}
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta,shapes.geometric}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepackage[backend=biber,style=numeric,sorting=nyt]{biblatex}
\addbibresource{literatura.bib}
\usepackage{hyperref}
\usepackage{cleveref}
\begin{document}

% tu rozdziały: \section, table, figure, lstlisting, tikzpicture, axis

\printbibliography[heading=bibintoc,title={Literatura}]
\end{document}
```

W `article` jest `\section`, nie `\chapter`. W szablonie projektu klasa to `report`, więc rozdziały to `\chapter`.

Kompilacja: `lualatex`, `biber`, `lualatex`, `lualatex`.

---

## 13. Checklista przed oddaniem

- Kompilator: LuaLaTeX. PDF otwiera się, polskie znaki są całe.
- Strona tytułowa z `metadata.tex`, status `draft` (albo `final` tylko gdy prowadzący każe i dane są pełne).
- Sekcje zrobione poleceniami, nie pogrubieniem.
- Jest `\textbf` i `\textit` (albo `\emph`).
- Jest `itemize` i `enumerate`.
- Indeks, potęga, ułamek, suma, pochodna. Przynajmniej jedno `equation` z numerem.
- Tabela: 5 kolumn, `\caption`, `\label`, w tekście `\cref`.
- Rysunek z pliku: szerokość względem `\textwidth`, podpis, etykieta, `\cref`.
- Listing w `lstlisting` oraz drugi przez `\lstinputlisting`.
- Przy C: `language=C`, `numbers=left`, podpis, etykieta, `\cref`.
- TikZ: elipsa, prostokąt, romb, strzałki, gałęzie Tak/Nie, `figure` + `\caption` + `\label`.
- PGFPlots: funkcja z `domain`, `xlabel`, `ylabel`, `grid`, `very thick`.
- Drugi wykres z CSV (`col sep=comma`, `x=`, `y=`), dwie serie, `\legend`, jednostki na osi.
- `literatura.bib`: prawdziwe źródła, `url` + `urldate`, autorzy przez `and`.
- W tekście co najmniej dwa `\cite`. Po Biberze numery, nie klucze.
- Spisy rysunków i tabel włączone (`true`) i po kompilacji mają aktualne strony.
- Żadnego `??`, żadnej literatury wpisanej ręcznie jako lista, żadnego „Rys. 1” na sztywno.
