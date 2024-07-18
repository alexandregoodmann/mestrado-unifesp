
- [x] Como pegar informação do sensor (LIDAR)
- [ ] Mapeamento Grid (Técnica de Occupancy Probability Mapping ou Histograma)
- [ ] Tamanho de celula
- [x] Modelo inverso do sensor
- [x] Controle PID
- [x] Bug Algorithm

- Na medida em que o robô se move pelo ambiente para acessar
cada objetivo, o mapeamento em grid deve ser realizado e mostrado
- O mapa final deve estar coerente com o ambiente. Os valores de
tamanho de célula r e modelo inverso do sensor ε devem ser
escolhidos para um resultado satisfatório

(1) [[Controle PID]] em malha fechada (ver os exemplos)
(2) Algoritmo de Path Planning do tipo Bug Algorithm (feito na Atividade A3, pode ser o “0”, “1” ou o “2”)
(3) Realização de Mapeamento por Grid pela Técnica de Occupancy Probability Mapping ou Histograma
(1) Controle PID em malha fechada:
- O controle deve ser aplicado no Pioneer, portanto, um controle não-holonômico, que está pronto nos exemplos.
(2) [[Bug Algorithm]]
- Pode ser o mesmo algoritmo implementado na Atividade 2, qualquer tipo (0, 1 ou 2), a encargo do projetista
(3) Mapeamento
- Para facilitar, pode ser usado somente um feixe do LIDAR, de preferência o que está à frente do robô.
- O mapa em grid deve ser atualizado de forma constante durante e mostrado para o usuário
- O algoritmo para detecção das células tocadas pelo feixe do LIDAR deve ser implementado