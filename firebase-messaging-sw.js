importScripts('https://www.gstatic.com/firebasejs/9.6.10/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.10/firebase-messaging-compat.js');

// Ваша конфигурация Firebase
const firebaseConfig = {
    apiKey: "AIzaSyAl5OYzwT9W55-GV_cN8rtpvqj1dyHQhAA",
    authDomain: "django-app-980ad.firebaseapp.com",
    projectId: "django-app-980ad",
    storageBucket: "django-app-980ad.appspot.com",
    messagingSenderId: "1022628920985",
    appId: "1:1022628920985:web:9e06039017ffdee16a0208"
};

// Инициализация Firebase в Service Worker
firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();

// Обработка фоновых сообщений (background notifications)
messaging.onBackgroundMessage((payload) => {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);

    // Настройки уведомления
    const notificationTitle = payload.notification.title;
    const notificationOptions = {
        body: payload.notification.body,
        icon: '/firebase-logo.png'  // Иконка уведомления (можете указать свою)
    };

    self.registration.showNotification(notificationTitle, notificationOptions);
});
