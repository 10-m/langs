$(document).ready(() => {
  $('.css-button').on('click', event => {
    $(event.currentTarget).css('background-color', 'red');
  });

  $('.css2-button').on('click', event => {
    $(event.currentTarget).css({
      backgroundColor: 'red',
      width: '200px'
    });
  });
  
  $('.animate-button').on('click', event => {
    $(event.currentTarget).animate({
      width: '200px',
      height: '50px'
    }, 'slow');
  });

  $('.add_class-button').on('click', event => {
    $(event.currentTarget).addClass('button-active');
  });

  $('.remove_class-button').addClass('button-active');
  $('.remove_class-button').on('click', event => {
    $(event.currentTarget).removeClass('button-active');
  });

  $('.toggle_class-button').on('click', event => {
    $(event.currentTarget).toggleClass('button-active');
  });

});
