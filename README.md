# P1_SCAV_VIDEO
Pràctica1_VIDEO

Aquest document detalla el conjunt d'exercicis de la Pràctica 1 de la part de vídeo de SCAV.

**Exercici 1.**

Aquest exercici conté l'script *rgb_yuv.py* que consta de dues funcions una que passa de l'espai de color RGB a YUV i l'altre l'inversa. Al mateix script hi ha una petit main que invoca les funcions.

**Exercici 2.**

La línia de comando que hem utilitzat del ffmpeg per fer el resize de la imatge de Lenna.png és el següent:

*ffmpeg -i Lenna.png -vf scale=320:-1 Lenna_320.png*

A continuació podem observar el resultat al terminal:

![ScreenShot E2](https://github.com/paumonterop/P1_SCAV_VIDEO/tree/main/Imatges/E2_resize_Lenna.png?raw=true "ScreenShot E2")

A continuació també podem veure alguns exemple de la imatge Lenna.png rescala a varies resolucions inferiors a la original:

![Lenna 320x320](https://github.com/paumonterop/P1_SCAV_VIDEO/tree/main/Imatges/Lenna_320.png?raw=true)
![Lenna 240x240](https://github.com/paumonterop/P1_SCAV_VIDEO/tree/main/Imatges/Lenna_3240.png?raw=true)
![Lenna 120x120](https://github.com/paumonterop/P1_SCAV_VIDEO/tree/main/Imatges/Lenna_120.png?raw=true)

**Exercici 3.**

Per convertir la imatge Lenna.png a blanc i negre. Hem utilitzat el comando ffmpeg següent:

*ffmpeg -i Lenna.png -f lavfi -i color=gray:s=512x512 -f lavfi -i color=black:s=512x512 -f lavfi -i color=white:s=512x512 -filter_complex threshold Lenna_b_and_w.png*

 continuació podem observar el resultat al terminal:

![ScreenShot E3](https://github.com/paumonterop/P1_SCAV_VIDEO/tree/main/Imatges/E3_bw_Lenna.png?raw=true)

A continuació podem observar l'imatge resultant:

![Lenna b/w](https://github.com/paumonterop/P1_SCAV_VIDEO/tree/main/Imatges/Lenna_b_and_w.png?raw=true)

**Exercici 4.**

Aquest exercici conté l'script *run_length_function.py* que conte la funció per codificar a Run-Length Encoding una serie de bytes.
el fitxer conté un petit main al final que invoca la funció.

**Exercici 5.**

l'script d'aquest últim exercici: *DCT_encoder.py* converteix la imatge Lenna.jpg a DCT i l'inversa. 

![Lenna DCT Output](https://github.com/paumonterop/P1_SCAV_VIDEO/tree/main/Imatges/output_Lenna.jpg?raw=true)
