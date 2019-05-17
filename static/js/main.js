$('#send-form').submit(function () {

  var text = $('#chat-input').val();

  $.post('/rooms/{{ room_id }}/messages/', { from: nick, text: text }

  ).done(function (data) {

    console.log('send response: ' + JSON.stringify(data));

  }).fail(function () {

    alert('failed to send message');

  });

  return false;

});

// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}

// Change style of navbar on scroll
window.onscroll = function() {myFunction()};
function myFunction() {
    var navbar = document.getElementById("myNavbar");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        navbar.className = "w3-bar" + " w3-card" + " w3-animate-top" + " w3-white";
    } else {
        navbar.className = navbar.className.replace(" w3-card w3-animate-top w3-white", "");
    }
}

// Used to toggle the menu on small screens when clicking on the menu button
function toggleFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}


var img=document.getElementById('turnImg');  
var angle=0;
setInterval(function(){
    img.style.transform="rotateZ("+ angle++ +"deg)";
}, 30);