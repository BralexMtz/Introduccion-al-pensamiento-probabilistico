# Introduccion-al-pensamiento-probabilistico
curso de introduccion al pensamiento probabilistico de PLATZI 
## TEOREMA DE BAYES
```
         P(A) P(B|A)
 P(A|B)= ----------
           P(B)
```
Probabilidad de A (Hipotesis) dado B (evidencia)


# Mentiras estadisticas

## Garbage in, garbage out (GIGO)
Son como un tercer nivel de errores donde tenemos
- 1 Errores de sintaxis
- 2 Errores de lógica
- 3 Errores de (diseño y modelado del programa)

GIGO solo nos dice que si la calidad de nuestros datos es igual de fundamental que la precisión de nuestros computos

En otras palabras con datos errados las conclusiones serán erradas.


#### *Ejemplo*
> Los censos en su principio tenian muchisimos errores, y uno de los errores mas importantes es que se llego a la conclusión de que una persona de color que era libre tenian 10% más probabilidad de volverse locos que los esclavos. Sin embargo esto no era cierto, debido a que los censos eran incorrectos.

#### *Otro ejemplo* aporte de Juan Moreno

> Una historia común sobre muestreo es el caso de los aviones aliados en la Segunda Guerra Mundial. Lo que pasó era que veían que los aviones de combate que regresaban, usualmente tenían muchas averías e impacto de proyectiles en las alas y otras áreas. Lo que pensó la RAF fue observar donde estaban los huecos, hacer un analisis de las zonas más afectadas en sus aviones y empezar a mandar los aviones reforzados en esas zonas. ¿El problema? su muestra eran aviones que sí regresaban de combate, por lo que Abraham Wald les hizo ver que si los aviones regresaban con huecos en esas partes, era porque en esas partes los impactos no eran letales y al contrario de lo que decían los datos, había que reforzar las  partes del avión que no habian sido afectadas.

## Imagenes engañosas
Un error o metodo de engaño es:
>Extrapolar las conclusiones erroneas despues de ver una imagen.

- Cuando se juega con la escala de la grafica se puede llegar a conclusiones incorrectas.

![Escalas engañosas.- La primera grafica empieza en 400](./img/escalas_erroneas.jpg)

Podemos ver que nos da una perspectiva distinta al comparar con una escala adecuada.

- **Nunca debes confiar en una gráfica sin etiquetas.**


## Cum Hoc Ergo Propter Hoc (*latin*)
Lo primero que necesitamos entender es que la correlacion entre dos variables sólo significa que ambas se mueven en el mismo sentido cuando se trata de una correlacion *positivo* o *negativa* cuando se mueven en direcciones opuestas. Pero recuerda
> Correlación no implica causalidad

La frase en latín *Cum Hoc Ergo Propter Hoc* en español significa:

*Despues de esto, eso; Entonces a consecuencia de esto, eso.*

Pero no te cases con una sola causa, piensa ***out of the box***, imagina que otras causas pueden hacer que suceda cierto hecho, para no caer en conclusiones erroneas.

