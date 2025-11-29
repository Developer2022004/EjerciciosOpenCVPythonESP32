<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use App\Models\Sensor;
use Exception;

class SensorController extends Controller
{
   public function index()
   {
      // //Para descomprimir los objetos de Sensors en un array de elementos faciles de interactuar.
      // $datos = DB::table('sensors')->pluck('sensor_uno')->map(fn($valor) => floatval($valor));
      // // dd($datos);
      // return view('welcome',compact('datos'));
      
      //pluck obtiene los valores del campo de la entidad
      $datos = Sensor::orderBy('created_at','desc')->take(20)->pluck('sensor_uno');
      return view('welcome',compact('datos'));
   }

   public function vistaSensores()
   {
      $datos = Sensor::orderBy('created_at','desc')->take(20)->pluck('sensor_uno')->map(fn($v) => floatval($v))->values();
      return response()->json($datos);
   }

   public function store(Request $request)
   {
      $request->validate([
        'valor' => 'required|numeric',
      ]);

      $sensor = new Sensor();
      $sensor->sensor_uno = $request->valor;
      $sensor->save();
      // try{
      //    $sensor->save();
      // }catch(Exception $e){
      //    return response()->json(["error" => $e->getMessage()]);
      // }

      $maxRegistros = 20;

      $total = Sensor::count();
      if ($total > $maxRegistros) {
         $excedente = $total - $maxRegistros;
         Sensor::orderBy('created_at', 'asc')->limit($excedente)->delete();
      }
      return response()->json(["mensaje" => "Sensor registrado"]);
   }
}