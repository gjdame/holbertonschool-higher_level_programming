$(document).ready(function () {
  $('DIV#toggle_header').addClass('red');
  $('DIV#toggle_header').click(function () {
    $('DIV#toggle_header').toggleClass('green');
  });
});
