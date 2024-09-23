const fs = require("fs");

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, "utf8", (err, data) => {
      if (err) {
        reject(err);
      } else {
        const students = data
          .split("\n")
          .map((line) => line.trim())
          .filter((line) => line !== "")
          .map((line) => line.split(","));

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

        resolve(fields);
      }
    });
  });
}

module.exports = readDatabase;
