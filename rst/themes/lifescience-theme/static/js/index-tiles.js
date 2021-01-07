$(document).ready(function() {
    $(".tile-click").click(function(){
        window.location=$(this).find("a.tile-click-url").attr("href"); 
        return false;
    });
});
