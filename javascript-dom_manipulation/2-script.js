// When the user clicks the element with id 'red_header', add the 'red' class to the header element

document.getElementById('red_header').onclick = function () {
    document.querySelector('header').classList.add('red');
};
