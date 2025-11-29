<?php

use App\Http\Controllers\SensorController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

// Route::get('/sensor', function () {
//     $data = Sensor::orderBy('created_at', 'desc')->take(20)->get();
//     return response()->json($data);
// });


//Ruta correspondiente a la api de captura de datos por parte de la aplicacion en flutter.
Route::get('/dsensor',[SensorController::class,'vistaSensores']);

//Ruta correspondiente a la api de captura de datos por parte de la aplicacion en laravel.
Route::get('/sensor',[SensorController::class,'index']);

//Ruta correspondiente a la api de envio de informacion desde el microcontrolador.
Route::post('/sensores',[SensorController::class,'store']);