// auth.js
import { auth } from './firebase.js';
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword
} from "https://www.gstatic.com/firebasejs/9.22.2/firebase-auth.js";

const signUpForm = document.getElementById('signUpForm');
const signInForm = document.getElementById('signInForm');

if (signUpForm) {
  signUpForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = signUpForm.email.value;
    const password = signUpForm.password.value;

    try {
      await createUserWithEmailAndPassword(auth, email, password);
      alert('Sign-up successful! Redirecting...');
      window.location.href = "dashboard.html";
    } catch (error) {
      alert(error.message);
    }
  });
}

if (signInForm) {
  signInForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = signInForm.email.value;
    const password = signInForm.password.value;

    try {
      await signInWithEmailAndPassword(auth, email, password);
      alert('Sign-in successful! Redirecting...');
      window.location.href = "dashboard.html";
    } catch (error) {
      alert(error.message);
    }
  });
}
