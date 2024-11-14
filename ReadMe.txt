Marcos-
Eu tenho que identificar o fato gerador do credito estornavel.
dentro do contexto do freegames eu sei que quanto eu tenho uma sobreposicao direta de mascaras, o valor da ultima mascara sobreposta
deve ser estornavel.

Processo de absorcao destes credito estornavel.
Eu tenho que armazenar este valor em um objeto em cache.
Ele tem que ser abatido a cada premio ganho em freegames.
Somente sera pago ao cliente o valor que sobre apos este abatimento.
Exemplo.

Momento 1.
Tirei uma mascara Duplo T.
Ganhei 75 credito.
Por conta do instant deposit eu imediatamente creditei a conta do cliente.
No entanto eu armazenei em cache este ultimo valor para que, caso aconteca um evento de sobreposicao no futuro, eu tenha
o controle para saber o quanto que eu tenho que estornar dos creditos de freegames subsequentes ao fato gerador.
Momento 2.
Tirei um House e com isso crio um fato gerador de estorno do ultimo premio sobreposto diretamente.
Entro em freegames e começo a jogar o bonus.
Momento 3.
Para cada valor ganho no curso do freegames, eu realizo o abatimento do total estornavel do fato gerador relacionado.
Termino de jogar os premios e com isso eu posso ter tres situacoes.
    1-Ganhei um valor superior ao aquele estornavel pelo fato gerador originario.
        Neste caso eu credito ao cliente o valor residual.
    2-Ganhei um valor inferior ao aquele estornavel pelo fato gerador originario.
        Neste caso eu vou creditar ao cliente o valor correspondente a diferenca entre o total ganho subtraido do total estornavel
        pelo fato gerador.
        Exemplo: 
        Valor Estornavel 75.
        Valor Ganho em jogos freegames 40.
        Valor a ser creditado ao cliente é 35.
    3-Nada ganhei durante o as rodadas de freegames.
        Neste caso eu credito ao cliente o valor integral daquele estornavel relacionado ao fato gerador originario.

Momento 4.
Tenho que registrar estas operacoes para poder realizar a contabilidade.


Isa - 
Temos um cenario novo que pode acontecer em qualquer jogo, inclusive nos estamos falando de freegames, entretanto, isso
vai acontecer na linha megamix.
Essa situacao vai acontecersempre que tivemos alguma situacao em que nos tivermos um premio onde nos pagamos um bonus do tipo nao 
financeiro.
Normalmente, quando temos esta situacao nos fazemos o bonus compensar o valor do premio.
Isso por si ja é um problema por conta do instant deposit.
Quando nos pagamos um premio na paytable, nos depositamos direto na conta do jogador.
E uma regra de negocio que nos nao podemos estornar o premio em  dinheiro na carteira do jogador.

Sao duas partes.
1-Entao, uma parte do problema é esta etapa do instant deposit.
Onde eu ja realizei o deposito na conta do cliente e por nao poder estornar este valor, eu tenho que 
abater este valor estornavel dos premios que a rodada vai me pagar no curso do freegames.

Logo, eu vou abatendo dos creditos ganhos do freegames este valor que deveria ser estornavel.

2-No freegames ha um cenario bem improvavel onde o jogador pode sair em perda.
Nestes casos, nos vamos cobrir o prejuizo, pagando ao jogador o valor integral do ultimo credito nao acumulavel.




