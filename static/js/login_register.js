document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('container');
    const CadastrarBtn = document.getElementById('Cadastrar');
    const EntrarBtn = document.getElementById('Entrar');

    CadastrarBtn.addEventListener('click', () => {
        container.classList.add('activate');
    });

    EntrarBtn.addEventListener('click', () => {
        container.classList.remove('activate');
    });
});
