// 7-has_array_values.js
function hasValuesFromArray(set, array) {
  return array.every((value) => set.has(value));
}

export default hasValuesFromArray;
