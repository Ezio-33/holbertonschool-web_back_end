const express = require("express");
const countStudents = require("./3-read_file_async");

const app = express();
const dbfile = process.argv[2];

app.get("/", (req, res) => {
  res.send("Hello Holberton School!");
});

app.get("/students", async (req, res) => {
  res.write("This is the list of our students\n");
  try {
    const originalLog = console.log;
    console.log = () => {};
    let logs = "";

    console.log = (msg) => {
      logs += `${msg}\n`;
    };

    await countStudents(dbfile);
    console.log = originalLog;
    res.write(logs);
  } catch (error) {
    res.write(error.message);
  } finally {
    res.end();
  }
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Express server listening on port ${PORT}`);
});

module.exports = app;
