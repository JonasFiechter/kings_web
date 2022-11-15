'use strict';

const headerMenu = document.querySelector('.menu');

function toggleMenu() {
    if (headerMenu.style.display === 'flex') {
        headerMenu.style.display = 'none';
    } else {
        headerMenu.style.display = 'flex';
    }
};