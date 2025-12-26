// -*- coding: utf-8 -*-
// Point d'entrée Mobile - Inventaire SaaS
import 'package:flutter/material.dart';
import 'screens/product_list_screen.dart';
import 'screens/add_product_screen.dart';
import 'screens/scan_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Inventaire SaaS',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: ProductListScreen(),
      routes: {
        '/add': (context) => AddProductScreen(),
        '/scan': (context) => ScanScreen(),
      },
    );
  }
}
