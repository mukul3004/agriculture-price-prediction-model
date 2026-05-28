// AgriPredict AI — Interaction Script

// Dynamic accuracy indicator based on days input
const daysInput = document.getElementById('daysInput');
const accRows = document.querySelectorAll('.acc-row');

if (daysInput) {
    daysInput.addEventListener('input', function () {
        const val = parseInt(this.value) || 0;
        accRows.forEach(r => r.style.opacity = '0.4');
        if (val <= 15 && val > 0) {
            document.querySelector('.acc-high').style.opacity = '1';
        } else if (val <= 30) {
            document.querySelector('.acc-med').style.opacity = '1';
        } else if (val > 30) {
            document.querySelector('.acc-low').style.opacity = '1';
        }
    });
}

// Smooth scroll for nav links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Animate stat cards on scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, { threshold: 0.15 });

document.querySelectorAll('.step-card, .feature-item, .commodity-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(el);
});

// Submit button loading state
const form = document.getElementById('predictForm');
const submitBtn = document.getElementById('submitBtn');
if (form && submitBtn) {
    form.addEventListener('submit', function () {
        submitBtn.querySelector('.btn-label').textContent = 'Running LSTM Model…';
        submitBtn.querySelector('.btn-arrow').textContent = '⟳';
        submitBtn.disabled = true;
        submitBtn.style.opacity = '0.8';
    });
}
<script src="{{ url_for('static', filename='script.js') }}"></script>