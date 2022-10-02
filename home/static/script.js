$(document).ready(function(){

    $('#menu').click(function(){
        $(this).toggleClass('fa-times');
        $('header').toggleClass('toggle');
    });

    $( ".btn-submit" ).onclick(function() {
        alert("alert");
      });

    $(window).on('scroll load',function(){

        $('#menu').removeClass('fa-times');
        $('header').removeClass('toogle');

    });
    /*function loadDoc() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML = this.responseText;
          }
        };
        xhttp.open("GET", "ajax_info.txt", true);
        xhttp.send();
*/
var text = [ " a student", " a developer", "Anup Poudel"];
var counter = 0;
var elem = $("#name-container");
const settexttime = setInterval(change, 2000);
function change() {
    elem.fadeOut(function(){
        elem.html(text[counter]);
        counter++;
        if(counter >= text.length) { 
            textassign();
        }
        elem.fadeIn();
       
   
    });
}

function textassign(){
     clearInterval(settexttime);
}




});

