// Card animation
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.transform = 'translateY(0)';
            card.style.opacity = '1';
        }, 300 * index);
    });
});

// Three.js and Vanta.js
document.addEventListener('DOMContentLoaded', () => {
    VANTA.NET({
        el: '#intro-card',
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 200.0,
        minWidth: 200.0,
        scale: 1.0,
        scaleMobile: 1.0,
        color: '#e63946',
        backgroundColor: '#171717',
        points: 20.0,
    });
});