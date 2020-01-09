$(document).ready(() => {
  $('.mouseenter-button').on('mouseenter', () => {
    $('.first-image').hide();
  });
  
  $('.mouseleave-button').on('mouseleave', () => {
    $('.first-image').show();
  });

  $('.change-event-button').on('mouseenter', () => {
    $('.first-image').hide();
  }).on('mouseleave', () => {
    $('.first-image').show();
  });

  $('.current-target-button').on('mouseenter', event => {
    $(event.currentTarget).addClass('button-active');
  }).on('mouseleave', () => {
    $(event.currentTarget).removeClass('button-active');
  });

});
