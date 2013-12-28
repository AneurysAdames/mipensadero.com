Tip Calery: Mostrar el estado de una tarea en ejecución
#######################################################
:date: 2013-02-01 02:22
:author: bameda
:category: snippets
:tags: celery, django, django-celery, python, snippets, tips
:slug: tip-calery-mostrar-el-estado-de-una-tarea-en-ejecucion

`Celery`_ es una aplicación python que **nos permite crear tareas de
trabajo asíncronas gestionadas por un gestor de colas, basada en el
paradigma de envío de mensajes, de manera distribuida**. Se focaliza en
operaciones en tiempo real pero también soporta la generación de tareas
periódicas, es decir, puede lanzar tareas que se tengan que ejecutar en
un momento determinado (al más puro estilo cron de Linux). Las unidades
de ejecución, llamadas tareas, se ejecutan de manera concurrente en uno
o más nodos de trabajo. Estas tareas pueden ejecutarse de manera
asíncrona o bien de manera síncrona (esperando hasta que la tarea está
lista); o incluso puedes generar una cadena de tareas . El sistema de
mensajería recomendado por Celery es RabbitMQ aunque tamiben se pueden
usar otros (Redis, MongoDB o una base de datos SQL).

En mi caso, lo suelo usar conjuntamente con la librería
**django-celery**, para integrarlo en las aplicaciones django y delegar
algunas tareas pesadas, por ejemplo: envío de emails (masivos),
recálculos pesados, generación de reportes, ..

En esta ocasión he tenido que generar una tarea que crease informes en
csv sobre una colección de datos muy grande extraídos de la base de
datos además de otro conjunto de datos generados. Por lo que el periodo
de generación del informe podría llegar a ser de varias horas, por lo
que necesitaba mostrar que porcentaje de datos se habían procesado.

    reports/tasks.py

.. code-block:: python

    # -*- coding: utf-8 -*-
    from celery import task
    from celery import current_task
    from reports.models import Report

    # More imports
    # (...)

    def _update_task_state(state, **kwargs):
        current_task.update_state(state=state, meta=kwargs)
        # Some auxiliar functions
        # (...)

    @task(ignore_result=True, name="create-csv-report")
    def create_csv_report(report_id):
        report = Report.objects.get(pk=report_id)
        if report:
            # Create the csv file and write the first row
            # (...)

        total = report.items.count()
        current = 0
        for item in report.items.all():
            # Print the item data to the csv file
            # (...)

        current += 1
        _update_task_state("PROCESSING", current=current, total=total)

De esta forma el estado de la tarea se va actualizando cada vez que
procesamos un elemento. Por lo que podremos mostrar este estado, por
ejemplo, en el panel de administración de django de la siguiente manera.

    reports/admin.py

.. code-block:: python

    # -*- coding: utf-8 -*-
    from django.contrib import admin
    from celery import task
    from celery import current_task
    from reports.models import Report
    # More imports
    # (...)

    class ReportAdmin(admin.ModelAdmin)
        # Some atributes
        # (...)
        list_display = ("uuid", "created_at", "user", "colored_status", "async_task_status",)

        def async_task_status(self, report_obj):
            if report_obj.task_uuid:
                status = current_app.backend.get_status(report_obj.task_uuid)
                info = current_app.backend.get_result(report_obj.task_uuid)

                if status == "PROCESING" and info:
                    current = info.get("current", None)
                    total = info.get("total", None)
                    return u"%(percentage).1f%% (Processing %(current)d of %(total)d)" % {
                        "percentage": current * 100.0 / total,
                        "current": current,
                        "total": total,
                    })

                return "Not started yet"

        async_task_status.short_description = _(u"Asyncronous task status")
        async_task_status.allow_tags = True

        # More methods
        # (...)

    # More methods and/or class
    # (...)

Y quedaría algo así:

|Panel de administración de infórmenes|

Espero que esto os sea de utiliza. Quejas, dudas y sugerencias serán
bien recibidas.

.. _Celery: http://celeryproject.org/

.. |Panel de administración de infórmenes| image:: /media/2013/02/reports_admin_status.png
   :target: /media/2013/02/reports_admin_status.png
