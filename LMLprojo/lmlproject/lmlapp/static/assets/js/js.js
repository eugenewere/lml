


function openSubmit() {
    var submitbutton = document.getElementById('submitbutton');
    var termscheck = document.getElementById("termschecks");

    if(termscheck.checked === true){
        submitbutton.style.visibility = "visible";
    }else {
        submitbutton.style.visibility = "hidden";
    }

}

// var yesscheckbox = document.getElementById('yes');
// var nocheckbox = document.getElementById('no');
var disability = document.getElementById('disability');
    function openDisability() {
        disability.style.display="block";
    }
    function closeDisability() {
        disability.style.display="none";
    }


var phd = document.getElementsByClassName("phd");
var masters = document.getElementsByClassName("masters");
var diploma = document.getElementsByClassName("diploma");
var certificate = document.getElementsByClassName("certificate");
var bachelor = document.getElementsByClassName("bachelor");
// var regno = document.getElementsByClassName("regno");

var university = document.getElementsByClassName("uni");
var qualifications = document.getElementsByClassName("qualifications");
var graduationdate = document.getElementsByClassName("graduation");



    function showItem(select) {

       // var i,p,m,d,c,b,u,g;
        for(i=0; i<qualifications.length; i++){
            for(p=0; p<phd.length; p++){
                for(m=0; m<masters.length; m++){
                    for(d=0; d<diploma.length; d++){
                        for(c=0; c<certificate.length; c++){
                            for(b=0; b<bachelor.length; b++){
                                for(u=0; u<university.length; u++){
                                    for(g=0; g<graduationdate.length; g++){
                                        // if(qualifications[i].options[qualifications[i].selectedIndex[i]][i].value[i] === 'Phd'){
                                        if(qualifications[i].value === 'Phd'){
                                            phd[p].style.display="block";
                                            graduationdate[g].style.display="block";
                                            university[u].style.display="block";
                                            if(masters[m].style.display==="block" ||  diploma[d].style.display==="block" || certificate[c].style.display==="block" || bachelor[b].style.display ==="block"){
                                                    masters[m].style.display="none";
                                                    diploma[d].style.display="none";
                                                    certificate[c].style.display="none";
                                                    bachelor[b].style.display="none";
                                            }
                                        }
                                        // if(qualifications[i].options[qualifications[i].selectedIndex[i]][i].value[i] === 'Masters'){
                                        if(qualifications[i].value  === 'Masters'){
                                             masters[m].style.display="block";
                                             graduationdate[g].style.display="block";
                                             university[u].style.display="block";
                                             if( phd[p].style.display==="block" ||  diploma[d].style.display==="block" || certificate[c].style.display==="block" || bachelor[b].style.display ==="block"){
                                                    phd[p].style.display="none";
                                                    certificate[c].style.display="none";
                                                    diploma[d].style.display="none";
                                                    bachelor[b].style.display="none";
                                            }
                                        }
                                        // if(qualifications[i].options[qualifications[i].selectedIndex[i]][i].value[i] === "Bachelor"){
                                        if(qualifications[i].value  === "Bachelor"){
                                            bachelor[b].style.display = "block";
                                            graduationdate[g].style.display = "block";
                                            university[u].style.display="block";
                                            if( phd[p].style.display==="block" ||  diploma[d].style.display==="block" || certificate[c].style.display==="block" || masters[m].style.display ==="block"){
                                                    phd[p].style.display="none";
                                                    certificate[c].style.display="none";
                                                    diploma[d].style.display="none";
                                                    masters[m].style.display="none";
                                            }
                                        }
                                        // if(qualifications[i].options[qualifications[i].selectedIndex[i]][i].value[i] === "Diploma"){
                                        if(qualifications[i].value  === "Diploma"){
                                             diploma[d].style.display="block";
                                             graduationdate[g].style.display="block";
                                             university[u].style.display="block";
                                             if( phd[p].style.display==="block" ||  masters[m].style.display==="block" || certificate[c].style.display==="block" || bachelor[b].style.display ==="block"){
                                                    phd[p].style.display="none";
                                                    certificate[c].style.display="none";
                                                     masters[m].style.display="none";
                                                     bachelor[b].style.display="none";
                                            }
                                        }
                                        // if(qualifications[i].options[qualifications[i].selectedIndex[i]][i].value[i] === "Certificate"){
                                        if(qualifications[i].value  === "Certificate"){
                                            certificate[c].style.display="block";
                                            graduationdate[g].style.display="block";
                                            university[u].style.display="block";
                                            if( phd[p].style.display==="block" ||  masters[m].style.display==="block" || diploma[d].style.display==="block" || bachelor[b].style.display === "block"){
                                                    phd[p].style.display="none";
                                                    diploma[d].style.display="none";
                                                    masters[m].style.display="none";
                                                    bachelor[b].style.display="none";
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }












var employer = document.getElementsByClassName('employer');
var clonebutton1 = document.getElementById('clonebutton1');
var clonebutton2 = document.getElementById('clonebutton2');

    function showEmployment() {
        var i;
        for(i=0; i<employer.length; i++){
            employer[i].style.display="block";

        }

    }
    function hideEmployment() {
        var i;
        for(i=0; i<employer.length; i++){
            employer[i].style.display="none";
        }
    }


function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();
         var disclaimer= document.getElementById("disclaimer");
            reader.onload = function (element) {
                $('.blah').attr('src', element.target.result).css('visibility', 'visible');
                disclaimer.style.visibility = "hidden";
            };
            reader.readAsDataURL(input.files[0]);
            }
        }




(function ($) {
    // USE STRICT
    "use strict";
    $(".animsition").animsition({
      inClass: 'fade-in-left',
      outClass: 'fade-out-right',
      inDuration: 900,
      outDuration: 900,
      linkElement: 'a:not([target="_blank"]):not([href^="#"]):not([class^="chosen-single"]):not([class^="not_a_link"]) textarea:not([class^="form-control"])',
      loading: true,
      loadingParentElement: 'html',
      loadingClass: 'Loader',
      loadingInner: '<div class="page-loader__spin"></div>',
      timeout: false,
      timeoutCountdown: 5000,
      onLoadEvent: true,
      browser: ['animation-duration', '-webkit-animation-duration'],
      overlay: false,
      overlayClass: 'animsition-overlay-slide',
      overlayParentElement: 'html',
      transition: function (url) {
        window.location.href = url;
      }
    });


  })(jQuery);










