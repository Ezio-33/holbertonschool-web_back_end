// En utilisant la base de données database.csv (fournie dans la description du projet),
// créez une fonction countStudents dans le fichier 2-read_file.js
// Créez une fonction nommée countStudents. Elle doit accepter un chemin en argument.
// Le script doit tenter de lire le fichier de base de données de manière synchrone.
// Si la base de données n'est pas disponible, elle doit lancer une erreur avec le texte suivant :
// "Impossible de charger la base de données"
// Si la base de données est disponible, le script doit afficher le message suivant :
// "Nombre d'étudiants : NUMBER_OF_STUDENTS"
// Il doit enregistrer le nombre d'étudiants dans chaque domaine,
// et la liste dans le format suivant : "Nombre d'étudiants en FIELD : 6. Liste : LIST_OF_FIRST_NAMES"
// Le fichier CSV peut contenir des lignes vides (à la fin)

const fs = require("fs");

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, "utf8");
    const students = data
      .split("\n")
      .map((line) => line.trim())
      .filter((line) => line !== "")
      .map((line) => line.split(","));

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
      const studentList = students.join(", ");
      console.log(
        `Number of students in ${field}: ${students.length}. List: ${studentList}`
      );
    }
  } catch (err) {
    throw new Error("Cannot load the database");
  }
}

module.exports = countStudents;
