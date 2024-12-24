# D&C_Paralelismo

**Número da Lista**: X<br>
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

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

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



