import React, { useState } from "react";
import axios from "../services/api";

const AddProduct = () => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [quantity, setQuantity] = useState(0);
  const [value, setValue] = useState(0);
  const [code, setCode] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("token");
      await axios.post(
        "/products",
        { name, description, quantity, value, code_unique: code },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      alert("Produit ajouté avec succès !");
      setName(""); setDescription(""); setQuantity(0); setValue(0); setCode("");
    } catch (error) {
      alert("Erreur lors de l'ajout du produit");
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Ajouter un Produit</h2>
      <input type="text" placeholder="Nom" value={name} onChange={(e)=>setName(e.target.value)} required />
      <input type="text" placeholder="Description" value={description} onChange={(e)=>setDescription(e.target.value)} />
      <input type="number" placeholder="Quantité" value={quantity} onChange={(e)=>setQuantity(e.target.value)} required />
      <input type="number" placeholder="Valeur" value={value} onChange={(e)=>setValue(e.target.value)} required />
      <input type="text" placeholder="Code Unique (QR)" value={code} onChange={(e)=>setCode(e.target.value)} />
      <button type="submit">Ajouter</button>
    </form>
  );
};

export default AddProduct;
