// Hello 
$(function(){
    $('form').on('submit',function(event){
        event.preventDefault();

        const process = () => {
        
            function isValidEmail(email) {
                var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                return re.test(String(email).toLowerCase());
            }
    
            if( isValidEmail($('.email').val()) ){
                $('.email').attr('disabled','true');
                $('.submit').html("Please wait...");
                setTimeout(() => {
                    $('.submit').html("Joined");
                    $('.email').attr('disabled','false');
                    $('.email').val('');
                    next();
                }, 5000);
            }
    
            const next = () => {
                $('.email').html("Joined");
                setTimeout(() => {
                    // window.location.href = '/';
                }, 2000);
            }
        }

        $('.email').on('submit', $('.submit').trigger('click'))
        $('.submit').on('click', process)
    })
})
console.log('Hello')