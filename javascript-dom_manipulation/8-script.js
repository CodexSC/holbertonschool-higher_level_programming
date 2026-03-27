// Ensure the script runs after the DOM is fully loaded
window.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      document.getElementById('hello').textContent = 'Error fetching greeting';
      console.error('Fetch error:', error);
    });
});
