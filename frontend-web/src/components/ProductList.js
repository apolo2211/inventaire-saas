import React, { useState, useEffect } from "react";
import axios from "../services/api";

const ProductList = () => {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    try {
      const token = localStorage.getItem("token");
      const response = await axios.get("/products", { headers: { Authorization: `Bearer ${token}` } });
      setProducts(response.data);
    } catch (error) {
      console.error("Erreur lors du chargement des produits", error);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div>
      <h2>Inventaire Produits</h2>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Nom</th>
            <th>Description</th>
            <th>Quantité</th>
            <th>Valeur</th>
            <th>Code Unique</th>
          </tr>
        </thead>
        <tbody>
          {products.map((p) => (
            <tr key={p.id}>
              <td>{p.name}</td>
              <td>{p.description}</td>
              <td>{p.quantity}</td>
              <td>{p.value}</td>
              <td>{p.code_unique}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProductList;
