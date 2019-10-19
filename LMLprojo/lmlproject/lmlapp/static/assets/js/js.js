




var yesscheckbox = document.getElementById('yes');
var nocheckbox = document.getElementById('no');
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

var university = document.getElementsByClassName("uni");
var uniselect = document.getElementsByClassName("uniselect");
var graduationdate = document.getElementsByClassName("graduation");
    function showItems() {
        var i,p,m,d,c,b,u,g;
        for(i=0; i<uniselect.length; i++){
            for(p=0; p<phd.length; p++){
                for(m=0; m<masters.length; m++){
                    for(d=0; d<diploma.length; d++){
                        for(c=0; c<certificate.length; c++){
                            for(b=0; b<bachelor.length; b++){
                                for(u=0; u<university.length; u++){
                                    for(g=0; g<graduationdate.length; g++){
                                        if(uniselect[i].options[uniselect[i].selectedIndex].value === 'Phd'){
                                            phd[p].style.display="block";
                                            graduationdate[g].style.display="block";
                                            university[u].style.display="block";
                                            if( masters[m].style.display==="block" ||  diploma[d].style.display==="block" || certificate[c].style.display==="block" || bachelor[b].style.display ==="block"){
                                                    masters[m].style.display="none";
                                                    diploma[d].style.display="none";
                                                    certificate[c].style.display="none";
                                                    bachelor[b].style.display="none";
                                            }

                                        }
                                        if(uniselect[i].options[uniselect[i].selectedIndex].value === 'Masters'){
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
                                        if(uniselect[i].options[uniselect[i].selectedIndex].value === "Bachelor"){
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
                                        if(uniselect[i].options[uniselect[i].selectedIndex].value === "Diploma"){
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
                                        if(uniselect[i].options[uniselect[i].selectedIndex].value === "Certificate"){
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











    // function showPhd(){
    //     phd.style.display="block";
    //     if( masters.style.display==="block" ||  diploma.style.display==="block" || certificate.style.display==="block"){
    //             masters.style.display="none";
    //             diploma.style.display="none";
    //             certificate.style.display="none";
    //     }
    // }
    // function showMasters(){
    //     masters.style.display="block";
    //      if( phd.style.display==="block" ||  diploma.style.display==="block" || certificate.style.display==="block"){
    //             phd.style.display="none";
    //             certificate.style.display="none";
    //             diploma.style.display="none";
    //     }
    // }
    // function showDiploma(){
    //     diploma.style.display="block";
    //      if( phd.style.display==="block" ||  masters.style.display==="block" || certificate.style.display==="block"){
    //             phd.style.display="none";
    //             certificate.style.display="none";
    //              masters.style.display="none";
    //     }
    // }
    // function showCertificate(){
    //     certificate.style.display="block";
    //     if( phd.style.display==="block" ||  masters.style.display==="block" || diploma.style.display==="block"){
    //             phd.style.display="none";
    //             diploma.style.display="none";
    //             masters.style.display="none";
    //     }
    // }

var employer = document.getElementsByClassName('employer');
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
            reader.onload = function (e) {
                $('.blah').attr('src', e.target.result).css('visibility', 'visible');
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
      linkElement: 'a:not([target="_blank"]):not([href^="#"]):not([class^="chosen-single"])',
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










