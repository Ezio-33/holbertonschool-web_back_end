// En utilisant la base de données database.csv (fournie dans la description du projet),
// créez une fonction countStudents dans le fichier 2-read_file.js
// Créez une fonction nommée countStudents. Elle doit accepter un chemin en argument.
// Le script doit tenter de lire le fichier de base de données de manière synchrone.
// Si la base de données n'est pas disponible, elle doit lancer une erreur avec le texte suivant :
// "Impossible de charger la base de données"
// Si la base de données est disponible, le script doit afficher le message suivant :
// "Nombre d'étudiants : NUMBER_OF_STUDENTS"
// Il doit enregistrer le nombre d'étudiants dans chaque domaine,
// et la liste dans le format suivant : "Nombre d'étudiants en FIELD :
// 6. Liste : LIST_OF_FIRST_NAMES"
// Le fichier CSV peut contenir des lignes vides (à la fin)

const fs = require('fs');

function countStudents(path) {
  try {
    const datas = fs
      .readFileSync(path, { encoding: 'utf8' })
      .trim()
      .split('\n')
      .filter((line) => line.length > 0);
    datas.shift();
    if (datas.length === 0) {
      console.log('Number of students: 0');
      return;
    }
    const studentFields = {};

    datas.forEach((data) => {
      const [firstname, , , field] = data.split(',');
      if (!studentFields[field]) {
        studentFields[field] = [];
      }
      studentFields[field].push(firstname);
    });
    console.log(`Number of students: ${datas.length}`);
    for (const field in studentFields) {
      if (field) {
        const list = studentFields[field].join(', ');
        console.log(
          `Number of students in ${field}: ${studentFields[field].length}. List: ${list}`,
        );
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
