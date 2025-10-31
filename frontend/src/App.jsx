import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import UbicacionSalas from "./pages/UbicacionSalas";
import SalasDisponibles from "./pages/SalasDisponibles";
import Reglamentacion from "./pages/ReglamentacionReservas";
import AsistenciaRemota from "./pages/AsistenciaRemota";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/ubicacion" element={<UbicacionSalas />} />
        <Route path="/salas" element={<SalasDisponibles />} />
        <Route path="/reglamentacion" element={<Reglamentacion />} />
        <Route path="/asistencia" element={<AsistenciaRemota />} />
      </Routes>
    </Router>
  );
}

export default App;
