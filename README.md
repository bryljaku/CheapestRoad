# Projekt Analiza Algorytmów

## Wizytówka

| Pole      | Wartość       |
| --------- |:-------------:|
| Imię      | Jakub      |
| Nazwisko  | Bryl         |
| Numer indeksu | 293085 |
| Studia | Informatyka inżynierskie |
| Semestr | 5 |

## Tytuł i treść problemu
### Podróż

Dane są miasta połączone siecią dróg. Dla każdej drogi znany jest czas przejazdu w godzinach. Wjazd do każdego miasta oraz na każdą drogę jest płatny (koszt ustalony oddzielnie dla każdego miasta i drogi). Miasta mogą należeć do grup miast partnerskich - wjazd do takiego miasta zwalnia z oplat za wjazd do pozostałych miast partnerskich. Każda godzina podróży ma ustalony koszt (niezależny od drogi). Należy znaleźć najtańszą opcję podróży pomiędzy dwoma wyróżnionymi miastami.

# Interpretacja problemu
W opisie problemu występuję 2 rodzaje obiektów:
- miasto <cena_biletu, grupa>
- droga <liczba godzin potrzebnych na przejechanie, cena biletu>
Sieć tych elementów tworzy graf spójny. Wierzchołki tego grafu są miastami a drogi krawędziami.
Problemem jest znalezienie najtańszej drogi od punktu A do B uwzględniając przy tym wszystkie czynniki wpływające na koszt podróży.

## Informacja o możliwych poleceniach aktywacji programu
### Warianty uruchomienia
- Rozwiąż zadany graf `./python3 main.py -input_file [path_to_input_file] -hour_cost <number>`
    - Wpisz dane ręcznie lub przekieruj z pliku.
    - Wypisz dane tylko na standardowe wyjście lub także do pliku (nazwa pliku jako argument).
- Wygeneruj i sprawdź graf o zadanych atrybutach `python3 main.py -hour_cost <number> -number_of_nodes <number> -number_of_groups <number> -even_groups <number> -max_city_ticket_price <number> -min_city_ticket_price <number> -max_road_ticket_price <number> -min_road_ticket_price <number> -max_distance <number> -min_distance <number>` -test <0/1>

- Narysuj wykres złożoności `python3 plot.py fileName`
    - parametr `fileName` to nazwa pliku wygenerowanego przez program
## Opis konwencji dotyczących danych wejściowych i prezentacji wyników
### Przykładowy plik wejściowy
```
0 5 1 
1 10 0
2 505 1
3 20 2
#
1 0 10 4
1 2 10 4
2 3 41 3
eof

```
`Node - <id, ticket_cost, group>` group 0 == no group
`Edge - <Node, Node, hours_needed_for_travel, ticket_price>`

### Prezentacja wyników
- Ścieżka przebyta aby osiągnąć cel, ostateczny koszt i czas wykonania.
`path: [1, 0, 5, 6, 12, 17, 26, 99] cost: 2681 time: 0.0005493209999940518`
 
|nodes|edges|time|groups|reversable_nodes
 ```
 480;479;0.001539150998723926;5;0
495;494;0.0009607810006855289;5;0
510;509;0.0015324500000133412;5;0
525;524;0.001987486000871286;5;0
540;539;0.0018332680010644253;5;0
555;554;0.0020934900003339862;5;0
570;569;0.002231202000984922;5;0
585;584;0.001691837000180385;5;0
600;599;0.002001201999519253;5;0
615;614;0.0023539470003015595;5;0
```

``` 

```
## Krótki opis metody rozwiązania, zastosowanych algorytmów i struktur danych

- Język: Python
- Zastosowane algorytmy:
    - zmodyfikowany algorytm Dijkstra

- Wartość zwracana: Lista miast reprezentująca przebytą drogę, całkowity koszt.
- Złożoność: O((V*logV + E)^V) gdzie potęga zależy od ilości miast do których "warto" pojechać tylko po bilet do grupy. W przypadku gdy miasta z danej grupy mają koszty biletu na podobnym poziomie, złożoność algorytmu jest równa O(V*logV + E) - czyli jest równa złożonośći algorytmu Dijsktry.

- Struktury danych:
    - Graph: Dict[Node] i List[Edge]
    - Node: atrybuty danego wierzchołka oraz list id sąsiadujących z nim Node'ów  
    - Edge: atrybuty danej krawędzi
## Informacje o funkcjonalnej dekompozycji programu na moduły źródłowe - nagłówkowe i implementacyjne ("przewodnik" po plikach źródłowych)
- Graph - struktury wymagane do utworzenia grafu
- GraphGenerator - generator grafu połączonego
- PriorityQueue - kolejka zaimplementowana przy użyciu kopca
- Dijkstra - algorytm poszukiwania ścieżki
- solver - tzw "main", odpowiada za przyjęcie argumentów od użytkownika i uruchomienie programu w odpowiednim trybie
 


## Opis algorytmu
Dla przypadku w którym nie mamy żadnych miast które są "zawracalne" algorytm zachowuje się jak zwyczajny algorytm Dijkstry.
Natomiast gdy takie miasta znajdują się w naszym grafie, w trakcie przeszukiwania gdy natrafimy na takie miasto, zapisywany jest stan(dotychczasowa ścieżka, dotychczasowy koszt, zebrane bilety) w jakim obecnie jesteśmy i po odnalezieniu przez algorytm "najlepszej" ścieżki sprawdzane są wszystkie takie stany. Sprawdzanie polega na uruchomieniu algorytmu Dijkstry startując z wierzchołka zapisanego w stanie. Umożliwia to powrót do wcześniej odwiedzonych miast.

## Złożoność obliczeniowa
- Załadowanie danych i utworzenie grafu: O(E + V)
- Podstawowy algorytm Dijkstry z użyciem kolejki zaimplementowanej przez kopiec: O(E + V*log(V))
- Przypadek gdy w grafie są miasta z których opłaca się zawracać: O((E + V*log(V))^reversable_vertices) i w najgorszym wypadku jest równa O((E + V*log(V))^(V/2)).
- Szukanie zawracalnych miast:  O(V^2 + E)

## Generator danych testowych
Utworzony generator tworzy graf spójny o zadanej liczbie wierzchołków. Przyjmuje parametry `number_of_nodes, number_of_groups, even_cost_in_one_group, max_city_ticket_price, min_city_ticket_price, max_distance, min_distance, max_road_ticket_price, min_road_ticket_price, hour_cost`

## Testowanie 
Poprawność rozwiązania była testowana na kilku prostych grafach utworzonych ręcznie.
Złożoność obliczeniowa była testowana na grafach utworzonych przy użyciu generatora załączonego do projektu.


## Wyniki projektu
![alt tag](https://github.com/jbryl7/CheapestRoad/blob/master/regular_dijkstra_equal_groups.png)

Dla przypadku prostszym w którym wszystkie miasta w danej grupie miały identyczny koszt złożoność wynikająca z wykresu mniej więcej pokrywa się ze złożonością przewidywaną. Odchyły są spowodowane losowością generatora.





![alt tag](https://github.com/jbryl7/CheapestRoad/blob/master/modified_dijkstra.png)

w przypadku trudniejszym można zauważyć że jest kilka wartości które znacząco odbiegają od reszty wyników. Jest to spowodowane losowością generatora i wynikającą z tego liczbą miast "zawracalnych" oraz ich położenia w grafie.