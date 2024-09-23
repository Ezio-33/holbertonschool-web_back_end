const readDatabase = require("../utils");

class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const students = await readDatabase(process.argv[2]);

      let responseText = "This is the list of our students\n";
      const fields = Object.keys(students).sort();
      for (const field of fields) {
        responseText += `Number of students in ${field}: ${
          students[field].length
        }. List: ${students[field].join(", ")}\n`;
      }

      response.status(200).send(responseText);
    } catch (err) {
      response.status(500).send("Cannot load the database");
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== "CS" && major !== "SWE") {
      response.status(500).send("Major parameter must be CS or SWE");
      return;
    }

    try {
      const students = await readDatabase(process.argv[2]);

      let responseText = `List: ${students[major].join(", ")}`;
      response.status(200).send(responseText);
    } catch (err) {
      response.status(500).send("Cannot load the database");
    }
  }
}

module.exports = StudentsController;
