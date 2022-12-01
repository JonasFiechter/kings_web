`use strict`;

const currentPageGen = window.location.href.split('/');
const currentPage = currentPageGen[currentPageGen.length - 2];
const nav1 = document.getElementById('nav-1');
const nav2 = document.getElementById('nav-2');
const nav3 = document.getElementById('nav-3');


function dynamicMenu(page) {
    if (currentPage === 'home') {
        nav1.classList.add('hidden');
    } else if (currentPage === 'profile') {
        nav2.classList.add('hidden');
    } else {
        nav3.classList.add('hidden');
    }
};

dynamicMenu(currentPage);