![Ejemplo de Correlacion sin causalidad](https://pbs.twimg.com/media/EDFyOM6XsAAsQUp.jpg)

 
## El prejuicio del muestreo
Aspectos importantes que seguir para el muestreo.
 - Para que un muestreo pueda servir como base para la inferencia estadistica tiene que ser:
   - **Aleatorio**
   - **Representativo.**
 - El prejuicio en el muestreo elimina la representatividad de las muestras.
 - A veces conseguir muestras es difícil, por lo que se utiliza a la población de más fácil acceso (caso estudios universitarios)

*Ejemplo*

> La mayoria piensa que los primeros seres humanos en la era de la prehistoria, siempre vivian en cavernas. Sin embargo esto no es totalmente cierto ya que no todos vivían en cavernas, sin embargo es lo que encontramos en las cuevas lo que nos ayudó a entender a esta civilización. 
Asi que podemos decir que la muestra era posiblemente aleatoria pero no era representativa.


*El error de muestreo provoca que los resultados o conclusiones puedan estar sesgados.*

## Falacia del francotirador de Texas

Esta falacia se da cuando no se toma la aletoriedad en consideración
- También sucede cuando uno se enfoca en la similitudes e ignora las diferencias
- Cuando fallamos al empezar a recolectar datos antes de generar una hipotesis estamos en alto riesgo de caer en esta falacia (muy común en Data Science)

![Falacia del francotirador](./img/Falacia_Franco.jpg)

La falacia del francotirador consiste en primero disparar y posteriormente pintar los blancos.

En otro contexto podemos decir que empezamos a obtener las muestras y despues la hipotesis se adapta a los datos recolectados, lo cual no debería ser así.

*Ejemplo*

Cuando ignoramos parte de los datos, como por ejemplo enfocarnos unicamente en las veces que le fue bien a un emprendedor e ignorar las veces que le fue mal y concluir que es un gran emprendedor porque a una le fue bien.

Evita caer en el error de ver primero los datos y concluir algo al respecto, en lugar de generar una hipotesis, recolectar muestras de manera aleatoria y representativa para posteriormente concluir adecuadamente.

## Porcentajes confusos

La mentira a través de los porcentajes puede suceder cuando:

- No sabemos la cuenta total de la cual se obtiene un porcentaje.
- No tenemos un contexto claro
- Existen porcentajes en vacío

*Ejemplo*

> ¿Cual escuela tuvo el mejor desempeño global?
> - Escuela A - incremento su rendimiento en 25%
> - Escuela B - incremento su rendimiento en 10%
> - Escuela C - incremento su rendimiento en 5% 


Ahora con contexto, ¿Cual escuela realmente alcanzó un mejor desempeño?.

|  | Rendimiento 2018 | Rendimiento 2019 | Incremento  | Incremento porcentaje |
| :---         | :---:      |  :---: |:---:      |  :---: |
| Escuela A   | 20     |  25    | 5 | 25% |
| Escuela B   | 50   | 55  | 5 | 10 % |
| Escuela C   | 95   | 100  | 5 | 5 % |

Ejemplo 2
> **¡La excusa del borracho que maneja!**
Argumentando que estadísticamente es más probable que choque si va sobrio a que si va borracho. ya que el 70% de los accidentes son por personas sobrias y el 30% por personas borrachas.


## Falacia de regresión

Esta falacia sucede cuando atribuimos efectos de causalidad a eventos que simplemente suceden por regresión a la media. 

*Ejemplo*

>Como cuando un deportista tiene su peor racha en la liga y el entrenador lo regaña o castiga para que mejore, posteriormente el deportista ya no la riega tan feo. Sin embargo esto sucede porque tiende a la media, a su juego normal, no porque el entrenador haya aplicado la medida correcta.

Esta falacia ocurre unicamente  cuando los eventos fluctuan 

# INTRODUCCION A MACHINE LEARNING

¿Que es?

> Es el campo de estudio que le da a las computadoras la habilidad de aprender sin ser explícitamente programadas.
> - Artur Samuel, 1959

Machine Learning no es TERMINATOR. Son algoritmos que se utilizan principalmente en la detección de patrones.


Todo comienza con el **TEOREMA DE BAYES**.
Nos enseña como incorporar la evidencia y los datos que obtenemos del mundo real de una forma cada vez más correctas.

![Teorema de bayes](https://miro.medium.com/max/3200/1*as2DnWuAUVLSZpS6MvPZxw.png)


*Posteriormente*, Alan Turing nos otorgó una forma de ver a los algoritmos como el mismo algoritmo (**maquinas de turing**), dando la base de las computadoras modernas. Sino tambien las bases para que las computadoras pudieran aprender.

![Alan Turing](https://ba994713-a-62cb3a1a-s-sites.googlegroups.com/site/bionicagalandeblasdesign/personajes/alan-turing-1/Alan-Turing-el-hombre-que-enseno-a-pensar-a-las-maquinas.jpg?attachauth=ANoY7cq-h5HWjHeogFZVfAHxv0b3Il5jo_n210OgHVcR2GusgOf0tbxmSy_3SkXLOs6DiVB-u0LzUHy6cRAZX-VbxN9-yK5Z1HdsV_sUfXJJ3TyhWceukfeD8wXDu-q7Z0MtcTUx01ittzGEzfT04hdI32CmLaz69Pue0x66sjdIXBoLTI6ldjKd4EiApcf_fQbkTvVJ93UM4f7E9bNmj-0q3aNB3nQkuaHzvijGUO-yV7ybqtbREjt1FoqHUsHA1IecfYHT3FQmWrChJg43f9zeJ_7vETRO9BFvvfNyWM7_I9Sx9WuZ6wtvfkYAcp1ERiVU7aIst9gIjyHWdJ2_P9gJuhurDPfutw%3D%3D&attredirects=0)

*Años despues* llega Marvin Minsky, quien logra crear la **primera red neuronal**, cuando en el año de 1951 las computadoras ocupaban cuartos completos con memoria super limitada. Sin embargo ya era demostrable que las computadoras pudieran aprender.

![Marvin Minsky](https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2016/01/26/14538401873730.jpg)

Y en *1952* Arthur Samuel genera el **primer programa que sabe jugar damas chinas**, y lo genera calculando los siguientes movimientos. Este programa nos permitio entender que aprender desde una perspectiva humana era:
- Memorizar
- Generalizar

Por lo que los algoritmos basicamente recuerdan lo que han visto y en otras ocasiones generalizan esta información.

![Arthur Samuel](https://i.blogs.es/589df8/650_1000_us__en_us__ibm100__700_series__checkers__620x350/450_1000.jpg)

En *1957* Frank Rosenblatt **inventa el perceptron**, que podía reconocer digitos escritos a mano y convertirlos en una representación computacional.

![Frank Rosenblatt](https://news.cornell.edu/sites/default/files/styles/story_thumbnail_xlarge/public/2019-09/0925_rosenblatt_main.jpg?itok=SE0aS7ds)

*En 1963 Donald Michie* crea la **primera red adversarial** que permite que las computadoras puedan jugar constantemente para entender como automatizar las reglas de un juego. TIC TAC TOE

![Donald Michie](https://farm1.static.flickr.com/197/519305676_4b8adcd997.jpg?v=0)

*En 1969 Marvin Minsky* escribe el **libro de perceptron** donde se recolecta toda la investigación relacionada con redes neuronales. Deteniendo la investigación en inteligencia artificial por casi 20 años al pensarse que no podía llegar a desarrollarse más.

![Libro Perceptrons](https://images-na.ssl-images-amazon.com/images/I/71QXEPrw3YL.jpg)


*En el año 1997* fue el año en que la computadora Deep Blue de IBM derrota al actual campeón de ajedrez del mundo, Gary Kaspárov. Que marcó el pasó hacia la inteligencia artificial moderna.

![Derrota Kasparov](https://www.imer.mx/wp-content/uploads/sites/36/11may_garykasparov_twitter.jpg)

*En el 1998* se libera el dataset mnist, que aún hoy en día se sigue utilizando como el hello world de machine learning, ya que se toma este dataset con muchisimos digitos escritos a mano junto con las etiquetas de estos digitos, de tal forma que se pudieran potencializar los algoritmos que cada vez podían utilizar computo de mayor y mayor escala, aprovechando la Ley de Moore.

![MINST](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)


*En 2009* Fei Fei Li una investigadora de estanford libero el dataset imagenet, una de las más grandes contribuidoras en el campo de la inteligencia artificial y que lideró la inteligencia artificial dentro de google. A partir de su liberación la inteligencia artificial mejoró y crecio el campo en esta areá para lograr muchas de las cosas que vemos hoy en día.

![Fei fei Li](https://cms.qz.com/wp-content/uploads/2017/07/ap_318979552057.jpg?quality=75&strip=all&w=1200&h=900&crop=1)

*En el año 2011* la computadora Watson de IBM que jugaba Jeopardy, derrotó a dos de los más grandes jugadores utilizando, redes neuronales, reconocimiento de patrones y retrieval de información( acceso a la información de manera muy rapida). Demostrando que las computadoras, aún en juegos muy abstractos podían derrotar a los grandes campeones del mundo.

![jeopardy vs watson](https://i.ytimg.com/vi/P18EdAKuC1U/maxresdefault.jpg)


*En el año 2012* youtube tenía gran cantidad de videos en su información, Google lográ procesar con toda su infraestructura toda la data para encontrar gatos en los videos.
*En el 2014* implemento su algoritmo de reconocimiento facial y justamente en ese año fue cuando comenzamos a ver que podíamos etiquetar, y aún en imagenes que no nos habian etiquetado, podían detectar que nosotros apareciamos ahí.

![Facial Recognition](https://blog.phonehouse.es/wp-content/uploads/2019/01/Reconocimiento-facial.jpg)

*En el 2016* el algoritmo alpha go de google, derroto al respectivo campeon del mundo en el juego go. Uno de los juegos con más posibilidades y mayor demanda.
![alpha go](https://i.blogs.es/46009f/1366_2000/1366_2000.jpg)

Finalmente, para concluir debemos entender que Machine Learning se utiliza cuando:
- Programar un algoritmo es muy complejo o no se conocen algoritmos para resolverlo
- Ayuda a los humanos a entender patrones(data mining)

Existe: 
- Aprendizaje supervisado (etiquetado)
- Aprendizaje no supervisado
- Aprendizaje semisupervisado

Tambien existen tecnicas:
 - Batch (Se genera una vez y se aplica)
 - online learning (Se va actualizando constantemente conforme entran datos.)
