Kata: Sumar Arrays (en C y Common Lisp)
#######################################
:date: 2011-11-01 02:06
:author: bameda
:category: snippets
:tags: array, c, kata, lisp, optimización, snippets, suma, vectores
:slug: kata-sumar-arrays-en-c-y-common-lisp

Desde `kaleidos.net`_\ se nos planteaba una `kata`_ muy interesante que
transcribo a continuación:

    **Kata: Sumar arrays**

    Empecemos con algo sencillo, para desentumecer los músculos.

    Muchas veces, cuando programamos con una fecha límite, y tenemos que
    resolver los problemas con prisa, no nos preocupamos por el
    rendimiento. Como mucho, pensamos en refactorizar más adelante si
    hace falta. Sería muy bueno tener integradas ciertas rutinas de
    programación que nos permitan programar de forma más eficiente sin
    pensarlo.

    A si que la kata que propongo es la siguiente:

    Tenemos diez arrays largos, de 500 enteros cada uno.  Queremos
    obtener el número que obtenemos al sumar cada uno de esos
    10\*500=5000 enteros. Sencillo, ¿verdad?

    Elige tu lenguaje de programación preferido. Y piensa dos formas
    distintas de obtener la suma. Por ejemplo, puedes sumar cada uno de
    los arrays por separado, y luego sumar los resultados. O puedes
    hacer sumas parciales de cada una de las posiciones de los arrays. O
    fundir los arrays en uno, y luego sumar todos los números. O
    cualquier otra forma que se te ocurra (¿una funcion recursiva
    tendría sentido?). Implementalas.

    Ahora, mediante un bucle,  mide el tiempo que tarda en ejecutarse
    1000 veces cada una de ellas.

    ¿Cuales son los resultados? ¿La forma que pensabas que sería más
    rápida, lo era de verdad?

    Bonus I: A la vista de los resultados, ¿se te ocurre una tercera
    forma capaz de conseguir un mejor rendimiento?

    Bonus II: Repite el ejercicio en un lenguaje en el que nunca hayas
    programado

    Y recuerda,  no se trata de un concurso. Se trata de una kata.
    Practica y mejora. Siempre

En la noticia extendida encontrarás mis soluciones en **C** y **Common
Lisp**.

En primer lugar ofrezco la solución en Common Lisp (OJO, probablemente
tú encuentres una solución mejor)

.. code-block:: common-lisp

    #|
     | kata.lisp
     |
     | Author: David Barragan Merino (@bameda)
     | Date: 2011-10-29
     |
     | Interpreter
     | clisp kata.lisp
     | Compile:
     | clisp -c -l -q kata.lisp -o kata
     | Execute:
     | clisp kata.fas
     |#
    (defun random_list (L n)
        (if (> n 1)
            (random_list (cons (random 1000000) L) (1- n))
            (cons (random 1000000) L)))

    (defun random_lists (L n)
        (if (> n 1)
            (random_lists (cons (random_list nil 500) L) (1- n))
            (cons (random_list nil 500) L)))

    (defun sup_sum (L)
        (reduce #'+ (mapcar #'(lambda (x) (apply #'+ x)) L)))

    (defun sup_sum2 (L)
        (if L
            (+ (apply #'+ (car L)) (sup_sum2 (cdr L)))
            (apply #'+ (car L))))

    (defun sum (L res)
        (if L
            (+ (car L) (sum (cdr L) res))
            (if res
                (sum (car res) (cdr res))
                0)))

    (let ((arrays (random_lists nil 10)))
        (time (sup_sum arrays)))

    (let ((arrays (random_lists nil 10)))
        (time (sup_sum2 arrays)))

    (let ((arrays (random_lists nil 10)))
        (time (sum nil arrays)))


Y a continuación la versión en C

.. code-block:: c

    /* kata.c
     *
     * Author: David Barragan Merino (@bameda)
     * Date: 2011-10-29
     *
     * Compile:
     * gcc kata.c -o kata
     * Execute:
     * ./kata
     */
    #include <stdio.h>
    #include <stdlib.h>

    #define NUM_ARRAYS 10
    #define ARRAY_SIZE 500
    #define MAX 1000000

    int main(int argc, char *argv[]) {
       struct timeval tv;
       long double t_init, t_end;

       int arrays[NUM_ARRAYS][ARRAY_SIZE];
       int sum;
       int i, j;

       // Generate Arrays
       for (i = 0; i < NUM_ARRAYS; i++)
           for (j = 0; j < ARRAY_SIZE; j++)
               arrays[i][j] = rand() % MAX + 1;

       gettimeofday(&tv, NULL);
       t_init = tv.tv_sec + (tv.tv_usec / 1000000.0);

       // Calculate
       for (i = 0; i < NUM_ARRAYS; i++)
           for (j = 0; j < ARRAY_SIZE; j++)
               sum += arrays[i][j];

       gettimeofday(&tv, NULL);
       t_end = tv.tv_sec + (tv.tv_usec / 1000000.0);
       printf("Total time: %Lgn", t_end - t_init);
   }


Por último muestro los resultados obtenidos para tres ejecuciones, en
primer lugar lanzando lisp desde el interprete

::
     Real time: 1.03E-4 sec.
     Run time: 0.0 sec.
     Space: 608 Bytes
     Real time: 9.9E-5 sec.
     Run time: 0.0 sec.
     Space: 0 Bytes
     Real time: 0.009647 sec.
     Run time: 0.012 sec.
     Space: 0 Bytes

en segundo lugar compilando lisp

::
     bameda@stewie:~$ clisp -c -l -q kata.lisp -o kata
     ;; Compiling file /home/bameda/kata.lisp ...
     ;; Wrote file /home/bameda/kata.fas
     ;; Wrote file /home/bameda/kata.lis
     0 errores, 0 advertencias
     bameda@stewie:~$ clisp kata.fas
     Real time: 9.8E-5 sec.
     Run time: 0.0 sec.
     Space: 160 Bytes
     Real time: 9.1E-5 sec.
     Run time: 0.0 sec.
     Space: 0 Bytes
     Real time: 9.69E-4 sec.
     Run time: 0.0 sec.
     Space: 0 Bytes

y en tercer lugar la ejecución en C

::
     bameda@stewie:~$ gcc kata.c -o kata
     bameda@stewie:~$ ./kata
     Total time: 1.50204e-05

Saquen sus propias conclusiones

.. _kaleidos.net: http://kaleidos.net
.. _kata: http://albaontech.wordpress.com/2011/10/27/kata-sumar-arrays/#comments
