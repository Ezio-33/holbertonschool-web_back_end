const http = require('http');
const fs = require('fs');
const url = require('url');

const app = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  if (parsedUrl.pathname === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (parsedUrl.pathname === '/students') {
    const databasePath = process.argv[2];
    fs.readFile(databasePath, 'utf8', (err, data) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Cannot load the database');
      } else {
        const students = data
          .split('\n')
          .map((line) => line.trim())
          .filter((line) => line !== '')
          .map((line) => line.split(','));

        let responseText = 'This is the list of our students\n';
        responseText += `Number of students: ${students.length - 1}\n`;

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

        for (const [field, names] of Object.entries(fields)) {
          responseText += `Number of students in ${field}: ${
            names.length
          }. List: ${names.join(', ')}\n`;
        }

        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(responseText);
      }
    });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

module.exports = app;
