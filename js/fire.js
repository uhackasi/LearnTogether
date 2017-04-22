var config = {
    apiKey: "AIzaSyBLA6sDqXwnMX6tJayM4dmYCPRzt5CW91M",
    authDomain: "learntogether-a250b.firebaseapp.com",
    databaseURL: "https://learntogether-a250b.firebaseio.com",
    projectId: "learntogether-a250b",
    storageBucket: "learntogether-a250b.appspot.com",
    messagingSenderId: "3175571907"
};
firebase.initializeApp(config);

signOut = function () {
    firebase.auth().signOut().then(function() {
        console.log("Signed out")
    }, function(error) {
        // An error happened.
    });
};

initApp = function() {
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            // User is signed in.
            var displayName = user.displayName;
            var email = user.email;
            var uid = user.uid;
            
            user.getToken().then(function(accessToken) {
                if(email.indexOf('monash.edu') < 0){
                    alert("Use monash email");
                    signOut();
                }else{
                    //redirect
                    window.location.href = "https://uhackasi.github.io/LearnTogether/logged.html";
                }
            });

        } else {
            // User is signed out.

        }
    }, function(error) {
        console.log(error);
    });
};


var uiConfig = {
    signInSuccessUrl: '.',
    signInOptions: [
        // Leave the lines as is for the providers you want to offer your users.
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        firebase.auth.EmailAuthProvider.PROVIDER_ID
    ],
    // Terms of service url.
    tosUrl: '<your-tos-url>'
};

