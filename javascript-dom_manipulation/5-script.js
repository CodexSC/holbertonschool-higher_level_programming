// Update the header text to 'New Header!!!' when #update_header is clicked

document.getElementById('update_header').onclick = function () {
    document.querySelector('header').textContent = 'New Header!!!';
};
