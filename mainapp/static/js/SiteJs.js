



function toggleSidebar()
{
   document.getElementById('toggle-btn').classList.toggle('active');
   document.getElementById('aside').classList.toggle('active');
   document.getElementById('block_content').classList.toggle('active');
  
}
function topFunction()
{
 // 
    document.body.scrollTop =0;
    document.documentElement.scrollTop=0;
    

}


  
$(function()
{

   var b =document.body || document.getElementsByTagName('body')[0];

   document.getElementById("toTop").setAttribute("style","display:none;position:fixed;bottom:18px;z-index:1000;border:none;outline:none;background:none;cursor:pointer;");
   document.documentElement.setAttribute("style","scroll-behavior:smooth;");
  

   $(window).scroll(function(){scrollFunction()})
    function scrollFunction () 
    {
      let t = document.getElementById("toTop");
      if(document.body.scrollTop>480 ||document.documentElement.scrollTop>480)
      {

        t.style.display="block";
      }
      else
        {
          t.style.display="none";
        }
    }
  
  
   
   
   
   
   $('.content').click(function(){

    $('#aside').removeClass('active');
  
    $('.toggle-btn').removeClass('active');
    $('.block_content').removeClass('active');

 });
	
    

});

$(document).ready(function(){
   $('a[href^="#"]').on("click", function(e){
       var anchor = $(this);
       $('html, body').stop().animate({
           scrollTop: $(anchor.attr('href')).offset().top
       }, 777);
       e.preventDefault();
       return false;
   });
});

