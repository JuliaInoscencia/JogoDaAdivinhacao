# Jogo Da Adivinhação

O objetivo do EP é implementar um jogo de adivinhação de números, no qual o usuário tentará adivinhar um número "sorteado" pelo computador a partir de dicas que o programa fornecerá.

O programa deverá pedir que o usuário digite um número inteiro (a semente) e usá-lo para "sortear" o número inteiro (que depois deverá ser "adivinhado" pelo usuário de seu programa).  As instruções sobre como fazer o "sorteio" estão na seção 3 mais abaixo no enunciado, mas vocês precisarão gerar apenas um valor.

Após o "sorteio" do número,  seu programa deverá permitir que o usuário faça “chutes”, ou seja, tentativas para adivinhar o número.

A cada "chute" errado, seu programa deverá exibir uma ou duas dicas para o usuário, para tentar ajudá-lo na adivinhação, como mostrado nos exemplos abaixo. Faz parte de seu trabalho deduzir a regra algoritmica da segunda dica (e.g. quando ela é ou não apresentada).

O programa deverá permitir que o usuário faça no máximo 5 tentativas. Se o usuário não adivinhar o número em até 5 tentativas, o programa deverá exibir o número sorteado.

## Como "sortear" um número?

Para implementação de programas envolvendo geração de valores aleatórios, usamos funções especialmente desenhadas para tal fim, que simulam a geração de aleatoriedade e por isso dizemos que geram números pseudo-aleatórios (https://en.wikipedia.org/wiki/Pseudorandomness).

Devido ao seu grande número de aplicações, geralmente as linguagens de programação apresentam funções próprias para geração pseudo-aleatória que passam em testes estatísticos (e até simulam distribuições específicas, como normal ou Bernoulli).

Na verdade essas funções geram uma sequência constante, bem definida, digamos S = {x0, x1, x2, ... xN}. Mas a linguagem também possibilita um modo de iniciar por qualquer dos elementos da sequência, dizemos que esse elemento será a semente, para a geração da sequência.

Se você fornecer uma mesma semente como entrada em diferentes execuções do programa, elas "sortearão" exatamente os mesmos números (como ocorre nos exemplos 2 e 3 apresentados neste enunciado).

Um vez que precisamos do avaliador automático do VPL e que funcione de maneira idêntica (gerando os mesmos valores) tanto para a linguagem C quanto para Python, então forneceremos uma função muito simples para simular a geração pseudo-aleatória.

Desse modo, pegue o código fornecido com as variáveis globais (CPA_NUM1, CPA_NUM1, CPA_MOD e _PROXIMO_INTERNO) e as funções (_define_semente(.), _proximo_pseudo_lim(.) e _inicia()), insirando-os no VPL para começar o seu programa.

Considerando qualquer valor inteiro k, invocar _proximo_pseudo_lim(k), devolverá o resto da divisão inteira do próximo valor pseudo-aleatório por k. Para simplificar usaremos sempre k=20.

Assim, supondo que a sequência pseudo-aleatória é dada pelo S acima, se usarmos como semente o elemento x2, usando _define_semente(x2), ao invocar a função _proximo_pseudo_lim(k) obteremos x3%k e na próxima chamada x4%k e assim por diante.
