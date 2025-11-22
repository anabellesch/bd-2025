import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import UbicacionSalas from "./pages/UbicacionSalas";
import SalasDisponibles from "./pages/SalasDisponibles";
import Reglamentacion from "./pages/ReglamentacionReservas";
import AsistenciaRemota from "./pages/AsistenciaRemota";
import Reservas from "./pages/Reservas";
import Dashboard from "./pages/Dashboard";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/ubicacion" element={<UbicacionSalas />} />
        <Route path="/salas" element={<SalasDisponibles />} />
        <Route path="/reservas" element={<Reservas />} />
        <Route path="/reglamentacion" element={<Reglamentacion />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/asistencia" element={<AsistenciaRemota />} />
      </Routes>
    </Router>
  );
}

export default App;