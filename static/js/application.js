// Initialize Firebase
var config = {
  apiKey: "AIzaSyBMt2qeVQ2_iKOft5qj3UPZ23UqaYT6OQo",
  authDomain: "newsapp-7c644.firebaseapp.com",
  databaseURL: "https://newsapp-7c644.firebaseio.com",
  storageBucket: "newsapp-7c644.appspot.com",
  messagingSenderId: "212684616822"
};
firebase.initializeApp(config);

// var myFirebaseApp = firebase.database().ref();
//
// var myFirebase = new Firebase("https://" + myFirebaseApp + ".firebaseio.com/");

var sources = firebase.database().ref("sources");

data = "../../newsSources.json"
var newsSources = JSON.parse(data);

// Save a new recommendation to the database, using the input in the form
var createNewSource = function (i) {

  // Get input values from each of the form elements
  var newsName = newsSources.sources[i].newsName;
  var fbLink = newsSources.sources[i].fbLink;
  var logo = newsSources.sources[i].logo;
  var leans = newsSources.sources[i].leans;

  // Push a new recommendation to the database using those values
  sources.push({
    "newsName": title,
    "fbLink": presenter,
    "logo": link,
    "leans": leans
  });
};

var displaySources = function() {

};

$( document ).ready(function() {
    console.log( "ready!" );
    var numSources = newsSources.sources.length;
    var i = 0;
    for (i = 0; i < numSources; i++) {
      createNewSource(i);
    }
    displaySources();
});
