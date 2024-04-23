Um teste de normalidade de dados ***é uma análise estatística realizada para determinar se uma determinada amostra de dados segue uma distribuição normal, também conhecida como distribuição gaussiana***. A distribuição normal é caracterizada por uma forma de sino, onde a maioria dos dados está centralizada em torno da média, com uma dispersão simétrica em relação a essa média.

Existem vários métodos para testar a normalidade dos dados, sendo o teste de Shapiro-Wilk e o teste de Kolmogorov-Smirnov exemplos comuns. Esses testes geram estatísticas que podem ser comparadas a valores críticos ou p-valores para determinar se os dados podem ser considerados como provenientes de uma distribuição normal. Se os dados passarem no teste de normalidade, isso sugere que a distribuição dos dados é aproximadamente normal, o que permite o uso de técnicas estatísticas paramétricas. Se os dados não passarem no teste de normalidade, técnicas estatísticas não paramétricas podem ser mais apropriadas.

-----------------------------------------------------------
## A técnica de D'Agostino 

é uma abordagem estatística utilizada para testar a normalidade dos dados. É chamada assim em homenagem a Ralph D'Agostino Sr., um estatístico conhecido por seu trabalho em métodos estatísticos e epidemiologia.

O teste de D'Agostino avalia se uma amostra de dados segue uma distribuição normal, com base em estatísticas descritivas dos dados, especificamente a assimetria (skewness) e a curtose (kurtosis) da distribuição. Essas estatísticas fornecem informações sobre a forma da distribuição dos dados.

O teste de D'Agostino é uma técnica paramétrica e utiliza as seguintes hipóteses:

- Hipótese nula (H0): Os dados seguem uma distribuição normal.
- Hipótese alternativa (H1): Os dados não seguem uma distribuição normal.

O teste calcula uma estatística de teste com base nas estatísticas de assimetria e curtose, e compara esse valor a uma distribuição de referência conhecida para determinar se os dados podem ser considerados normalmente distribuídos. A estatística de teste segue aproximadamente uma distribuição qui-quadrado.

Assim como outros testes de normalidade, o resultado do teste de D'Agostino é frequentemente interpretado em termos de um valor p. Um valor p menor que um determinado nível de significância (como 0,05) geralmente leva à rejeição da hipótese nula, sugerindo que os dados não seguem uma distribuição normal.

É importante notar que nenhum teste de normalidade é perfeito e os resultados devem ser interpretados com cautela, especialmente com amostras pequenas. Além disso, a violação da normalidade não necessariamente invalida completamente a análise estatística, mas pode influenciar a interpretação dos resultados.

--------------------

## O teste de D'Agostino-Pearson 

é uma técnica estatística utilizada para testar a normalidade dos dados. Este teste é uma versão modificada do teste de D'Agostino, que utiliza estatísticas de assimetria e curtose para avaliar se uma amostra de dados segue uma distribuição normal.

O teste de D'Agostino-Pearson é baseado nas seguintes etapas:

1. **Calcular as estatísticas de assimetria e curtose:** Primeiramente, são calculadas a assimetria (skewness) e a curtose (kurtosis) da distribuição dos dados. A assimetria mede a falta de simetria na distribuição dos dados em relação à média, enquanto a curtose mede a forma da distribuição em relação à sua forma normal (a forma do pico e a largura das caudas).
    
2. **Calculando a estatística de teste:** Com base nas estatísticas de assimetria e curtose calculadas, uma estatística de teste é calculada. Esta estatística segue aproximadamente uma distribuição qui-quadrado.
    
3. **Comparação com um valor crítico ou p-valor:** A estatística de teste calculada é então comparada com um valor crítico da distribuição qui-quadrado, ou um p-valor é calculado para determinar a significância estatística. Se a estatística de teste exceder o valor crítico ou se o p-valor for menor que um nível de significância previamente definido (como 0,05), então a hipótese nula (de que os dados seguem uma distribuição normal) é rejeitada.
    

O teste de D'Agostino-Pearson é uma ferramenta útil para avaliar a normalidade dos dados antes de realizar análises estatísticas paramétricas que pressupõem a normalidade dos dados. No entanto, assim como qualquer teste estatístico, é importante considerar as limitações e interpretar os resultados com cautela, especialmente em amostras pequenas.

-----------------

## A técnica de Lilliefors

é um teste estatístico utilizado para verificar a normalidade de uma amostra de dados. É uma variação do teste de Kolmogorov-Smirnov (KS), desenvolvido especificamente para amostras pequenas.

Enquanto o teste de Kolmogorov-Smirnov padrão é mais apropriado para amostras grandes (geralmente mais de 50 observações), o teste de Lilliefors é útil quando se lida com amostras menores.

O processo do teste de Lilliefors é semelhante ao do teste de Kolmogorov-Smirnov:

1. **Cálculo da estatística de teste (D):** O teste calcula a maior diferença absoluta entre a função de distribuição acumulada empírica (ECDF) da amostra de dados e a função de distribuição acumulada teórica (normalmente a distribuição normal padrão). Essa diferença é a estatística de teste D.
    
