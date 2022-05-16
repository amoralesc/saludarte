// require("jquery");
// require("datatables.net-dt")();

var $ = require("jquery");
var dt = require("datatables.net")(window, $);

$(document).ready(function () {
  $("#datatable").DataTable({
    language: {
      url: '../static/datatables.es-ES.json'
    }
  });
});
