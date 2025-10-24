import React from "react";
import "./Navbar.css";
// import logo from "../assets/logo-ucu.png";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <img src='https://logoteca.uy/wp-content/uploads/sites/3/2024/09/Logo-Universidad-Catolica.svg' alt="Logo UCU" className="logo" />
        <div className="navbar-title">
          <h2>UCU</h2>
          <p>Universidad Católica del Uruguay</p>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
