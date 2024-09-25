const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json()); // Para poder parsear requests JSON

// Ruta simple
app.get('/api/datos', (req, res) => {
  res.json({ mensaje: 'Hola desde el back end!' });
});

// Iniciar el servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
