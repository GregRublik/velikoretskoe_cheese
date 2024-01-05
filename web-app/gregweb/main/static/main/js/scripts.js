$(document).ready(function() {
  $(".method_obtaining").change(function() {

    if ($('#fid-2').prop("checked")) {
      $('#hide1').fadeIn(300);
    } else {
      $('#hide1').fadeOut(300);
    }

  });
  $(".method_obtaining").change(function() {

    if ($('#fid-1').prop("checked")) {
      $('#hide2').fadeIn(300);
    } else {
      $('#hide2').fadeOut(300);
    }

  });
});