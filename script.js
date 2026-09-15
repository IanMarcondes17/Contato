// Seleciona o botão e o corpo da página
const themeToggleBtn = document.getElementById('theme-toggle');
const body = document.body;

// Função para alternar o tema
themeToggleBtn.addEventListener('click', () => {
    // Alterna a classe 'light-mode' no <body>
    body.classList.toggle('light-mode');

    // Altera o texto do botão de acordo com o tema atual
    if (body.classList.contains('light-mode')) {
        themeToggleBtn.textContent = '☀️ Modo Escuro';
    } else {
        themeToggleBtn.textContent = '🌙 Modo Claro';
    }
});