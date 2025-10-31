import { useNavigate } from "react-router-dom";
import "../styles/Home.css";
import Navbar from "../components/Navbar";

// import clock from "../assets/clock.png";
// import classroom from "../assets/classroom.jpg";

export default function Home() {
  const navigate=useNavigate();

  return (
  <div className="home-container">
      <aside className="sidebar">
        <img src='https://icons.veryicon.com/png/o/miscellaneous/all-blue-icon/clock-294.png' alt="Clock icon" />
      </aside>

      <main className="content">
        <header className="header">
          <Navbar />
        </header>

        <section>
          <h2 className="title">Sistema de Gestión de Salas de Estudio UCU</h2>

          <div className="resources">
            <div className="resources-text">
              <h3>RECURSOS</h3>
              <div className="resource-buttons">
                <button className="resource-button" onClick={() => navigate("/ubicacion")}>Ubicación de salas</button>
                <button className="resource-button" onClick={() => navigate("/salas")}>Salas disponibles</button>
                <button className="resource-button" onClick={() => navigate("/reglamentacion")}>Reglamentación de reservas</button>
                <button className="resource-button" onClick={() => navigate("/asistencia")}>Asistencia remota</button>
              </div>
            </div>
            <img src='https://i.pinimg.com/736x/fa/c4/20/fac420951935b4d3973acd604e43a3c0.jpg' alt="Sala" className="resource-image" />
          </div>
        </section>
      </main>
    </div>
  );
}
