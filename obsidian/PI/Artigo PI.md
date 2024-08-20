Buscar artigos
Buscar artigos do professor
Teses na base capes
Compreender os processos de análise da Imagem
As partes técnicas do processamento da imagem (convolução, filtragem, outras)
Gradiente
Buscar laboratório em Porto Alegre

flood fill
olhar pra cor da celula e identificar sobreposicao e focar no formato
extrair elipses hough

--------------
#### Processo de contagem das células

**Processo de contagem**
- Abrir imagem colorida
- Converter para GrayScale e reduzir tamanho pela metade
- Marcar zona de filtragem (ação manual)
- A partir da zona filtrada pegar min e max, varrer a imagem e remover ruido do fundo (poderia usar convolucao?)
- Convert a imagem para binario
- Ajustar Parâmetros
	- Filtrar Fundo:
	- Tamanho de Células:
		- As células possuem um tamanho mínimo e máximo. Foi criado uma imagem com uma amostra de celulas individuais, não agrupadas. Com a ciência do número de células, fez-se um histograma da área das células. Decidindo um tamanho mínimo e máximo. Para os grupos de células. Logo, para os grupos de células, divide-se o tamanho do grupo pelo menor tamanho de células, para se obter um número aproximado de células em cada grupo.
- Conta as celulas (aqui é um tópico a parte para explicar como se faz isso)
	- Neste momento considera-se a imagem com células individuais, agrupadas e ruídos (pequenas marcas pretas)
	- Algorítimo
		- Cria uma lista vazia de marcados
		- Encontra o primeiro pixel preto e adiciona na lista
		- Para o primeiro pixel, faz convolução e adiciona à lista os vizinhos sem intensidade
		- Faz os dois passos anteriores enquanto houver pixel na lista, senão continua a varrer a imagem
		- Com estas técnicas foi possível objter 97% de acertos no número de células
			

Parametros de entrada
filename
reduzir - porcentamgem que vai reduzir

**Preparação**
- Gerar imagem com um spermatosoide para usar em todo processo, posteriormente a imagem do microscópio
	- #redimensionada = img[::2, ::2]
- Pegar uma cabeça de espermatosoide e obter um tamanho de exemplo (depois será usado uma margem de erro).
- Obter a intensidade média de uma cabeça de espermatosoide de duas maneiras. Uma usando imagem GrayScale e outra usando Imagem Binária

