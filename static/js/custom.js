
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

        $(document).ready(function() {
            $('#configMenu a').on('click', function(e) {
                e.preventDefault();
                $('#configMenu a').removeClass('active');
                $(this).addClass('active');
                $('.content').removeClass('active');
                $($(this).data('target')).addClass('active');
            });
        });
