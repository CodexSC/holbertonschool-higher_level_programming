// 7-script.js
// Fetch and list Star Wars movie titles in the ul#list_movies

document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const movies = data.results;
      const ul = document.getElementById('list_movies');
      movies.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        ul.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error fetching movies:', error);
    });
});
