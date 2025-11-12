// JavaScript for The Hitchhiker's Guide to History
// Additional interactive features can be added here

document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Account for fixed navbar
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add highlight to active navigation link based on URL hash
    function highlightActiveNav() {
        const hash = window.location.hash;
        const navLinks = document.querySelectorAll('.culture-link');
        
        navLinks.forEach(link => {
            if (link.getAttribute('href') === hash) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }
    
    // Initial highlight
    highlightActiveNav();
    
    // Listen for hash changes
    window.addEventListener('hashchange', highlightActiveNav);
    
    // Add any other initialization code here
});