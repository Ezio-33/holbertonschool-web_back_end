import express from "express";
import controllerRouting from "./routes/index.js";
import { countStudents, countStudentsByMajor } from "./utils.js";

const app = express();
const PORT = 1245;

controllerRouting(app);

const databaseFile = process.argv[2];

app.get("/students", (req, res) => {
  countStudents(databaseFile)
    .then((data) => {
      res.send(`This is the list of our students\n${data}`);
    })
    .catch((err) => {
      res.status(500).send(err.message);
    });
});

app.get("/students/:major", (req, res) => {
  const { major } = req.params;
  countStudentsByMajor(databaseFile, major)
    .then((data) => {
      res.send(`List: ${data.join(", ")}`);
    })
    .catch((err) => {
      res.status(500).send(err.message);
    });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

export default app;
