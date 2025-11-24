# Integración de GlitchTip con Django

Este proyecto incorpora un sistema de monitoreo y captura de errores utilizando GlitchTip, una alternativa open-source a Sentry. La integración permite recibir, almacenar y visualizar errores generados por la aplicación Django en tiempo real, facilitando el debugging y aumentando la observabilidad del sistema.

## Comparativa de Herramientas de Monitoreo

A continuación se documenta un cuadro comparativo entre las herramientas evaluadas durante la investigación previa del proyecto y la herramienta final seleccionada (**GlitchTip**).

| Herramienta | Tipo | Ventajas | Desventajas |
| :--- | :--- | :--- | :--- |
| **GlitchTip** | Open Source (Self-hosted o cloud) | - Muy similar a Sentry. <br>- Panel moderno y detallado. <br>- API compatible con SDKs de Sentry. <br>- Permite alertas y notificaciones. | - Requiere Docker para instalación completa. |
| **Sentry (Cloud)** | SaaS | - Estándar del mercado. <br>- SDK muy maduro. <br>- Dashboards avanzados. | - Versión cloud limitada en el plan gratuito. <br>- Self-hosted muy pesado. |
| **Errbit** | Open Source | - Ligero. <br>- Fácil de desplegar. | - Interfaz antigua. <br>- No soporta el SDK moderno de Sentry. |
| **Elastic APM** | Open Source / Enterprise | - Observabilidad completa (Logs, metrics, tracing). | - Requiere ElasticSearch + stack ELK (pesado). <br>- Configuración compleja. |


Después, de lo anterior se siguio con la instalación de GlitchTip, Por lo cual en primer lugar se instalo Docker.
Así mismo, Se utilizo el siguiente compose para la instlacion de manera local.

```bash
services:
  postgres:
    image: postgres:14-alpine
    restart: unless-stopped
    volumes:
      - postgres-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=glitchtip
      - POSTGRES_USER=glitchtip
      - POSTGRES_PASSWORD=glitchtip

  redis:
    image: redis:7-alpine
    restart: unless-stopped

  glitchtip:
    image: glitchtip/glitchtip:latest
    restart: unless-stopped
    command: sh -c "python manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 glitchtip.wsgi"
    depends_on:
      - postgres
      - redis
    environment:
      - DJANGO_SETTINGS_MODULE=glitchtip.settings
      - DATABASE_URL=postgres://glitchtip:glitchtip@postgres:5432/glitchtip
      - REDIS_URL=redis://redis:6379/1
      - SECRET_KEY=1234567891011121314151617181920
      - DEBUG=True
      - EMAIL_URL=consolemail://  # Agrega esto para evitar errores de email
    ports:
      - "8000:8000"

  # WORKER DE CELERY - ESTO ES LO QUE FALTABA
  worker:
    image: glitchtip/glitchtip:latest
    restart: unless-stopped
    command: celery -A glitchtip worker -l INFO
    depends_on:
      - postgres
      - redis
      - glitchtip
    environment:
      - DJANGO_SETTINGS_MODULE=glitchtip.settings
      - DATABASE_URL=postgres://glitchtip:glitchtip@postgres:5432/glitchtip
      - REDIS_URL=redis://redis:6379/1
      - SECRET_KEY=1234567891011121314151617181920
      - EMAIL_URL=consolemail://

  # BEAT DE CELERY (opcional pero recomendado para tareas programadas)
  beat:
    image: glitchtip/glitchtip:latest
    restart: unless-stopped
    command: celery -A glitchtip beat -l INFO
    depends_on:
      - postgres
      - redis
    environment:
      - DJANGO_SETTINGS_MODULE=glitchtip.settings
      - DATABASE_URL=postgres://glitchtip:glitchtip@postgres:5432/glitchtip
      - REDIS_URL=redis://redis:6379/1
      - SECRET_KEY=1234567891011121314151617181920
      - EMAIL_URL=consolemail://

volumes:
  postgres-data:

```

Después, de esto se tuvo que instalar el sdk de sentry, esto para poder hacer la comunición de django hacia,
el servidor de glitchtip

### Instalacíon del SDK

```bash
pip install sentry-sdk

```

Teniendo esto, se hace la configuracíon en el archvio de settings.py

```bash

# Inicializa el SDK de GlitchTip para capturar errores en Django
sentry_sdk.init(
    # DSN (Data Source Name): clave pública + URL del servidor + ID del proyecto.
    # Permite que la aplicación envíe errores al servidor de Sentry/GlitchTip.
    dsn="http://9eebc2a03fef4208a86411a561bdf87b@localhost:8000/1",

    # Integración específica para Django:
    # habilita la captura automática de excepciones, errores en vistas,
    # información del request, usuario autenticado, etc.
    integrations=[DjangoIntegration()],

    # Modo debug del SDK:
    # muestra en consola los eventos enviados, útil para pruebas locales.
    debug=True,

    # Entorno donde corre este proyecto:
    # permite diferenciar errores de "development", "staging" o "production".
    environment="development",
)

```

Para poder probar, se hace una vista para generar un error.

```bash
# Esta función existe únicamente para forzar un error y comprobar
# que GlitchTip está capturando y enviando excepciones correctamente.
def trigger_error(request):
    # Al dividir entre cero se genera una excepción ZeroDivisionError.
    1 / 0


```

Finalmente, se coloca la url, en el archivo de urls.py, para generar el error.

```bash
 # Ruta para forzar un error
    path('glitchtip-debug/', views.trigger_error, name='glitchtip-debug')

```

Cabe mencionar que para que se visualize, se debe de arrancar el servidor de django,
en el puerto 8001.

