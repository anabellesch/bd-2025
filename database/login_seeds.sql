USE gestion_salas;

-- Logins (passwords se guardan hasheadas)
INSERT INTO login (correo, password_hash, ci_participante)
VALUES ('ana.gomez@example.com', 'PENDING_HASH', '1000001'),
       ('juan.perez@example.com', 'PENDING_HASH', '1000002');