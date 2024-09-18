const express = require('express');
const fs = require('fs');

const app = express();
const PORT = 1245;

const countStudents = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
    } else {
      // Traitez les données ici (comme dans la tâche 3)
      const students = data
        .split('\n')
        .map((line) => line.trim())
        .filter((line) => line !== '')
        .map((line) => line.split(','));

      const numberOfStudents = students.length - 1;
      const fields = {};

      for (const student of students.slice(1)) {
        if (student.length === 4) {
          const [firstName, lastName, age, field] = student;
          if (fields[field]) {
            fields[field].push(firstName);
          } else {
            fields[field] = [firstName];
          }
        }
      }

      let responseText = `Number of students: ${numberOfStudents}\n`;
      for (const [field, students] of Object.entries(fields)) {
        responseText += `Number of students in ${field}: ${
          students.length
        }. List: ${students.join(', ')}`;
      }

      resolve(responseText);
    }
  });
});

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const path = process.argv[2];
  countStudents(path)
    .then((responseText) => {
      res.send(`This is the list of our students\n${responseText}`);
    })
    .catch((err) => {
      res.status(500).send(err.message);
    });
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

module.exports = app;
