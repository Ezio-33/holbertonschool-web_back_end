# Manipulation de Données en ES6

## Description

Ce projet vise à enseigner les concepts avancés de manipulation de données en JavaScript ES6. Vous apprendrez à utiliser des méthodes comme `map`, `filter`, et `reduce` sur des tableaux, ainsi que des structures de données comme `Set`, `Map`, et les tableaux typés.

## Objectifs d'apprentissage

À la fin de ce projet, vous serez capable de :

- Utiliser `map`, `filter`, et `reduce` sur des tableaux.
- Comprendre et utiliser les tableaux typés.
- Manipuler les structures de données `Set`, `Map`, et `WeakMap`.

## Prérequis

- Connaissances de base en JavaScript.
- NodeJS et npm installés sur votre machine.

## Ressources

- [Array](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Array)
- [Typed Array](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Typed_arrays)
- [Set Data Structure](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map Data Structure](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

## Installation

1. **Installer NodeJS 20.x.x** :

   ```bash
   curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
   sudo bash nodesource_setup.sh
   sudo apt install nodejs -y
   ```

   Vérifiez les versions installées :

   ```bash
   nodejs -v
   npm -v
   ```

2. **Installer les dépendances** :

   - Jest pour les tests :
     ```bash
     npm install --save-dev jest
     ```
   - Babel pour la transpilation :
     ```bash
     npm install --save-dev babel-jest @babel/core @babel/preset-env
     ```
   - ESLint pour le linting :
     ```bash
     npm install --save-dev eslint
     ```

3. **Configuration des fichiers** :

   - `package.json` :

     ```json
     {
       "scripts": {
         "lint": "./node_modules/.bin/eslint",
         "check-lint": "lint [0-9]*.js",
         "dev": "npx babel-node",
         "test": "jest",
         "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
       },
       "devDependencies": {
         "@babel/core": "^7.6.0",
         "@babel/node": "^7.8.0",
         "@babel/preset-env": "^7.6.0",
         "eslint": "^6.8.0",
         "eslint-config-airbnb-base": "^14.0.0",
         "eslint-plugin-import": "^2.18.2",
         "eslint-plugin-jest": "^22.17.0",
         "jest": "^24.9.0"
       }
     }
     ```

   - `babel.config.js` :

     ```javascript
     module.exports = {
       presets: [
         "@babel/preset-env",
         {
           targets: {
             node: "current",
           },
         },
       ],
     };
     ```

   - `.eslintrc.js` :
     ```javascript
     module.exports = {
       env: {
         browser: false,
         es6: true,
         jest: true,
       },
       extends: ["airbnb-base", "plugin:jest/all"],
       globals: {
         Atomics: "readonly",
         SharedArrayBuffer: "readonly",
       },
       parserOptions: {
         ecmaVersion: 2018,
         sourceType: "module",
       },
       plugins: ["jest"],
       rules: {
         "max-classes-per-file": "off",
         "no-underscore-dangle": "off",
         "no-console": "off",
         "no-shadow": "off",
         "no-restricted-syntax": ["error", "LabeledStatement", "WithStatement"],
       },
       overrides: [
         {
           files: ["*.js"],
           excludedFiles: "babel.config.js",
         },
       ],
     };
     ```

## Auteurs

- Samuel VERSCHUEREN
