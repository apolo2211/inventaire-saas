import 'package:flutter/material.dart';
import '../services/api_service.dart';

class AddProductScreen extends StatefulWidget {
  @override
  _AddProductScreenState createState() => _AddProductScreenState();
}

class _AddProductScreenState extends State<AddProductScreen> {
  final _formKey = GlobalKey<FormState>();
  String name = '', description = '', code = '';
  int quantity = 0;
  double value = 0.0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Ajouter Produit')),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                decoration: InputDecoration(labelText: 'Nom'),
                onChanged: (val) => name = val,
                validator: (val) => val!.isEmpty ? 'Requis' : null,
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Description'),
                onChanged: (val) => description = val,
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Quantité'),
                keyboardType: TextInputType.number,
                onChanged: (val) => quantity = int.tryParse(val) ?? 0,
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Valeur'),
                keyboardType: TextInputType.number,
                onChanged: (val) => value = double.tryParse(val) ?? 0.0,
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Code Unique'),
                onChanged: (val) => code = val,
              ),
              SizedBox(height: 20),
              ElevatedButton(
                child: Text('Ajouter'),
                onPressed: () async {
                  if (_formKey.currentState!.validate()) {
                    bool success = await ApiService.addProduct({
                      "name": name,
                      "description": description,
                      "quantity": quantity,
                      "value": value,
                      "code_unique": code
                    });
                    if (success) Navigator.pop(context);
                  }
                },
              )
            ],
          ),
        ),
      ),
    );
  }
}