---------------
### An efficient method for automatic morphological abnormality detection from human sperm images
https://www.sciencedirect.com/science/article/abs/pii/S0169260715002230
#### Methods
The SMA method was used to detect and analyze different parts of the human sperm. First of all, ==SMA removes the image noises and enhances the contrast of the image to a great extent. Then it recognizes the different parts of sperm (e.g., head, tail) and analyzes the size and shape of each part.== Finally, the algorithm classifies each sperm as normal or abnormal. Malformations in the head, midpiece, and tail of a sperm, can be detected by the SMA method. In contrast to other similar methods, the SMA method can work with low resolution and non-stained images. Furthermore, an image collection created for the SMA, has also been described in this study. This benchmark consists of 1457 sperm images from 235 patients, and is known as human sperm morphology analysis dataset (HSMA-DS).
__________________________
### Automatic detection and segmentation of sperm head, acrosome and nucleus in microscopic images of human semen smears
https://www.sciencedirect.com/science/article/abs/pii/S0169260716304023
#### Methods
==After an initial thresholding step, the histogram of the Hue channel of HSV color space is used, in addition to size criterion, to discriminate sperm heads in microscopic images.== To achieve an improved segmentation of sperm heads, an edge-based [active contour](https://www.sciencedirect.com/topics/computer-science/active-contour "Learn more about active contour from ScienceDirect's AI-generated Topic Pages") method is used. Also a novel tail point detection method is proposed to refine the segmentation by locating and removing the midpiece from the segmented head. An algorithm is also proposed to separate the acrosome and nucleus using morphological operations. Dice coefficient is used to evaluate the segmentation performance. The proposed methods are evaluated using a publicly available dataset.

______________

### Estudar
- [ ] Remover ruído
- [ ] Tamanho da celula
- [ ] Célula clara
- [ ] Célula escura
- [ ] Detecção de borda
- [ ] Filtros (passa baixa, passa alta, outros)

------------

## Introdução

A contagem de células espermáticas é uma prática essencial na avaliação da fertilidade masculina e na pesquisa reprodutiva. Os espermatozoides são as células sexuais masculinas responsáveis pela fertilização do óvulo feminino, desempenhando um papel crucial na reprodução humana. A análise quantitativa e qualitativa dessas células fornece informações valiosas sobre a saúde reprodutiva de um indivíduo, ajudando a diagnosticar possíveis causas de infertilidade e a monitorar a eficácia de tratamentos. Este artigo explora as técnicas e métodos utilizados na contagem de células espermáticas, bem como a importância dessa prática na medicina reprodutiva. A contagem precisa de espermatozoides, aliada à avaliação de parâmetros como motilidade, morfologia e viabilidade, é fundamental para uma compreensão abrangente da saúde reprodutiva masculina e para o desenvolvimento de intervenções terapêuticas eficazes.

## Introdução

A contagem de células espermáticas é uma prática essencial na avaliação da fertilidade masculina e na pesquisa reprodutiva. Os espermatozoides são as células sexuais masculinas responsáveis pela fertilização do óvulo feminino, desempenhando um papel crucial na reprodução humana. A análise quantitativa e qualitativa dessas células fornece informações valiosas sobre a saúde reprodutiva de um indivíduo, ajudando a diagnosticar possíveis causas de infertilidade e a monitorar a eficácia de tratamentos.

Nos últimos anos, o processamento de imagem emergiu como uma ferramenta poderosa para a contagem de células em diversas áreas da biologia e medicina, incluindo a análise de espermatozoides. A utilização de técnicas avançadas de processamento de imagem permite uma contagem mais precisa e eficiente, reduzindo a subjetividade e o tempo necessário para a análise manual. Este artigo explora as técnicas e métodos utilizados na contagem de células espermáticas, com ênfase nas abordagens de processamento de imagem e sua importância na medicina reprodutiva. A combinação de algoritmos de processamento de imagem com tecnologias de microscopia moderna proporciona uma compreensão mais detalhada dos parâmetros espermáticos, como motilidade, morfologia e viabilidade, contribuindo para avanços significativos no diagnóstico e tratamento da infertilidade masculina.

## Introdução

A contagem de células espermáticas é uma prática essencial na avaliação da fertilidade masculina e na pesquisa reprodutiva. Os espermatozoides são as células sexuais masculinas responsáveis pela fertilização do óvulo feminino, desempenhando um papel crucial na reprodução humana. A análise quantitativa e qualitativa dessas células fornece informações valiosas sobre a saúde reprodutiva de um indivíduo, ajudando a diagnosticar possíveis causas de infertilidade e a monitorar a eficácia de tratamentos.

Nos últimos anos, o processamento de imagem emergiu como uma ferramenta poderosa para a contagem de células em diversas áreas da biologia e medicina, incluindo a análise de espermatozoides. A utilização de técnicas avançadas de processamento de imagem permite uma contagem mais precisa e eficiente, reduzindo a subjetividade e o tempo necessário para a análise manual.

### Métodos Diferentes de Contagem de Células

A contagem de células pode ser realizada por uma variedade de métodos, cada um com suas vantagens e desvantagens. Entre os métodos mais comuns estão:

1. **Contagem Manual com Hemocitômetro:**
   - **Descrição:** Este método tradicional utiliza uma câmara de contagem (hemocitômetro) e um microscópio. Os espermatozoides são contados manualmente em uma grade conhecida.
   - **Vantagens:** Simples e de baixo custo, permite a observação direta das células.
   - **Desvantagens:** Pode ser demorado, subjetivo e propenso a erros humanos.

2. **Espectrofotometria:**
   - **Descrição:** A densidade óptica de uma amostra de esperma é medida, e a concentração de células é inferida a partir dessas medições.
   - **Vantagens:** Rápido e fácil de usar para amostras de grande volume.
   - **Desvantagens:** Menos preciso para amostras com baixa concentração de células e não fornece informações sobre a motilidade ou morfologia.

3. **Citometria de Fluxo:**
   - **Descrição:** As células são suspensas em um fluxo de fluido e passam por um laser, que mede várias características físicas e químicas.
   - **Vantagens:** Alta precisão e pode analisar um grande número de células rapidamente.
   - **Desvantagens:** Equipamento caro e requer treinamento especializado.

4. **Análise por Computador/Processamento de Imagem:**
   - **Descrição:** Utiliza software de análise de imagem para automatizar a contagem de células a partir de imagens digitais.
   - **Vantagens:** Alta precisão, reduz a subjetividade e pode fornecer informações adicionais sobre morfologia e motilidade.
   - **Desvantagens:** Requer software especializado e pode ser caro.

5. **Métodos de Imunofluorescência:**
   - **Descrição:** Utiliza anticorpos marcados com fluorescência que se ligam especificamente aos espermatozoides, permitindo a contagem sob um microscópio de fluorescência.
   - **Vantagens:** Alta especificidade e sensibilidade.
   - **Disvantagens:** Custo elevado e necessidade de anticorpos específicos.

### Considerações Finais

A escolha do método de contagem de células espermáticas depende de vários fatores, incluindo a precisão necessária, o volume de amostras, os recursos disponíveis e o nível de detalhe desejado na análise. O avanço das técnicas de processamento de imagem e a automação têm melhorado significativamente a precisão e a eficiência dessas contagens, proporcionando uma compreensão mais detalhada da saúde reprodutiva masculina e facilitando diagnósticos mais precisos e tratamentos mais eficazes para a infertilidade.