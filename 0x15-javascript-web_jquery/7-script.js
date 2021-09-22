// fetches and replaces the name of this URL: http://swapi.co/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character

$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (res) {
    $('DIV#character').text(res.name);
  }
});
