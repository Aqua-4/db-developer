/** All common functions here */

function ajax_call(url, async = true) {
  // use get_ajax_call.done(function(data){  <code> })
  return $.ajax({
    url: url,
    async: async,
    method: 'GET',
    // dataType: 'json'
  })
}

function loading(placeholder = 'body', show = true) {
  // $(placeholder).empty()
  $(placeholder).html('<img class="loading-icon" src="/static/connection/loader.gif" alt="Loading..."></img>')
}