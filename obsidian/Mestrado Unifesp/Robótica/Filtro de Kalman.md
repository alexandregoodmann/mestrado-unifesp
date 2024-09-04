O filtro de Kalman é um algoritmo utilizado para estimar o estado de um sistema dinâmico ao longo do tempo, mesmo quando as medições feitas estão imprecisas ou ruidosas. Ele é amplamente usado em áreas como robótica, navegação, controle de sistemas e processamento de sinais. 

Aqui está uma visão geral de como o filtro de Kalman funciona:

1. **Modelo de Estado**: O sistema é modelado por um conjunto de equações diferenciais ou de diferença que descrevem como o estado do sistema evolui ao longo do tempo. Este modelo inclui a matriz de transição de estado \(A\), que prediz o estado atual com base no estado anterior, e a matriz de controle \(B\), que representa o efeito dos comandos de controle aplicados ao sistema.

2. **Modelo de Medição**: O sistema também inclui um modelo que relaciona o estado real do sistema com as medições que podem ser feitas. Isso é representado pela matriz de medição \(H\).

3. **Predição**: Com base no modelo de estado, o filtro de Kalman faz uma predição do estado futuro do sistema e da incerteza associada a essa predição. Esta etapa utiliza a matriz de transição de estado \(A\) e a matriz de controle \(B\), além de considerar o ruído do processo \(Q\).

4. **Atualização**: Quando uma nova medição é feita, o filtro de Kalman atualiza sua estimativa do estado do sistema com base nessa nova medição. Esta etapa utiliza a matriz de medição \(H\), a medição atual, e o ruído de medição \(R\).

5. **Ganho de Kalman**: O filtro de Kalman calcula um ganho ótimo, chamado ganho de Kalman \(K\), que determina o quanto a estimativa deve ser ajustada com base na nova medição. 

As equações básicas do filtro de Kalman são:

- **Predição do estado**:
  \[
  \hat{x}_{k|k-1} = A \hat{x}_{k-1|k-1} + B u_k
  \]
  
- **Predição da covariância do erro**:
  \[
  P_{k|k-1} = A P_{k-1|k-1} A^T + Q
  \]

- **Atualização do ganho de Kalman**:
  \[
  K_k = P_{k|k-1} H^T (H P_{k|k-1} H^T + R)^{-1}
  \]

- **Atualização do estado**:
  \[
  \hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k (z_k - H \hat{x}_{k|k-1})
  \]

- **Atualização da covariância do erro**:
  \[
  P_{k|k} = (I - K_k H) P_{k|k-1}
  \]

Onde:
- \(\hat{x}_{k|k-1}\) é a predição do estado no tempo \(k\) com base nas informações até o tempo \(k-1\).
- \(P_{k|k-1}\) é a predição da covariância do erro.
- \(K_k\) é o ganho de Kalman.
- \(\hat{x}_{k|k}\) é a estimativa atualizada do estado.
- \(P_{k|k}\) é a covariância do erro atualizada.
- \(z_k\) é a medição atual.
- \(Q\) é a covariância do ruído do processo.
- \(R\) é a covariância do ruído da medição.
- \(u_k\) é o vetor de controle.

O filtro de Kalman é poderoso porque é capaz de integrar medições ruidosas e prévias incertas de maneira otimizada, resultando em uma estimativa mais precisa do estado do sistema ao longo do tempo.