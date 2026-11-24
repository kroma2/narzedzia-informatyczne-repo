# Wariant lokalny

Paczka jest przeznaczona do kompilacji na komputerze. Podstawowy wariant wymaga
MiKTeX-a i korzysta bezpośrednio z LuaLaTeX; Perl nie jest potrzebny:

```text
lualatex main.tex
```

Gotowy dokument powstanie jako `main.pdf` w katalogu projektu. Szczegółowa
konfiguracja TeXstudio i obsługa bibliografii są opisane w `README.md`.

Paczka zawiera także `latexmkrc`. Opcjonalna automatyzacja przez:

```text
latexmk main.tex
```

wymaga w systemie Windows interpretera Perl, np. Strawberry Perl. LatexMk
automatycznie uruchamia LuaLaTeX i Biber, a wynik zapisuje w `build/main.pdf`.
