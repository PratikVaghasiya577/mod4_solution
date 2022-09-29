var names = ["Yaakov", "John", "Jen", "Jason", "Paul", "Frank", "Larry", "Paula", "Laura", "Jim"];
var speaker = {
  hellospeaker: function speak(name) {
    var speakWord = "Hello";
    console.log(speakWord + " " + name)
  },
  byespeaker: function speak(name) {
    var speakWord = "Good bye";
    console.log(speakWord + " " + name)
  }
}

for (name of names){
  if (name[0].toLowerCase()=='j'){
      speaker.byespeaker(name);
  }else{
    speaker.hellospeaker(name);
  }
}
