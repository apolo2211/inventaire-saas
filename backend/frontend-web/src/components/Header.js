import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Inventaire</Link></li>
        <li><Link to="/add">Ajouter Produit</Link></li>
      </ul>
    </nav>
  );
};

export default Header;
