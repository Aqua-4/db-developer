/**Detail-view */

var connection_conifg = ajax_call("/static/connection/detail_config.json", false).done().responseJSON
const var_str = "$var$"

$(document).ready(function () {
  connection_conifg = connection_conifg[connection_type]
  make_query(connection_conifg.tables)
})

$('body')
  .tooltip({
    selector: '[data-toggle="tooltip"]',
    container: 'body',
    animation: true,
    html: true,
    trigger: 'click',
    placement: 'auto'
  })
  .on('click', '#submit_btn', function () {
    if ($("#query_ip").val() != "")
      make_query($("#query_ip").val())
  })
  .on('keydown', '#query_ip', function (e) {
    if (e.ctrlKey && e.keyCode == 13) {
      // Ctrl-Enter pressed
      $("#submit_btn").trigger('click');
    }
  });


function make_query(query) {
  loading("#table_placeholder")
  ajax_call("query?query=" + query).done(function (data) {
    if (typeof (data.data) == "string") {
      data.data = $.parseJSON(data.data)
    }
    $("#query_op").val(JSON.stringify(data.data))
    bs_table(data.data, query)

  }).fail(function () {
    $('.alert').show()
  })
}

function bs_table(data, query) {
  $('.alert').hide()
  var commentTemplate = document.getElementById("table_template").innerHTML;
  //create template function
  var templateFn = _.template(commentTemplate);
  var templateHTML = templateFn({ 'data': data, 'columns': _.keys(data[0]), 'tables': (query == connection_conifg.tables) });
  $("#table_placeholder").html(templateHTML)
  $('#table_caption').text(query)

}


function html_tip(table_name, header = "Table ops") {
  var ops = connection_conifg.table_ops
  var op = "<div class='bg-color tip border-radius text-dark pr-3'>"
  op += "<p class='h4 mb-0 py-2 text-uppercase text-center border border-white border-top-0 border-left-0 border-right-0 border-bottom' >"
  op += "<span class='d-block sm3'>" + header + "</span> </p >"
  op += " <ul class='list-unstyled h3 pt-2 pb-4 pl-3 mb-0 text-left'> "
  _.each(ops, function (v, k) {
    op += "<button class='btn btn-outline-info query-table' query='" + v.replace(var_str, table_name) + "'>  " + k + "</button >"
  })
  op += "</ul>"
  op += "</div>"
  return op

}