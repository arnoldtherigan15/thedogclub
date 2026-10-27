// Mobile menu drawer
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
        const open = mobileMenu.classList.toggle('hidden') === false;
        mobileMenuBtn.setAttribute('aria-expanded', String(open));
    });
}

// Footer year (the old site was stuck on © 2024)
document.querySelectorAll('[data-year]').forEach(el => {
    el.textContent = new Date().getFullYear();
});

// Home: facility tabs
document.querySelectorAll('[data-tab-btn]').forEach(btn => {
    btn.addEventListener('click', () => {
        const key = btn.dataset.tabBtn;
        document.querySelectorAll('[data-tab-btn]').forEach(b => {
            const active = b === btn;
            b.classList.toggle('bg-forest', active);
            b.classList.toggle('text-cream', active);
            b.classList.toggle('bg-beige', !active);
            b.classList.toggle('text-forest', !active);
            b.setAttribute('aria-selected', String(active));
        });
        document.querySelectorAll('[data-tab-panel]').forEach(panel => {
            panel.classList.toggle('hidden', panel.dataset.tabPanel !== key);
        });
    });
});

// Mock forms: no backend in the mockup, show an inline message instead of alert()
document.querySelectorAll('form[data-mock-form]').forEach(form => {
    form.addEventListener('submit', e => {
        e.preventDefault();
        const msg = form.querySelector('[data-form-msg]');
        if (msg) msg.classList.remove('hidden');
        form.reset();
    });
});
