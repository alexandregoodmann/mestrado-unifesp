Buscar artigos
Teses na base capes
Compreender os processos de análise da Imagem
As partes técnicas do processamento da imagem (convolução, filtragem, outras)
Gradiente
Buscar laboratório em Porto Alegre

--------------
#### Processo de contagem das células

**Preparação**
- Gerar imagem com um spermatosoide para usar em todo processo, posteriormente a imagem do microscópio
	- #redimensionada = img[::2, ::2]
- Pegar uma cabeça de espermatosoide e obter um tamanho de exemplo (depois será usado uma margem de erro).
- Obter a intensidade média de uma cabeça de espermatosoide de duas maneiras. Uma usando imagem GrayScale e outra usando Imagem Binária

**Processo de contagem**
- Abrir imagem colorida
- Converter para GrayScale
- Marcar zona de filtragem (ação manual)
- Filtrar imagem GrayScale com base na média de intensidade da zona marcada


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
	