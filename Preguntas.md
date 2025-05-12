# Criterio 6a) Objetivos estratégicos:

## ¿Qué objetivos estratégicos específicos de la empresa aborda tu software?
El bot de Discord permite organizar mejor

## ¿Cómo se alinea el software con la estrategia general de digitalización?
Debido a la naturaleza de Discord que permite a los usuarios poder comunicarse entre ellos a remoto, el bot organizador de tareas supone una gran ayuda a la hora de organizarse en equipo y realizar todo desde el mismo medio en vez de tener que depender de papeles para hacer anotaciones; ese medio siendo en este caso Discord.


# Criterio 6b) Áreas de negocio y comunicaciones:

## ¿Qué áreas de la empresa (producción, negocio, comunicaciones) se ven más beneficiadas con tu software?
Cualquier área puede beneficiarse, pero especialmente aquellas que trabajen en grupo a remoto le podrán dar un buen uso al bot.

## ¿Qué impacto operativo esperas en las operaciones diarias?


# Criterio 6c) Áreas susceptibles de digitalización:

## ¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?
Aquellas empresas que estén utilizando Discord para comunicarse pueden beneficiarse de este bot.

## ¿Cómo mejorará la digitalización las operaciones en esas áreas?
Les permitirá 


# Criterio 6d) Encaje de áreas digitalizadas (AD):

## ¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?
El bot asume que se utiliza Discord, el cual ya implica intrínsecamente un proceso de digitalización, pero sí que es cierto que Discord podría seguir siendo utilizado como un simple medio para comunicarse sin el uso del bot, y que se sigan realizando algunas de las tareas a mano.


## ¿Qué soluciones o mejoras propondrías para integrar estas áreas?
La implementación de más funcionalidades fomentaría el uso del propio bot sobre las secciones no digitalizadas, haciendo más llamativo y asequible el uso del bot comparado a otros medios no digitalizados.


# Criterio 6e) Necesidades presentes y futuras:

## ¿Qué necesidades actuales de la empresa resuelve tu software?
La organización del trabajo es una tarea ardua y usualmente molesta, ya que tiende a consumir tiempo que podría estar siendo utilizado en realizar las tareas en sí. Es por esto que el bot permite a los usuarios no solo poder llevar un seguimiento de todas las tareas que deseen sino que al mismo tiempo esto les ayudará a recordarlas y tenerlas a mano en todo momento.


# Criterio 6f) Relación con tecnologías:

## ¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?
A pesar de no haberse llegado a implementar, la tecnología habilitadora que se tenía pensado implementar era el cloud computing, donde se podrían almacenar datos en servidores o bases de datos a través de internet.


## ¿Qué beneficios específicos aporta la implantación de estas tecnologías?
En este caso habría permitido almacenar datos más pesados y complejos y sería capaz de conservarlos incluso a pesar de que el bot no estuviera activo, ya que en el estado actual del bot la lista de tareas se elimina cuando este deja de estar activo.


# Criterio 6g) Brechas de seguridad:

## ¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?
La brecha de seguridad más plausible que suceda es o bien el token del bot de discord o el ID del canal siendo expuesto al público, ya que ambas cosas son datos confidenciales. 



## ¿Qué medidas concretas propondrías para mitigarlas?
Almacenando la información en un .env permitirá que esta se mantenga oculta al resto de usuarios, de forma que no será expuesta y por ende no habría problemas al respecto.



# Criterio 6h) Tratamiento de datos y análisis:

## ¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?
Todos los datos son almacenados dentro de una lista mientras que el bot está activo. Esto se borra 

## ¿Qué haces para garantizar la calidad y consistencia de los datos?
El formato de los datos siempre es el mismo, de forma que las tareas se almacenan en un formato clave-valor donde primero se nombra la tarea y luego aparece su nombre ("Tarea: nombre"). Esto hace que los datos se muestren de la siguiente manera:

    ["Tarea": "n1", "Tarea": "n2", "Tarea": "n3"]