2. **Determinação do valor crítico ou p-valor:** Com a estatística de teste D calculada, ela é comparada com uma tabela de valores críticos ou é convertida em um p-valor. Se a estatística de teste exceder o valor crítico ou se o p-valor for menor que um nível de significância pré-definido (como 0,05), a hipótese nula de que os dados seguem uma distribuição normal é rejeitada, indicando que os dados não são normalmente distribuídos.
    

O teste de Lilliefors é especialmente útil quando a média e o desvio padrão da população não são conhecidos e precisam ser estimados a partir da amostra. No entanto, é importante notar que o teste de Lilliefors é sensível ao tamanho da amostra e pode não ser tão poderoso quanto o teste de Kolmogorov-Smirnov em amostras maiores.

Como acontece com todos os testes de normalidade, é crucial interpretar os resultados com cautela, especialmente em amostras pequenas, e considerar outros aspectos do conjunto de dados além do resultado do teste de normalidade.

--------------------

## O teste de Shapiro-Wilk 

é um teste estatístico utilizado para avaliar se uma amostra de dados segue uma distribuição normal. Ele é especialmente adequado para amostras de tamanho moderado a grande (geralmente até algumas milhares de observações).

Aqui está uma visão geral do processo do teste de Shapiro-Wilk:

1. **Formulação de hipóteses:** O teste de [[Shapiro-Wilk]] é um teste de hipóteses. A hipótese nula (H0) é que os dados são provenientes de uma distribuição normal. A hipótese alternativa (H1) é que os dados não são provenientes de uma distribuição normal.

2. **Cálculo da estatística de teste:** O teste de Shapiro-Wilk calcula uma estatística de teste, W, com base nas diferenças entre os valores observados e os valores esperados de uma distribuição normal para a amostra dada.

3. **Comparação com valores críticos ou cálculo do p-valor:** A estatística de teste W é comparada com valores críticos tabelados ou é convertida em um p-valor. Se o valor da estatística de teste for menor do que o valor crítico correspondente ou se o p-valor for menor do que um nível de significância pré-determinado (como 0,05), então a hipótese nula de que os dados são provenientes de uma distribuição normal é rejeitada, indicando que os dados não são normalmente distribuídos.

O teste de Shapiro-Wilk é amplamente utilizado devido à sua robustez e capacidade de detectar até mesmo pequenas desvios da normalidade. No entanto, ele pode ser menos potente em amostras muito grandes. Além disso, é importante lembrar que nenhum teste de normalidade é perfeito, e os resultados devem ser interpretados com cuidado, especialmente em amostras pequenas ou em conjuntos de dados que podem ser afetados por outros fatores além da distribuição subjacente dos dados.

---------------

## Bibliografia

1. ~~**"An Introduction to Statistical Learning"** de Gareth James, Daniela Witten, Trevor Hastie e Robert Tibshirani. Este livro oferece uma introdução acessível aos métodos estatísticos, incluindo uma discussão sobre normalidade de dados e técnicas para avaliá-la.~~

2. ~~**"Applied Multivariate Statistical Analysis"** de Richard A. Johnson e Dean W. Wichern. Este livro aborda uma variedade de técnicas multivariadas e inclui capítulos dedicados à análise de normalidade e testes de normalidade.~~

3. ~~**"Probability and Statistics"** de Morris H. DeGroot e Mark J. Schervish. Este é um texto introdutório abrangente que cobre uma ampla gama de tópicos em probabilidade e estatística, incluindo testes de normalidade e métodos para avaliar a normalidade dos dados.~~

4. ~~**"Statistical Methods for Psychology"** de David C. Howell. Este livro é direcionado especificamente para estudantes e pesquisadores de psicologia, oferecendo uma cobertura detalhada de métodos estatísticos com foco em aplicações práticas, incluindo a análise de normalidade.~~

5. ~~**"Discovering Statistics Using R"** de Andy Field, Jeremy Miles e Zoe Field. Este livro é uma introdução prática e orientada por software ao uso do R para análise [[estatística]]. Ele inclui informações sobre testes de normalidade e técnicas para lidar com dados não normais.~~

6. ~~**"Statistical Methods in Education and Psychology"** de Gene V. Glass, Kenneth D. Hopkins e Donald B. Stamey. Este livro é uma referência clássica que aborda métodos estatísticos comuns em educação e psicologia, incluindo discussões sobre normalidade de dados e testes de normalidade.~~

Essas referências oferecem uma variedade de perspectivas e profundidades de cobertura sobre o tema da normalidade de dados, permitindo que você escolha a que melhor se adapta às suas necessidades e nível de experiência em estatística.

------------

## Ações para o seminário

- [x] Ler material de pesquisa (pdf)
- [x] Conseguir uma base de dados
- [x] Escolher uma única técnica para aplicar a validação dos dados
- [ ] Comparar as técnicas (opcional)
- [ ] Manipular os dados com python e gerar diagramas
- [ ] Apresentar os resultados
- [ ] Montar apresentação
- [ ] Objetivo: Dizer porque os dados são válidos ou não
- [ ] Apresentação: Cada dupla irá apresentar um tópico a seguir incluindo: principais conceitos,
- [ ] exemplo numérico, exemplo prático pode usar bibliotecas, referências bibliográficas.