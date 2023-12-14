Nesse trabalho avaliaremos as implementações dos algoritmos para computação de rotas no problema do caixeiro viajante. Especificamente, avaliaremos uma solução exata, baseada em branch-and-bound, e as duas soluções aproximadas vistas em sala de aula para o TSP euclidiano, twice-around-the-tree e algoritmo de Christofides.
<h1>Como executar?</h1>
<ul>
        <li>Para executar o código, rode o seguinte comando:</li>
        <ul>
            <li><code>python src/main.py "nome_do_algoritmo"</code> (Windows)</li>
            <li><code>python3 src/main.py "nome_do_algoritmo"</code> (Linux)</li>
        </ul>
        <li>Em <code>nome_do_algoritmo</code>, altere para o nome do algoritmo correspondente:</li>
        <ul>
            <li>Branch and Bound: <code>branch</code></li>
            <li>Twice Around the Tree: <code>twice</code></li>
            <li>Christofides: <code>christofides</code></li>
        </ul>
        <li>O código irá criar um CSV com o nome do algoritmo mostrando os resultados. Este CSV se encontrará na pasta <code>resultados</code>.</li>
        <li>Os CSVs com o nome "completo" contêm todos os testes que rodaram satisfatoriamente neste trabalho.</li>
    </ul>
