// Add a new <li>Item</li> to the ul.my_list when #add_item is clicked

document.getElementById('add_item').onclick = function () {
    const ul = document.querySelector('ul.my_list');
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
};
