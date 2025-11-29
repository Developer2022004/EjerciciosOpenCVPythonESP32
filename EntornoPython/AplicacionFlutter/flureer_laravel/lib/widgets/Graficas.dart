import 'package:flutter/material.dart';
import 'dart:convert';
import 'dart:async';
import 'package:http/http.dart' as http;
import 'package:fl_chart/fl_chart.dart';

class Graficas extends StatefulWidget {
  const Graficas({super.key});

  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return Ventana();
  }
}

class Ventana extends State<Graficas> {
  List<double> datos_grafica = [];
  bool cargando = true;
  Timer? timer;

  //Se carga despues del constructor, es el escuchador de la ventana
  @override
  void initState() {
    super.initState();
    obtenerDatos();

    //Que se hara cada 3 segundos?
    timer = Timer.periodic(const Duration(seconds: 3), (timer) {
      obtenerDatos();
    });
  }

  //Para cerrar la aplicacion
  @override
  void dispose() {
    timer?.cancel();
    super.dispose();
  }

  Future obtenerDatos() async {
    try {
      final url = Uri.parse("http://192.168.100.14:8000/api/dsensor");
      final response = await http.get(url).timeout(const Duration(seconds: 10));
      if (response.statusCode == 200) {
        final dynamic datos = json.decode(response.body);
        if (datos is List) {
          setState(() {
            final _datos =
                datos.map<double>((item) {
                  if (item is num) return item.toDouble();
                  return double.tryParse(item.toString()) ?? 0.0;
                }).toList();

            //Construimos los datos de la grafica
            datos_grafica =
                _datos.length > 10
                    ? _datos.sublist(_datos.length - 10)
                    : _datos;

            cargando = false;
          });
        }
      }
    } catch (e) {
      print('Error $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(
        title: Text('Graficas', style: TextStyle(color: Colors.white)),
        backgroundColor: Colors.amber,
      ),
      body:
          cargando
              ? Center(child: CircularProgressIndicator())
              : Padding(
                padding: EdgeInsets.all(10),
                child: Column(
                  children: [
                    Card(
                      elevation: 15,
                      child: Padding(
                        padding: EdgeInsets.all(5),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Column(
                              children: [
                                Text("Datos a Graficar"),
                                Text("Datos: ${datos_grafica.length}"),
                              ],
                            ),
                            Column(
                              children: [
                                Text("Ultimo Dato"),
                                //toStringAsFixed() convierte a String y redonde a un  entero proximo
                                Text(
                                  "Datos: ${datos_grafica.isNotEmpty ? datos_grafica.last.toStringAsFixed(1) : '0'}",
                                ),
                              ],
                            ),
                            Column(
                              children: [
                                Text("Primer Dato"),
                                Text(
                                  "Datos: ${datos_grafica.isNotEmpty ? datos_grafica.first.toStringAsFixed(1) : '0'}",
                                ),
                              ],
                            ),
                            SizedBox(width: 5),
                          ],
                        ),
                      ),
                    ),
                    //Debajo del card
                    Expanded(
                      child: BarChart(
                        BarChartData(
                          minY: 0,
                          maxY:
                              datos_grafica.isNotEmpty
                                  ? datos_grafica.reduce(
                                        (a, b) => a > b ? a : b,
                                      ) *
                                      1.2
                                  : 100,
                          barGroups:
                              datos_grafica.asMap().entries.map((entry) {
                                final index = entry.key;
                                final valor = entry.value;
                                return BarChartGroupData(
                                  x: index,
                                  barRods: [
                                    BarChartRodData(
                                      toY: valor,
                                      color: Colors.deepOrange,
                                      width: 15,
                                      borderRadius: BorderRadius.circular(5),
                                    ),
                                  ],
                                );
                              }).toList(),
                          titlesData: FlTitlesData(
                            bottomTitles: AxisTitles(
                              sideTitles: SideTitles(
                                showTitles: true,
                                getTitlesWidget: (value, meta) {
                                  return Text('${value.toInt() + 1}');
                                },
                              ),
                            ),
                            leftTitles: AxisTitles(
                              sideTitles: SideTitles(
                                showTitles: true,
                                getTitlesWidget: (value, meta) {
                                  return Text('${value.toInt()}');
                                },
                              ),
                            ),
                          ),
                          gridData: FlGridData(show: true),
                          borderData: FlBorderData(show: true),
                        ),
                      ),
                    ),
                    Expanded(
                      child: LineChart(
                        LineChartData(
                          minY: 0,
                          maxY: 100,
                          lineBarsData: [
                            LineChartBarData(
                              spots: [
                                for (int i = 0; i < datos_grafica.length; i++)
                                  FlSpot(i.toDouble(), datos_grafica[i]),
                              ],
                              isCurved: true,
                              color: Colors.red,
                              barWidth: 3,
                              dotData: FlDotData(show: false),
                            ),
                            LineChartBarData(
                              spots: [
                                for (int a = 0; a < datos_grafica.length; a++)
                                  FlSpot(a.toDouble(), datos_grafica[a]),
                              ],
                            ),
                          ],
                          titlesData: FlTitlesData(
                            bottomTitles: AxisTitles(
                              sideTitles: SideTitles(
                                showTitles: true,
                                getTitlesWidget: (value, meta) {
                                  return Text('${value.toInt() + 1}');
                                },
                              ),
                            ),
                            leftTitles: AxisTitles(
                              sideTitles: SideTitles(
                                showTitles: true,
                                getTitlesWidget: (value, meta) {
                                  return Text('${value.toInt()}');
                                },
                              ),
                            ),
                          ),
                          gridData: FlGridData(show: true),
                          borderData: FlBorderData(show: true),
                        ),
                      ),
                    ),
                    Expanded(
                      //Hacer tercera grafica
                      child: PieChart(
                        PieChartData(
                          sections: () {
                            if (datos_grafica.isEmpty)
                              return <PieChartSectionData>[];

                            final total = datos_grafica.reduce((a, b) => a + b);

                            return datos_grafica.map<PieChartSectionData>((
                              item,
                            ) {
                              final valor = item;
                              final porcentaje =
                                  total > 0 ? (valor / total) * 100 : 0;

                              return PieChartSectionData(
                                value: valor,
                                color: Colors.blue,
                                title: '${porcentaje.toStringAsFixed(1)}%',
                                radius: 50,
                                titleStyle: const TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white,
                                ),
                              );
                            }).toList();
                          }(),
                          centerSpaceRadius: 30,
                          sectionsSpace: 2,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
    );
  }
}
