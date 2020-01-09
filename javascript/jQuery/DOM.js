$(document).ready(() => {
  const $kids = $('#holder').children();
  $kids.on('click', event => {
    $(event.currentTarget).css('border', '1px solid black');
  });

  $('#parent').on('click', event => {
    $(event.currentTarget).parent().hide();
  });

  $('#siblings').on('click', event => {
    $(event.currentTarget).siblings().css('border', '1px solid black');
  });

  $('.example-class-one').closest('.another-class').css('background-color', 'red');
  $('#next').next().css('background-color', 'red');

  $('.myList').find('li').css('background-color', 'red');
});
