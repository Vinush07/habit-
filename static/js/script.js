// Add smooth animations and interactions
document.addEventListener('DOMContentLoaded', function() {
    // Add stagger animation to habit cards
    const habitCards = document.querySelectorAll('.habit-card');
    habitCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
    
    // Add click animation to buttons
    const buttons = document.querySelectorAll('.habit-button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
    
    // Add progress bar animation on summary page
    const progressFill = document.querySelector('.progress-fill');
    if (progressFill) {
        const targetWidth = progressFill.style.width;
        progressFill.style.width = '0%';
        setTimeout(() => {
            progressFill.style.width = targetWidth;
        }, 500);
    }
    
    // Add floating animation to hero icon
    const heroIcon = document.querySelector('.hero-icon');
    if (heroIcon) {
        setInterval(() => {
            heroIcon.style.transform = 'translateY(-5px)';
            setTimeout(() => {
                heroIcon.style.transform = 'translateY(0)';
            }, 1000);
        }, 2000);
    }
    
    // Add particle effect on completed habits
    function createParticles(element) {
        for (let i = 0; i < 6; i++) {
            const particle = document.createElement('div');
            particle.style.position = 'absolute';
            particle.style.width = '4px';
            particle.style.height = '4px';
            particle.style.backgroundColor = '#4ecdc4';
            particle.style.borderRadius = '50%';
            particle.style.pointerEvents = 'none';
            particle.style.zIndex = '1000';
            
            const rect = element.getBoundingClientRect();
            particle.style.left = rect.left + rect.width / 2 + 'px';
            particle.style.top = rect.top + rect.height / 2 + 'px';
            
            document.body.appendChild(particle);
            
            const angle = (i / 6) * Math.PI * 2;
            const distance = 50;
            const x = Math.cos(angle) * distance;
            const y = Math.sin(angle) * distance;
            
            particle.animate([
                { transform: 'translate(0, 0) scale(1)', opacity: 1 },
                { transform: `translate(${x}px, ${y}px) scale(0)`, opacity: 0 }
            ], {
                duration: 600,
                easing: 'ease-out'
            }).addEventListener('finish', () => {
                particle.remove();
            });
        }
    }
    
    // Trigger particles when habit is completed
    const completedCards = document.querySelectorAll('.habit-card.completed');
    completedCards.forEach(card => {
        const button = card.querySelector('.habit-button');
        if (button) {
            button.addEventListener('click', () => {
                if (!card.classList.contains('completed')) {
                    setTimeout(() => createParticles(card), 100);
                }
            });
        }
    });
});
