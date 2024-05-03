/*
 * adds a list to lists using JQuery
 */

$(function () {
    $('#add_item').click(function () {
	$('ul.my_list').append('<li>Item</li>');
  });
});
