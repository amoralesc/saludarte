// require("jquery");
// require("datatables.net-dt")();

var $ = require("jquery");
var dt = require("datatables.net")(window, $);

$(document).ready(function () {
  $("#users-datatable").DataTable({
    language: {
      url: "../static/datatables.es-ES.json",
    },
    // Disable sorting on the 7th column (actions)
    columnDefs: [
      {
        searchable: false,
        orderable: false,
        targets: 6,
      },
    ],
  });
});

$(document).ready(function () {
  $("#residents-datatable").DataTable({
    language: {
      url: "../static/datatables.es-ES.json",
    },
    // Disable sorting on the 4th column (actions)
    columnDefs: [
      {
        searchable: false,
        orderable: false,
        targets: 3,
      },
    ],
  });
});
