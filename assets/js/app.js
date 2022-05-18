var $ = require("jquery");
var dt = require("datatables.net")(window, $);

// Users datatable
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
        targets: 7,
      },
    ],
  });
});

// Residents datatable
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

// Medications datatable
$(document).ready(function () {
  $("#medications-datatable").DataTable({
    language: {
      url: "../static/datatables.es-ES.json",
    },
    // Disable sorting on the 2nd and 3rd column (presentations, actions)
    columnDefs: [
      {
        searchable: false,
        orderable: false,
        targets: [1, 2],
      },
    ],
  });
});