$("button[name='btn_delete_function']").click(function() {

    var data = { function_name : $(this).data('function_name')}

    $.ajax({
      type: 'POST',
      url: "/delete_function",
      data: data,
      dataType: "text",
      success: function(resultData) {
          location.reload();
      }
});
});


$("button[name='btn_edit_person']").click(function() {

    window.location = "edit_person?person_login="+$(this).data('person_login');

});


$("button[name='btn_new_person']").click(function() {

    window.location = "new_person";

});

$("button[name='btn_new_function']").click(function() {

    window.location = "new_function/"+$(this).data('person_login');

});
