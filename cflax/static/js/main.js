$(document).ready(function(){
    $('.toggle-menu').click(()=>{
        $('.nav-bar').toggleClass('active')
    });
        window.addEventListener('resize', ()=>{
            if(window.innerWidth<500){
                $('ul li').click(function(){
                    $(this).siblings().removeClass("active");
                    $(this).toggleClass("active");
            
                });
            }
        });
        $('ul li').click(function(){
            if(window.innerWidth<500){
                    $(this).siblings().removeClass("active");
                    $(this).toggleClass("active");
            }
        })
});  
