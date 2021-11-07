<h1><b>Chess Manager</b></h1>

![](https://img.shields.io/github/languages/top/AlfonsoXIII/chess_manager)
![](https://img.shields.io/github/repo-size/AlfonsoXIII/chess_manager?color=critical)
![](https://img.shields.io/github/license/AlfonsoXIII/chess_manager?color=success)
![](https://img.shields.io/github/v/release/AlfonsoXIII/chess_manager?color=yellow&include_prereleases)
![](https://img.shields.io/github/stars/AlfonsoXIII/chess_manager?style=social)

<p style="text-align: justify">El programari que trobarà en aquest repositori pertany al <i><b>Treball de Recerca de l'alumne Sergio Mancha</b></i>, de l'<b>Institut Alexandre Satorras</b>, sobre el desenvolupament de Software i l'aplicació dels principis que formen les inteligències artificials als escacs. </p>

<p style="text-align: justify;"><i>Tots i cadascún dels arxius queden protegits sota el règim establert per la llicència MIT que trobarà en aquest mateix directori, en cas de que no s'indiqui el contrari explícitament.</i></p>

<h2><b>Software d'anàlisi</b></h2>
<p style="text-align: justify"> Una de les principals característiques que forma aquest projecte es l'entorn d'anàlisi basat en Chess Base desenvolupat. Amb una interfície simple i efectiva, la visualització de partides així com el seu anàlisi són els principals objectius d'aquest entorn.</p>

![Image from Gyazo](https://i.gyazo.com/03c656db8e00602760a2b7e26c6958f6.gif)

<p style="text-align: justify"> L'usuari tindrà a la seva dispocició un ampli ventall d'opcions per a conseguir la millor experiència possible. Controlar l'<b>historial de jugades</b>, <b>desplaçar-se sobre ell</b>, i fins i tot poder <b>esborrar i reescriure jugades</b>, d'entre altres.</p>

<img align="left" padding="10px" margin="10px" width="40%" src="https://i.gyazo.com/f8141d5cd85f6144e24f7c99b9f91a14.gif">

<p style="text-align: justify; margin-left:43%;" > A més, dins de la barra principal d'opcions trobarà un ventall de possibilitats per a <b>emmagatzemar posicions</b>, <b>carregar posicions</b>, <b>canviar de mode</b>...</p>

<p style="text-align: justify; margin-left:43%;"> En primera instànca trobem un <b>menú</b> a on l'usuari podrà visualitzar tota la informació relacionada amb la versió actual del software utilitzat, així com la data de publicació d'aquesta mateixa versió i el control del estat del mòdul d'anàlisi incorporat.</p>

<p style="text-align: justify; margin-left:43%;"> També, una sèrie de funcionalitats a través de les quals l'usuari podrà <b>importar</b> i <b> exportar</b> qualsevol posició, indpenedent ment del seu estat, en un còmode format JSON que li permetrà poder portar allà on vulgui les seves millors partides.</p>

<p style="text-align: justify; margin-left:43%;"> Així mateix, també es disposarà d'uns botons que dotaran de la plena capaçitat a l'usuari de <b>restablir la posició de treball</b>, o bé <b>canviar de mode</b> de finestra en qualsevol moment (anàlisi/joc).</p>


<p align="center"><img align="center" src="https://i.gyazo.com/c3542eca34eacf32bf2e5632f1f1e403.gif"></p>

<p align="center" width="100%">
    <img width="20%" src="https://i.gyazo.com/13cc507b8eefe2061658478445e435e6.gif">
    <img width="23%" src="https://i.gyazo.com/a15f5c77e8b67587d359e522a59ffb7a.gif">
    <img width="21%" src="https://i.gyazo.com/9a6a710b81eb65bbd489308b81dbbd8d.gif">
    <img width="21.5%" src="https://i.gyazo.com/774d2f18ca30373e079280d36b306da3.gif">
</p>

<p style="text-align: justify"> Finalment, s'acomoda un bloc dedicat a la representació de l'<b>historial de notacions</b>, en format algebraic amb caràcters unicode. Aquest incorpora un sistema de pàgines per a poder tenir una experiència no finita de moviments per a una posició, per tant: cada vegada que s'ompli el bloc mostrar en pantalla es crearà una nova pàgina la qual podrà ser ajustada des dels dos botons blaus adjunts a la zona exterior inferior dreta.</p>

<p align="center"><img align="center" src="https://i.gyazo.com/2624eb0ab4ea95018ef3db5d95b9e0c9.gif"></p>
</p>

Un darrer bloc de dimensions petites ofereix la possibilitat de poder incorporar un <b>anàlisi al moment</b> per part del prototip d'intel·ligència artificial desenvolupat. Aquest pot ser gestionat a través del seus dos botons d'encès i apagat integrats.

<h2><b>Entorn de joc integrat</b></h2>

<p style="text-align: justify"> A través del botó de canvi de mode és accesible una modalitat del software i del prototip de mòdul d'anàlisi enfocat al joc <b>humà VS màquina</b>. Aquest treballa en paral·lel al funcionament del programari principal.</p>

![Image from Gyazo](https://i.gyazo.com/e7525a29b9b845224dc62d7925cb4a59.gif)

<p style="text-align: justify"> A través d'un <b>menú adjacent</b> es pot configurar el mode de joc: sent la voluntat de colors la principal i única de les opcions disponibles. Bo i això, els botons de <b>restablir posició</b>, <b>importar posició i exportar posició</b> NO estaran disponibles per a aquest mode.</p>

<p style="text-align: justify"><i>Cal recalcar que en transitar d'un mode a un altre la posició es perdrà en cas de que no hagi sigut desada prèviament.</i></p>

<h2 style="text-align: right"><em><br>~ 03 de Novembre de 2021</em></h2>
