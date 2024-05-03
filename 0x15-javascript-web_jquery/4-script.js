/*
 * toggles class in header using JQuery
 */

$(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
