Modelo ART
El modelo ART se refiere a la gestión de seguros de Accidentes de Riesgos de Trabajo (ART) en la aplicación de Seguranza Seguros SA.

Descripción
El modelo ART se encarga de gestionar la información relacionada con las pólizas de seguros de accidentes de trabajo para los clientes de la compañía. Este modelo incluye campos como la profesión u oficio del asegurado, el código postal, la matrícula del seguro, y el año de la póliza.

Estructura del Modelo
El modelo ART cuenta con los siguientes campos:

Profesión u Oficio: Campo de texto que indica la profesión u oficio del asegurado.
Código Postal: Campo de texto que almacena el código postal del asegurado.
Matrícula: Campo de texto que guarda el número de matrícula de la póliza de seguro.
Año: Campo entero que representa el año de vigencia de la póliza.
Uso en la Aplicación
El modelo ART se utiliza en las siguientes partes de la aplicación:

Formulario de Cotización (artForm.html): Este formulario permite a los usuarios obtener una cotización personalizada para su seguro de ART. Los campos correspondientes a la profesión u oficio, código postal y año son completados por el usuario.

Listado de Usuarios Suscriptos (art_list.html): En esta sección se muestra un listado de usuarios que han suscrito pólizas de ART. Se muestran detalles como la profesión u oficio, código postal, matrícula y año de la póliza.

Página de Coberturas de ART (artcob.html): Aquí se presentan los distintos tipos de coberturas disponibles para los seguros de ART. Se detallan los precios mensuales y las coberturas incluidas para los trabajadores independientes y los que están en relación de dependencia.

Dependencias del Modelo
El modelo ART depende de los siguientes archivos y recursos en la aplicación:

Plantilla HTML para Formulario ART: Se utiliza la plantilla artForm.html para renderizar el formulario de cotización de seguros de ART.
Plantilla HTML para Listado de Usuarios Suscriptos: Se utiliza la plantilla art_list.html para mostrar el listado de usuarios que han suscrito pólizas de ART.
Plantilla HTML para Coberturas de ART: Se utiliza la plantilla artcob.html para mostrar los distintos tipos de coberturas disponibles para los seguros de ART.