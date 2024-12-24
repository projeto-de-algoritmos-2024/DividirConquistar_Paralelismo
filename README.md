# D&C_Paralelismo

**Número da Lista**: 9<br>
**Conteúdo da Disciplina**: Divisão e Conquista<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 221008436  | Ryan Augusto Brandão Salles |
| 221008481 |  Víctor Moreira Almeida |

## Sobre 
O projeto visa observar a performance de um algoritmo dividir e conquistar após a aplicação de paralelismo
e observar exatamente quanta performance pode ser obtida ou perdida no processo a depender de especificidades como
quantidade de processos gerados.

[explicação estensa do código e relatorio](https://youtu.be/patzm9WBnTU)

O relatório está disponível em tex e pdf na pasta tex.

## Screenshots
[](https://raw.githubusercontent.com/projeto-de-algoritmos-2024/DividirConquistar_Paralelismo/refs/heads/main/assets/rodando1.png)
[](https://raw.githubusercontent.com/projeto-de-algoritmos-2024/DividirConquistar_Paralelismo/refs/heads/main/assets/rodando2.png) 
[](https://raw.githubusercontent.com/projeto-de-algoritmos-2024/DividirConquistar_Paralelismo/refs/heads/main/assets/rodando3.png)

## Instalação 
**Linguagem**: Python<br>
Basta clonar o projeto e rodar os scripts na pasta src.

Cada script é contido em seu próprio código e apresenta um (tosco) relatório de performance 
para cada rodagem.

## Uso 

1. Após a iniciação do script, escolha a quantidade de números a serem gerados.
2. Após a quantidade, escolha a semente de geração.
3. Será rodado inicialmente o algoritmo paralelizado, do qual espera-se que seja mais rápido, em geral.
4. Após, será rodado o algoritmo single-thread e single process, que deve demorar consideravelmente mais.

## Outros

NÃO UTILIZAR MULTIPROCESSING DA MESMA FORMA QUE THREADING.

Ademais, a quantidade de threads no algoritmo descrito no relatório pode ser alterada por meio da constante
THREADS. Leia o trecho Resultados para mais detalhes.



