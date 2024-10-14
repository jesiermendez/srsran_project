
        function showSection(sectionId) {
            const sections = document.querySelectorAll('.content-section');
            let allHidden = true;
        
            sections.forEach(section => {
                if (section.id === sectionId) {
                    section.style.display = 'block';
                    allHidden = false;
                } else {
                    section.style.display = 'none';
                }
            });
        }    
