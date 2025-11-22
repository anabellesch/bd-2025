from db import execute_query;

class ParticipanteService:

    @staticmethod
    def listar():
        conn = execute_query()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT ci, nombre, apellido, email FROM participante")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    @staticmethod
    def obtener(ci):
        conn = execute_query()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT ci, nombre, apellido, email FROM participante WHERE ci = %s", (ci,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if not row:
            raise ValueError("Participante no encontrado")
        return row

    @staticmethod
    def crear(ci, nombre, apellido, email):
        conn = execute_query()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO participante (ci, nombre, apellido, email) VALUES (%s,%s,%s,%s)",
                        (ci, nombre, apellido, email))
            conn.commit()
            return {"message": "Participante creado"}
        except Exception as e:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def eliminar(ci):
        conn = execute_query()
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM participante WHERE ci = %s", (ci,))
            conn.commit()
            return {"message": "Participante eliminado"}
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
