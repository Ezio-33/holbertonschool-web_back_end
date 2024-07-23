# ES6 Promises

## Présentation du Projet

### Objectifs d'Apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer à n'importe qui, sans l'aide de Google, les concepts suivants :

- Les promesses (comment, pourquoi et quoi)
- Comment utiliser les méthodes `then`, `resolve`, `catch`
- Comment utiliser chaque méthode de l'objet Promise
- Les blocs `throw` et `try`
- L'opérateur `await`
- Comment utiliser une fonction `async`

### Prérequis

- NodeJS 12.11.x installé sur Ubuntu 18.04 LTS
- Éditeurs de texte recommandés : `vi`, `vim`, `emacs`, Visual Studio Code
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- Un fichier `README.md` à la racine du projet est obligatoire
- Votre code doit utiliser l'extension `.js`
- Votre code sera testé avec Jest et la commande `npm run test`
- Votre code sera vérifié avec ESLint

### Installation et Configuration

1. **Installer NodeJS 20.x.x** :

   ```bash
   curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
   sudo bash nodesource_setup.sh
   sudo apt install nodejs -y
   nodejs -v
   npm -v
   ```

2. **Installer Jest, Babel, et ESLint** :
   ```bash
   npm install --save-dev jest
   npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
   npm install --save-dev eslint
   ```

### Fichiers à Créer

- `package.json`
- `babel.config.js`
- `utils.js`
- `.eslintrc.js`

### Format des Données de Réponse

- `uploadPhoto` retourne un objet :

  ```json
  {
    "status": 200,
    "body": "photo-profile-1"
  }
  ```

- `createUser` retourne un objet :
  ```json
  {
    "firstName": "Guillaume",
    "lastName": "Salva"
  }
  ```

### Tâches

1. **Retourner une promesse** :

   - Créer une fonction `getResponseFromAPI` qui retourne une promesse.

2. **Gérer une promesse avec un paramètre booléen** :

   - Créer une fonction `getFullResponseFromAPI` qui retourne une promesse en fonction d'un paramètre booléen.

3. **Ajouter des gestionnaires de promesses** :

   - Créer une fonction `handleResponseFromAPI` qui ajoute des gestionnaires à une promesse.

4. **Gérer plusieurs promesses réussies** :

   - Créer une fonction `handleProfileSignup` qui utilise `uploadPhoto` et `createUser`.

5. **Promesse simple** :

   - Créer une fonction `signUpUser` qui retourne une promesse résolue avec un objet.

6. **Rejeter des promesses** :

   - Créer une fonction `uploadPhoto` qui retourne une promesse rejetée avec un message d'erreur.

7. **Gérer plusieurs promesses** :

   - Créer une fonction `handleProfileSignup` qui gère les promesses de `signUpUser` et `uploadPhoto`.

8. **Load balancer** :

   - Créer une fonction `loadBalancer` qui retourne la valeur de la promesse résolue en premier.

9. **Gérer les erreurs avec `try/catch`** :
   - Créer une fonction `divideFunction` qui lève une erreur si le dénominateur est 0.
   - Créer une fonction `guardrail` qui capture les erreurs et ajoute des messages à une file d'attente.

## Resources

**Lire ou regarder**:

- [JavaScript Promise: An introduction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
- [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [Throw / Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
