import { createUser, uploadPhoto } from './utils';

function handleProfileSignup() {
  return Promise.all([createUser(), uploadPhoto()])
    .then((values) => {
      console.log(
        `${values[1].body} ${values[0].firstName} ${values[0].lastName}`,
      );
    })
    .catch(() => console.log('Signup system offline'));
}

export default handleProfileSignup;
