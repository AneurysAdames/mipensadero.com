pyLoad, alternativa "ligera" a jDownloader
##########################################
:date: 2011-04-06 22:57
:author: bameda
:category: software
:tags: descargas, jdownloader, NAS, pyload, python, recomendaciones, software
:slug: pyload-alternativa-ligera-a-jdownloader

El otro día un amigo me comentó que estaba buscando una aplicación tipo
`jDownloader`_ para su `NAS`_. En principio descartó jDownloader porque
resulta ser una solución muy pesada ya que depende de Java. Además la
alternativa ha de tener una interfaz web/interprete de comandos para su
uso debido a que los NAS suelen carecer de pantalla.

Así que recordé haber leído algo por ahí sobre una alternativa que
se adaptaba perfectamente a sus necesidades, de ella sólo recordaba que
estaba hecha en python. Me puse a buscar en google y la encontré de
inmediato.

El software en cuestión se llama `pyLoad`_ y pretende ser un gestor de
descargas ligero para esos One-Click-Hoster que están ahora tan de moda,
no obstante no hay mejor definición que la de su propia página web:

    `pyLoad`_ is a fast, lightweight and full featured download manager
    for many One-Click-Hoster, container formats like DLC, video sites
    or just plain http/ftp links. It aims for low hardware requirements
    and platform independence to be runnable on all kind of systems
    (desktop pc, netbook, NAS, router).

Algunas de las características que ofrece son:

-  **Multiplataforma**: ya que está hecho en Python
-  **Multilingüe**:  actualmente traducido a 7 idiomas (en, de, it, pl,
   fr, cs, es)
-  **Soporta los servicios más utilizados en la actualidad**: cuentas
   gratuitas y cuentas premium de Rapidshare, Megaupload, HotFile,
   YouTube... `y muchos más`_.
-  **Arquitectura cliente-servidor**: la aplicación posee un servidor o
   core y varios clientes:

   -  **GUI**: interfaz de escritorio realizada en pyQT para todas las
      plataformas (Linux, Windows y Mac).
   -  **CLI**: interfaz de linea de comandos útil para interactuar en
      remoto (no disponible en la versión para Windows).
   -  **Web Interface**: interfaz web para acceder con tu navegador
      favorito desde donde quieras.
   -  **Android Client**: es un cliente Android para manejar la
      aplicación desde tu smartphone o tu tableta.
   -  **IRC/XMPP Interface**: controla `pyLoad`_ desde tu cliente de IRC
      o de mensajería.

-  **Es Software Libre**: con todas las ventajas que ello conlleva.

Personalmente, `pyLoad`_ me gusta por su versatilidad y facilidad de
uso. Además no consume a penas recursos del sistema, lo que ofrece
la posibilidad de `instalarlo incluso en el router`_ de casa. Y
todo ello en una aplicación hecha en python.

Aquí os dejo su `página de descarga`_, donde encontraréis `pyLoad`_
empaquetado para diferentes sistemas operativos, y su `wiki`_, donde
encontraréis toda la información necesaria para su uso e instalación.

.. _jDownloader: http://jdownloader.org/
.. _NAS: http://es.wikipedia.org/wiki/Network-attached_storage
.. _pyLoad: http://pyload.org/
.. _y muchos más: http://pyload.org/hoster
.. _instalarlo incluso en el router: http://pyload.org/installing_pyload_on_a_router
.. _página de descarga: http://pyload.org/download
.. _wiki: http://pyload.org/wiki
