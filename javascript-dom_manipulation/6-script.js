// Fetch the Star Wars character and display the name in the #character div
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.getElementById('character').textContent = data.name;
  })
  .catch(error => {
    document.getElementById('character').textContent = 'Error fetching character';
    console.error('Fetch error:', error);
  });
