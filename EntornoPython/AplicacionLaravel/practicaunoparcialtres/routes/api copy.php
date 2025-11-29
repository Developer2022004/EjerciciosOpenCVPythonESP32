<?php

use App\Http\Controllers\SensorController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Models\Sensor;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get("/sensor",[SensorController::class,'index']);
Route::post("api/sensores",[SensorController::class,'store']);
// Route::get('/sensor', function (Request $request) {
//     return response()->json([
//         'message' => 'ok',
//     ],201);
// });

// Route::get('/sensores', function (Request $request) {
//     return response()->json([
//         'message' => 'ok',
//         'data' => $request->all()
//     ]);
// });