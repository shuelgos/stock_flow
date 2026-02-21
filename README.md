# StockFlow API

Backend de gestión de inventario construido con Django y Django REST Framework.

Este proyecto permite administrar productos, registrar movimientos de stock y obtener métricas de inventario mediante una API REST segura.

---

## Tecnologías utilizadas

* Python 3.13
* Django 6
* Django REST Framework
* SQLite (por defecto)
* Token Authentication
* django-filter

---

## Funcionalidades actuales

### Productos

* CRUD completo de productos
* Activación/desactivación (`is_active`)
* Cálculo dinámico de stock (`current_stock`)
* Búsqueda, filtros y ordenamiento
* Paginación

---

### Movimientos de stock

* Registro de entradas (IN)
* Registro de salidas (OUT)
* Validación de stock insuficiente
* Validación de producto inactivo

---

### Métricas de inventario

Endpoints personalizados:

* `/api/products/low_stock/` — productos bajo mínimo
* `/api/products/summary/` — resumen general del inventario

---

### Seguridad

* Autenticación por Token
* Permisos globales (`IsAuthenticated`)

---

## Instalación

### 1. Clonar repositorio

```bash
git clone <TU_REPO_URL>
cd stockflow
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar en Windows:

```bash
venv\Scripts\activate
```

Activar en Linux / Mac:

```bash
source venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

---

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

---

### 6. Ejecutar servidor

```bash
python manage.py runserver
```

---

## Autenticación

La API utiliza Token Authentication.

### Uso del token

Incluir en cada request el header:

```
Authorization: Token <tu_token>
```

---

## Endpoints principales

### Productos

* `GET /api/products/`
* `POST /api/products/`
* `GET /api/products/{id}/`
* `PUT /api/products/{id}/`
* `DELETE /api/products/{id}/`

---

### Movimientos

* `GET /api/movements/`
* `POST /api/movements/`

---

### Endpoints personalizados

* `GET /api/products/low_stock/`
* `GET /api/products/summary/`

---

## Estado del proyecto

En desarrollo activo.

### Próximas mejoras

* Transacciones atómicas
* Optimización SQL del stock
* Tests automatizados
* Documentación OpenAPI
* Frontend dashboard

---

## Autor

Proyecto desarrollado como práctica de backend con Django REST Framework.

---

