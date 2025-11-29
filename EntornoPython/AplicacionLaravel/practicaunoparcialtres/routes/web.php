<?php

use App\Http\Controllers\SensorController;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\DB;
use App\Models\Sensor;

Route::get('/',function(){
    $datos = Sensor::orderBy('created_at','desc')->take(20)->pluck('sensor_uno');
    return view('welcome',compact('datos'));
});