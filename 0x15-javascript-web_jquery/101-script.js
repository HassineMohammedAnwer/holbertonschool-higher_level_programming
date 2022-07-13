(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').appendTo('<li>Item</li>');
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list li').remove();
    counter();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list li').empty();
  });
})();
