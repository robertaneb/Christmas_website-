const themeButton = document.getElementById('theme-btn');
const bodyElement = document.body;

function toggleTheme() {
    bodyElement.classList.toggle('dark-theme');   
}

themeButton.addEventListener('click', toggleTheme);