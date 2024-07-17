````markdown
# ES6 Basics

## Resources

Lisez ou regardez les ressources suivantes :

- [ECMAScript 6 - ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp)
- [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [Javascript ES6 — Iterables and Iterators](https://towardsdatascience.com/javascript-es6-iterables-and-iterators-de18b54f4d4)

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer à quiconque, sans l'aide de Google :

- Qu'est-ce qu'ES6
- Les nouvelles fonctionnalités introduites dans ES6
- La différence entre une constante et une variable
- Les variables à portée de bloc
- Les fonctions fléchées et les paramètres par défaut des fonctions
- Les paramètres rest et spread
- Les littéraux de chaîne en ES6
- La création d'objets et leurs propriétés en ES6
- Les itérateurs et les boucles for-of

## Exigences

### Général

- Tous vos fichiers seront exécutés sur Ubuntu 18.04 LTS en utilisant NodeJS 12.11.x
- Les éditeurs autorisés sont : vi, vim, emacs, Visual Studio Code
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- Un fichier README.md à la racine du dossier du projet est obligatoire
- Votre code doit utiliser l'extension .js
- Votre code sera testé à l'aide du framework de test Jest
- Votre code sera analysé à l'aide du linter ESLint avec des règles spécifiques fournies
- Toutes vos fonctions doivent être exportées

## Configuration

### Installation de NodeJS 12.11.x

```bash
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```
````

Vérifiez la version installée :

```bash
nodejs -v
npm -v
```

### Installation de Jest, Babel et ESLint

Dans le répertoire de votre projet, installez les dépendances suivantes :

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

## Fichiers de configuration

Créez les fichiers suivants à la racine de votre projet :

### package.json

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
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```

### babel.config.js

```javascript
module.exports = {
  presets: [
    [
      "@babel/preset-env",
      {
        targets: {
          node: "current",
        },
      },
    ],
  ],
};
```

### .eslintrc.js

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

N'oubliez pas d'exécuter `npm install` depuis le terminal de votre dossier de projet pour installer toutes les dépendances nécessaires.

```

## Tâches du projet

1. Utilisation de `const` et `let`
2. Portée des blocs
3. Fonctions fléchées
4. Paramètres par défaut
5. Paramètres rest
6. Opérateur spread
7. Littéraux de gabarits
8. Propriétés d'objet raccourcies
9. Propriétés calculées
10. Méthodes ES6
11. Boucles for...of
12. Création d'objets itérables

## Auteur

Samuel Verschueren

## Licence

Ce projet est sous licence MIT.
```
