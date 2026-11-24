/* Funkcja zwraca największy element niepustej tablicy. */
int max_element(const int tab[], int n)
{
    int max = tab[0];
    for (int i = 1; i < n; i++) {
        if (tab[i] > max) {
            max = tab[i];
        }
    }
    return max;
}
