import { useState } from "react";
import { api } from "../services/api";

export default function SalasDisponibles() {
  const [fecha, setFecha] = useState("");
  const [hora, setHora] = useState("");
  const [salas, setSalas] = useState([]);

  const buscar = async () => {
    const res = await api.post("/reservas/disponibles", { fecha, hora });
    setSalas(res);
  };

  return (
    <div className="page">
      <h2>Salas Disponibles</h2>
      <div className="filtros">
        <input type="date" value={fecha} onChange={(e) => setFecha(e.target.value)} />
        <input type="time" value={hora} onChange={(e) => setHora(e.target.value)} />
        <button onClick={buscar}>Buscar</button>
      </div>
      <ul>
        {salas.map((s) => (
          <li key={s.nombre_sala}>
            {s.nombre_sala} - {s.edificio} ({s.capacidad} personas)
          </li>
        ))}
      </ul>
    </div>
  );
}
