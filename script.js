// Seleção dos elementos do Tema
const themeToggleBtn = document.getElementById('theme-toggle');
const body = document.body;

themeToggleBtn.addEventListener('click', () => {
    body.classList.toggle('light-mode');
    if (body.classList.contains('light-mode')) {
        themeToggleBtn.textContent = '☀️ Modo Escuro';
    } else {
        themeToggleBtn.textContent = '🌙 Modo Claro';
    }
});

// Captura do Formulário e redirecionamento de mensagem
const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', (e) => {
    e.preventDefault(); // Impede o recarregamento da página

    const nome = document.getElementById('cliente-nome').value;
    const whatsapp = document.getElementById('cliente-whatsapp').value;
    const servico = document.getElementById('cliente-servico').value;

    // Formata a mensagem para o WhatsApp do Desenvolvedor
    const mensagem = `Olá! Meu nome é ${nome} (${whatsapp}). Gostaria de um orçamento para: ${servico}.`;
    const urlWhatsapp = `https://wa.me/5512996855884?text=${encodeURIComponent(mensagem)}`;

    // Abre o WhatsApp com a mensagem pronta
    window.open(urlWhatsapp, '_blank');
});