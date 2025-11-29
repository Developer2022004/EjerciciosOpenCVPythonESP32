<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Paths that should be accessible through CORS
    |--------------------------------------------------------------------------
    |
    | Aquí defines qué rutas aceptan solicitudes con CORS.
    | "api/*" significa: todas las rutas dentro de /api/
    |
    */

    'paths' => ['api/*', 'sanctum/csrf-cookie'],

    /*
    |--------------------------------------------------------------------------
    | Allowed Methods
    |--------------------------------------------------------------------------
    |
    | Métodos HTTP permitidos.
    |
    */

    'allowed_methods' => ['*'],

    /*
    |--------------------------------------------------------------------------
    | Allowed Origins
    |--------------------------------------------------------------------------
    |
    | IPs o dominios que pueden acceder a Laravel.
    | "*" significa cualquier origen (incluye IPs LAN y ESP32).
    |
    */

    'allowed_origins' => ['*'],

    /*
    |--------------------------------------------------------------------------
    | Allowed Origins Patterns
    |--------------------------------------------------------------------------
    |
    | Útil si deseas aceptar un rango como: 192.168.*.*
    | Está vacío porque allowed_origins ya acepta "*".
    |
    */

    'allowed_origins_patterns' => [],

    /*
    |--------------------------------------------------------------------------
    | Allowed Headers
    |--------------------------------------------------------------------------
    |
    | Headers aceptados.
    |
    */

    'allowed_headers' => ['*'],

    /*
    |--------------------------------------------------------------------------
    | Exposed Headers
    |--------------------------------------------------------------------------
    |
    | Headers que el cliente puede leer.
    |
    */

    'exposed_headers' => [],

    /*
    |--------------------------------------------------------------------------
    | Max Age
    |--------------------------------------------------------------------------
    |
    | Tiempo en segundos para cache del preflight.
    |
    */

    'max_age' => 0,

    /*
    |--------------------------------------------------------------------------
    | Supports Credentials
    |--------------------------------------------------------------------------
    |
    | Debe estar en false para ESP32 y clientes sin cookies.
    |
    */

    'supports_credentials' => false,

];
