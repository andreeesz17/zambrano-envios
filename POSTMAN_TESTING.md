{
  "info": {
    "_postman_id": "b2d2c3f0-aaaa-bbbb-cccc-123456789000",
    "name": "Envios API (Django + Postgres + JWT)",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "variable": [
    { "key": "baseUrl", "value": "http://127.0.0.1:8000" },
    { "key": "accessToken", "value": "" },
    { "key": "refreshToken", "value": "" },
    { "key": "rutaId", "value": "" },
    { "key": "paqueteId", "value": "" }
  ],
  "item": [
    {
      "name": "Auth",
      "item": [
        {
          "name": "Register (Public) - POST /api/auth/register/",
          "request": {
            "method": "POST",
            "header": [{ "key": "Content-Type", "value": "application/json" }],
            "url": { "raw": "{{baseUrl}}/api/auth/register/", "host": ["{{baseUrl}}"], "path": ["api", "auth", "register", ""] },
            "body": {
              "mode": "raw",
              "raw": "{\n  \"username\": \"user1\",\n  \"email\": \"user1@mail.com\",\n  \"password\": \"123456\"\n}"
            }
          }
        },
        {
            "name": "Login (JWT) - POST /api/auth/login/ (save tokens)",
            "event": [
                {
                "listen": "test",
                "script": {
                    "type": "text/javascript",
                    "exec": [
                    "let jsonData = {};",
                    "try { jsonData = pm.response.json(); } catch (e) {}",
                    "",
                    "if (jsonData.access) {",
                    "  pm.collectionVariables.set('accessToken', jsonData.access);",
                    "  pm.environment.set('accessToken', jsonData.access);",
                    "}",
                    "",
                    "if (jsonData.refresh) {",
                    "  pm.collectionVariables.set('refreshToken', jsonData.refresh);",
                    "  pm.environment.set('refreshToken', jsonData.refresh);",
                    "}",
                    "",
                    "pm.test('Token access recibido', function () {",
                    "  pm.expect(jsonData.access).to.be.a('string');",
                    "});"
                    ]
                }
                }
            ],
            "request": {
                "method": "POST",
                "header": [
                { "key": "Content-Type", "value": "application/json" }
                ],
                "url": { "raw": "{{baseUrl}}/api/auth/login/", "host": ["{{baseUrl}}"], "path": ["api", "auth", "login", ""] },
                "body": {
                "mode": "raw",
                "raw": "{\n  \"username\": \"admin\",\n  \"password\": \"admin\"\n}"
                }
            }
        },
        {
          "name": "Refresh (JWT) - POST /api/auth/refresh/ (save access)",
          "event": [
            {
              "listen": "test",
              "script": {
                "type": "text/javascript",
                "exec": [
                  "let jsonData = {};",
                  "try { jsonData = pm.response.json(); } catch (e) {}",
                  "if (jsonData.access) pm.collectionVariables.set('accessToken', jsonData.access);",
                  "pm.test('Token access refrescado', function () { pm.expect(jsonData.access).to.be.a('string'); });"
                ]
              }
            }
          ],
          "request": {
            "method": "POST",
            "header": [{ "key": "Content-Type", "value": "application/json" }],
            "url": { "raw": "{{baseUrl}}/api/auth/refresh/", "host": ["{{baseUrl}}"], "path": ["api", "auth", "refresh", ""] },
            "body": {
              "mode": "raw",
              "raw": "{\n  \"refresh\": \"{{refreshToken}}\"\n}"
            }
          }
        }
      ]
    },
    {
      "name": "Postgres - Rutas",
      "item": [
        {
          "name": "List rutas (Public) - GET /api/rutas/",
          "request": {
            "method": "GET",
            "url": { "raw": "{{baseUrl}}/api/rutas/", "host": ["{{baseUrl}}"], "path": ["api", "rutas", ""] }
          }
        },
        {
          "name": "Create ruta (Auth) - POST /api/rutas/ (save rutaId)",
          "event": [
            {
              "listen": "test",
              "script": {
                "type": "text/javascript",
                "exec": [
                  "let jsonData = {};",
                  "try { jsonData = pm.response.json(); } catch (e) {}",
                  "if (jsonData.id) pm.collectionVariables.set('rutaId', jsonData.id);",
                  "pm.test('Se creó ruta', function () { pm.expect(jsonData.id).to.be.a('number'); });"
                ]
              }
            }
          ],
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type", "value": "application/json" },
              { "key": "Authorization", "value": "Bearer {{accessToken}}" }
            ],
            "url": { "raw": "{{baseUrl}}/api/rutas/", "host": ["{{baseUrl}}"], "path": ["api", "rutas", ""] },
            "body": { "mode": "raw", "raw": "{\n  \"codigo\": \"RUTA-001\"\n}" }
          }
        },
        {
          "name": "Get ruta by id (Public) - GET /api/rutas/:id",
          "request": {
            "method": "GET",
            "url": {
              "raw": "{{baseUrl}}/api/rutas/{{rutaId}}/",
              "host": ["{{baseUrl}}"],
              "path": ["api", "rutas", "{{rutaId}}", ""]
            }
          }
        },
        {
          "name": "Patch ruta (Auth) - PATCH /api/rutas/:id",
          "request": {
            "method": "PATCH",
            "header": [
              { "key": "Content-Type", "value": "application/json" },
              { "key": "Authorization", "value": "Bearer {{accessToken}}" }
            ],
            "url": {
              "raw": "{{baseUrl}}/api/rutas/{{rutaId}}/",
              "host": ["{{baseUrl}}"],
              "path": ["api", "rutas", "{{rutaId}}", ""]
            },
            "body": { "mode": "raw", "raw": "{\n  \"codigo\": \"RUTA-002\"\n}" }
          }
        },
        {
          "name": "Delete ruta (Auth) - DELETE /api/rutas/:id",
          "request": {
            "method": "DELETE",
            "header": [{ "key": "Authorization", "value": "Bearer {{accessToken}}" }],
            "url": {
              "raw": "{{baseUrl}}/api/rutas/{{rutaId}}/",
              "host": ["{{baseUrl}}"],
              "path": ["api", "rutas", "{{rutaId}}", ""]
            }
          }
        }
      ]
    },
    {
      "name": "Postgres - Paquetes",
      "item": [
        {
          "name": "List paquetes (Public) - GET /api/paquetes/",
          "request": {
            "method": "GET",
            "url": { "raw": "{{baseUrl}}/api/paquetes/", "host": ["{{baseUrl}}"], "path": ["api", "paquetes", ""] }
          }
        },
        {
          "name": "Create paquete (Auth) - POST /api/paquetes/ (save paqueteId)",
          "event": [
            {
              "listen": "test",
              "script": {
                "type": "text/javascript",
                "exec": [
                  "let jsonData = {};",
                  "try { jsonData = pm.response.json(); } catch (e) {}",
                  "if (jsonData.id) pm.collectionVariables.set('paqueteId', jsonData.id);",
                  "pm.test('Se creó paquete', function () { pm.expect(jsonData.id).to.be.a('number'); });"
                ]
              }
            }
          ],
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type", "value": "application/json" },
              { "key": "Authorization", "value": "Bearer {{accessToken}}" }
            ],
            "url": { "raw": "{{baseUrl}}/api/paquetes/", "host": ["{{baseUrl}}"], "path": ["api", "paquetes", ""] },
            "body": {
              "mode": "raw",
              "raw": "{\n  \"codigo_rastreo\": 1,\n  \"destinatario\": \"Juan Pérez\",\n  \"peso_kg\": 5,\n  \"tipo\": \"paquete\",\n  \"estado\": \"pendiente\"\n}"
            }
          }
        },
        {
          "name": "Get paquete by id (Public) - GET /api/paquetes/:id",
          "request": {
            "method": "GET",
            "url": {
              "raw": "{{baseUrl}}/api/paquetes/{{paqueteId}}/",
              "host": ["{{baseUrl}}"],
              "path": ["api", "paquetes", "{{paqueteId}}", ""]
            }
          }
        },
        {
          "name": "Patch paquete (Auth) - PATCH /api/paquetes/:id",
          "request": {
            "method": "PATCH",
            "header": [
              { "key": "Content-Type", "value": "application/json" },
              { "key": "Authorization", "value": "Bearer {{accessToken}}" }
            ],
            "url": {
              "raw": "{{baseUrl}}/api/paquetes/{{paqueteId}}/",
              "host": ["{{baseUrl}}"],
              "path": ["api", "paquetes", "{{paqueteId}}", ""]
            },
            "body": { "mode": "raw", "raw": "{\n  \"estado\": \"entregado\",\n  \"peso_kg\": 5\n}" }
          }
        },
        {
          "name": "Delete paquete (Auth) - DELETE /api/paquetes/:id",
          "request": {
            "method": "DELETE",
            "header": [{ "key": "Authorization", "value": "Bearer {{accessToken}}" }],
            "url": {
              "raw": "{{baseUrl}}/api/paquetes/{{paqueteId}}/",
              "host": ["{{baseUrl}}"],
              "path": ["api", "paquetes", "{{paqueteId}}", ""]
            }
          }
        }
      ]
    }
  ]
}