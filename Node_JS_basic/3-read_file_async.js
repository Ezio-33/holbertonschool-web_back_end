// En utilisant la base de données database.csv (fournie dans la description du projet),
// créez une fonction countStudents dans le fichier 3-read_file_async.js
// créez une fonction nommée countStudents.
// Elle doit accepter un chemin en argument (comme dans 2-read_file.js)
// Le script doit tenter de lire le fichier de base de données de manière asynchrone
// La fonction doit retourner une Promesse
// Si la base de données n'est pas disponible, elle doit lancer une erreur avec le texte
// "Cannot load the database"
// Si la base de données est disponible, elle doit afficher le
// message suivant dans la console "Number of students: NUMBER_OF_STUDENTS"
// Elle doit afficher le nombre d'étudiants dans chaque domaine,
// et la liste avec le format suivant : "Number of students in FIELD:
// 6. List: LIST_OF_FIRSTNAMES"
// Le fichier CSV peut contenir des lignes vides (à la fin) - et elles ne sont pas
//des étudiants valides !const fs = require("fs").promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, { encoding: "utf8" });
    const lines = data
      .trim()
      .split("\n")
      .filter((line) => line.length > 0);
    lines.shift();
    if (lines.lenght === 0) {
      console.log("Number of students: 0");
      return;
    }
    const studentFields = {};
    lines.forEach((line) => {
      const [firstname, , , field] = line.split(",");
      if (!studentFields[field]) {
        studentFields[field] = [];
      }
      studentFields[field].push(firstname);
    });
    console.log(`Number of students: ${lines.length}`);
    for (const field in studentFields) {
      if (field) {
        const list = studentFields[field].join(", ");
        console.log(
          `Number of students in ${field}: ${studentFields[field].length}. List: ${list}`
        );
      }
    }
  } catch (err) {
    throw new Error("Cannot load the database");
  }
}
module.exports = countStudents;
