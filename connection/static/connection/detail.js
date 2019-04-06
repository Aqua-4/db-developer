/**Detail-view */

$(document).ready(function () {
  loading("#table_placeholder")
  ajax_call("query?query=show tables").done(function (data) {
    $("#query_op").val(JSON.stringify(data.data))
    bs_table(data.data)

  })
})



$('body')
  .on('click', '#submit_btn', function () {
    loading("#table_placeholder")
    var query = $("#query_ip").val()
    ajax_call("query?query=" + query).done(function (data) {
      if (typeof (data.data) == "string") {
        data.data = $.parseJSON(data.data)
      }
      $("#query_op").val(JSON.stringify(data.data))
      bs_table(data.data,query)

    }).fail(function () {
      $('.alert').show()
    })
  })
  .on('keydown', '#query_ip', function (e) {
    if (e.ctrlKey && e.keyCode == 13) {
      // Ctrl-Enter pressed
      $("#submit_btn").trigger('click');
    }
  });


function bs_table(data,query="Show Tables") {
  $('.alert').hide()
  var commentTemplate = document.getElementById("table_template").innerHTML;
  //create template function
  var templateFn = _.template(commentTemplate);
  var templateHTML = templateFn({ 'data': data, 'columns': _.keys(data[0]) });
  $("#table_placeholder").html(templateHTML)
  $('#table_caption').text(query)

}