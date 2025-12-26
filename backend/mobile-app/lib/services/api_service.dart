import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  static String baseUrl = "http://127.0.0.1:5000";

  static Future<List> getProducts() async {
    String token = "VOTRE_TOKEN"; // à remplacer par stockage sécurisé
    var response = await http.get(
      Uri.parse("$baseUrl/products"),
      headers: {"Authorization": "Bearer $token"},
    );
    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      return [];
    }
  }

  static Future<bool> addProduct(Map data) async {
    String token = "VOTRE_TOKEN";
    var response = await http.post(
      Uri.parse("$baseUrl/products"),
      headers: {
        "Authorization": "Bearer $token",
        "Content-Type": "application/json"
      },
      body: json.encode(data),
    );
    return response.statusCode == 201;
  }

  static Future<bool> updateInventory(String code) async {
    String token = "VOTRE_TOKEN";
    var response = await http.post(
      Uri.parse("$baseUrl/inventory/scan"),
      headers: {
        "Authorization": "Bearer $token",
        "Content-Type": "application/json"
      },
      body: json.encode({"code_unique": code}),
    );
    return response.statusCode == 200;
  }
}
