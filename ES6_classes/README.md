# Classes ES6

## Description

Ce projet explore les concepts avancés des classes en JavaScript ES6, y compris la métaprogrammation et l'utilisation de symboles.

## Ressources

Lire ou regarder :

- [Classes](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Classes)
- [Métaprogrammation](https://www.keithcirkel.co.uk/metaprogramming-in-es6-symbols/)

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être en mesure d'expliquer à n'importe qui, sans l'aide de Google :

- Comment définir une classe
- Comment ajouter des méthodes à une classe
- Pourquoi et comment ajouter une méthode statique à une classe
- Comment étendre une classe à partir d'une autre
- Métaprogrammation et symboles

## Exigences

- Tous vos fichiers seront exécutés sur Ubuntu 18.04 LTS en utilisant NodeJS 12.11.x
- Éditeurs autorisés : vi, vim, emacs, Visual Studio Code
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- Un fichier README.md, à la racine du dossier du projet, est obligatoire
- Votre code doit utiliser l'extension js
- Votre code sera testé à l'aide de Jest et de la commande npm run test
- Votre code sera vérifié par lint en utilisant ESLint
- Votre code doit passer tous les tests et le lint. Vous pouvez vérifier l'ensemble du projet en exécutant npm run full-test

## Configuration

### Installer NodeJS 12.11.x

(dans votre répertoire personnel) :

```

curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y

```

```

$ nodejs -v
v12.11.1
$ npm -v
6.11.3
```

### Installer Jest, Babel et ESLint

Dans votre répertoire de projet :

- Installer Jest en utilisant : `npm install --save-dev jest`
- Installer Babel en utilisant : `npm install --save-dev babel-jest @babel/core @babel/preset-env`
- Installer ESLint en utilisant : `npm install --save-dev eslint`

## Fichiers de configuration

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
    "@babel/preset-env": "^7.6.0",
    "@babel/node": "^7.8.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```

### babel.config.js```javascript

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

N'oubliez pas de lancer $ npm install lorsque vous avez le package.json

## Tasks

0. You used to attend a place like this at some point
1. Let's make some classrooms
2. A Course, Getters, and Setters
3. Methods, static methods, computed methods names..... MONEY
4. Pricing
5. A Building
6. Inheritance
7. Airport
8. Primitive - Holberton Class
9. Hoisting
10. Vroom
