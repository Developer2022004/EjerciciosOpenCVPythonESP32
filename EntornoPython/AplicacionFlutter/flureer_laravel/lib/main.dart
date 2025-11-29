import 'package:flureer_laravel/widgets/Graficas.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Laravel',
      theme: ThemeData(),
      debugShowCheckedModeBanner: false,
      home: Graficas(),
    );
  }
}
