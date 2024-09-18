const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const students = data
          .split('\n')
          .map((line) => line.trim())
          .filter((line) => line !== '')
          .map((line) => line.split(','));

        const numberOfStudents = students.length - 1;
        console.log(`Number of students: ${numberOfStudents}`);

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

        for (const [field, students] of Object.entries(fields)) {
          const studentList = students.join(', ');
          console.log(
            `Number of students in ${field}: ${students.length}. List: ${studentList}`,
          );
        }
        resolve();
      }
    });
  });
}

module.exports = countStudents;
