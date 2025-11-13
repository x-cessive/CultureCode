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
    
    // Theme management
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
        // Set initial state based on saved preference
        const currentTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        if (currentTheme === 'dark') {
            document.body.classList.add('dark-theme');
            darkModeToggle.checked = true;
        }
        
        // Add event listener if toggle exists
        darkModeToggle.addEventListener('change', function() {
            if (this.checked) {
                document.body.classList.add('dark-theme');
                localStorage.setItem('theme', 'dark');
            } else {
                document.body.classList.remove('dark-theme');
                localStorage.setItem('theme', 'light');
            }
        });
    }
    
    // Add any other initialization code here
});

// Function to set theme (can be called from other parts of the application)
function setTheme(theme) {
    if (theme === 'dark') {
        document.body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark');
        if (window.darkModeToggle) window.darkModeToggle.checked = true;
    } else {
        document.body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light');
        if (window.darkModeToggle) window.darkModeToggle.checked = false;
    }
}

// Function to toggle theme
function toggleTheme() {
    const currentTheme = localStorage.getItem('theme');
    setTheme(currentTheme === 'dark' ? 'light' : 'dark');
}