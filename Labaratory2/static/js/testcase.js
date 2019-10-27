$("button[name='btn_delete_testcase']").click(function() {

    var data = { person_login : $(this).data('testcase_id')}

    $.ajax({
      type: 'POST',
      url: "/testcase_person",
      data: data,
      dataType: "text",
      success: function(resultData) {
          location.reload();
      }
});
});


$("button[name='btn_edit_testcase']").click(function() {

    window.location = "edit_testcase?testcase_id="+$(this).data('testcase_id');

});




