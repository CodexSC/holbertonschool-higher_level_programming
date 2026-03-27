// Toggle the class of the header between 'red' and 'green' on click

document.getElementById('toggle_header').onclick = function () {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
};
