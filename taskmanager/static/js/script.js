document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
    
    // datepicker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy",
      i18n: {done: "select"}
    });

    // select initialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
  });