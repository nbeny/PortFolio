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