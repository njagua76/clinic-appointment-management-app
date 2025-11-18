import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ padding: "10px 20px", background: "#007bff" }}>
      <Link to="/patients" style={{ color: "white", marginRight: "15px" }}>Patients</Link>
      <Link to="/doctors" style={{ color: "white", marginRight: "15px" }}>Doctors</Link>
      <Link to="/appointments" style={{ color: "white" }}>Appointments</Link>
    </nav>
  );
}
