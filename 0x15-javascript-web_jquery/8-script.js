$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const d = data.results;
  for (i = 0; i < d.length; i++) {
    $('UL#list_movies').append('<li>' + d[i].title + '</li>');
  }
});
