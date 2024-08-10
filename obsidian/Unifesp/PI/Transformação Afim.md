~~Laboratório 02~~

~~Implementação de Transformação Afim~~

~~Escreva um programa em C++ ou Python, utilizando a biblioteca do openCV. Ele deve~~
~~receber como entrada um arquivo contendo uma imagem e também um arquivo contendo uma matriz de transformada afim, conforme dado nos exemplos.~~

~~O programa deve abrir a imagem e exibí-la. Depois deve ler o conteúdo da matriz afim,~~
~~exibir seu conteúdo e deve calcular a transformada afim dessa imagem.~~
~~Por fim, o programa deve exibir a imagem transformada.~~
Obs.:
1. Vocês devem implementar a transformada inversa (veja as notas de aula).
2. Para cada transformação afim, apenas uma matriz de transformação deve ser aplicada,
contendo a combinação correspondente das transformações solicitadas.
3. O tamanho da imagem final deve ser igual ao da imagem original. (veja o código dado)
4. As imagens de entrada e transformada devem ter o mesmo ponto de origem em 0,0. Isso
quer dizer que após uma translação maior ou igual a um pixel, a imagem transformada deve
apresentar o conteúdo da imagem original deslocado.
~~Se for entregar o projeto em C++, envie em um pacote compactado de arquivos (.zip, .rar, ou~~
~~.tar.gz) os seguintes arquivos: a sua implementação (.cpp) e os arquivos de teste (.txt) contendo~~
~~transformações.~~
Se a entrega for em python, envie o notebook com todas as implementações e
transformações.
As seguintes transformações devem ser implementadas e enviadas:
a. um exemplo de rotação em torno do centro da imagem, seguida de redução de escala;
b. um exemplo de cizalhamento seguido de translação, seguido de rotação;
c. um exemplo rotação em torno do centro da imagem, seguida de aumento de escala.
Os parâmetros de cada transformação podem ser escolhidos por vocês, desde que haja uma
parte da imagem final ainda visível dentro do campo visual da imagem final.