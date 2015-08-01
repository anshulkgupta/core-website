$(document).ready(function() {
	console.log("Welcome to the CORE website!");

	// Team page manipulation
	$(".team-card-square").find(".team-bio").hide()

	$(".team-card-square").click(function(e) { 
	   // bio not yet entered
	   if($(this).find(".team-bio").html().length < 25)
	   	return;

       $(this).find(".team-pic").toggle();
       $(this).find(".team-title").toggle();
       $(this).find(".team-byline").toggle();
       $(this).find(".team-bio").toggle();
    });

    $(".team-socialmedia").click(function(e) {
    	console.debug(e);
    	e.stopPropagation();
    });
});