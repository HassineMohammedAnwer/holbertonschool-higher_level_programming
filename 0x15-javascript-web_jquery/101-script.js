window.onload = function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list li').last().remove();
    counter();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list li').remove();
  });
}
