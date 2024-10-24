document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.content');
    const activeSection = localStorage.getItem('activeSection') || '#config1';

    function showSection(target) {
        sections.forEach(section => section.classList.remove('active'));
        document.querySelector(target).classList.add('active');
    }

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const target = this.getAttribute('data-target');
            showSection(target);
            localStorage.setItem('activeSection', target);
        });
    });

    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(event) {
            const activeForm = this.closest('.content').id;
            localStorage.setItem('activeSection', `#${activeForm}`);
            // No se usa event.preventDefault() aquí para permitir que el formulario se envíe
        });
    });

    showSection(activeSection);
});
