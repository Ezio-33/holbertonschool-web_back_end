// 3-get_ids_sum.js
function getStudentIdsSum(listeEtudiants) {
  return listeEtudiants.reduce(
    (accumulateur, etudiant) => accumulateur + etudiant.id,
    0,
  );
}

export default getStudentIdsSum;
