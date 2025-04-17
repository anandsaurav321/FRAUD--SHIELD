// firebase.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyAf3HK1-DNMVdBP3nlDEjOcKHw25kyOP8M",
  authDomain: "fraudshield2.firebaseapp.com",
  projectId: "fraudshield2",
  storageBucket: "fraudshield2.appspot.com",
  messagingSenderId: "574836527786",
  appId: "1:574836527786:web:30b2bf63a5b175632ff6d3",
  measurementId: "G-T4Q17V89R0"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { auth, db };
