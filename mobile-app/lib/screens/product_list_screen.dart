import 'package:flutter/material.dart';
import '../services/api_service.dart';

class ProductListScreen extends StatefulWidget {
  @override
  _ProductListScreenState createState() => _ProductListScreenState();
}

class _ProductListScreenState extends State<ProductListScreen> {
  List products = [];

  @override
  void initState() {
    super.initState();
    fetchProducts();
  }

  fetchProducts() async {
    var data = await ApiService.getProducts();
    setState(() {
      products = data;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Inventaire Produits')),
      body: ListView.builder(
        itemCount: products.length,
        itemBuilder: (context, index) {
          var p = products[index];
          return ListTile(
            title: Text(p['name']),
            subtitle: Text('Quantité: ${p['quantity']} - Code: ${p['code_unique']}'),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () => Navigator.pushNamed(context, '/add'),
      ),
    );
  }
}
