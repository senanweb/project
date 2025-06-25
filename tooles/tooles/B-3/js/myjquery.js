$(document).ready(function()
{$(".carousel").carousel({interval:5000}); 
// show tooles
$(".omar").mouseover(function()
{$(".color").fadeToggle();}); 
// change colors
var Sinan = $(".color ul li");
 Sinan
	.eq(0).css("background","#E41b17").end()
	.eq(1).css("background","#68d108").end()
	.eq(2).css("background","#0895D1");
	
 Sinan.click(function()
 {
	 $("link[href*='Colors']").attr("href",$(this).attr("data-value"));	 
 }); 
});

// loading
$(window).ready(function(){
  /*   $(".loading-overlay, .loading-overlay, .spinner").fadeOut(2000); just one line */
  
  $(".loading-overlay .spinner").fadeOut(1000,
	function(){
		$("body").css("overflow","auto");
		$(this).parent().fadeOut(2000,
		function(){
			
			$(this).remove();
		});	 
	});
	
	// go up or down
	var goTop = $(".go-top");
		$(window).scroll(function()
		{if($(this).scrollTop()>=700)
			{goTop.show()}
			else{goTop.hide()}
		});	
		goTop.click(function()
		{$("html,body").animate({scrollTop : 0},600);});
		
	
 });

