
var disability = document.getElementsByClassName('des')[0];
    function openDisability() {
        disability.style.display="block";
        disability.setAttribute('required','required');
    }
    function closeDisability() {
        disability.style.display="none";
    }





    // $(document).ready(function() {
    //     $("#submitbutton").attr('disabled',function () {
    //          $(this).on("click", function () {
    //             alert("Accept to terms and conditions to proceed");
    //         });
    //
    //          $('#termscheck:first-child').on('click', function () {
    //             if($(this).checked === true){
    //                 $('#submitbutton').removeAttr("disabled");
    //             }else if($(this).checked === false){
    //                 $("#submitbutton").attr('disabled','disabled');
    //                 alert("Accept to terms and conditions to proceed");
    //             }
    //
    //          })
    //         // if (typeof attr !== typeof undefined && attr !== false) {
    //         //     // ...
    //         // }
    //     });
    // });

// function openSubmit() {
//     var submitbutton = document.getElementsByClassName('submitbutton')[0];
//     var termscheck = document.getElementsByClassName('termscheck')[0];
//     var attr = submitbutton.getAttributeNode("disabled");
//
//
//     if(termscheck.checked === true){
//         submitbutton.removeAttribute("disabled");
//     }else {
//         submitbutton.setAttribute("disabled", "disabled");
//
//     }
// }

function showEducation(data) {
        var y = document.getElementById(data.id);
        var x = y.parentElement;

        if (y.value === 'Phd') {
            x.children[2].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if (x.children[3].style.display === "block" || x.children[5].style.display === "block" || x.children[6].style.display === "block" || x.children[4].style.display === "block") {
                x.children[3].style.display = "none";
                x.children[5].style.display = "none";
                x.children[6].style.display = "none";
                x.children[4].style.display = "none";
            }
        }
        else if (y.value === 'Masters') {
            x.children[3].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if (x.children[2].style.display === "block" || x.children[5].style.display === "block" || x.children[6].style.display === "block" || x.children[4].style.display === "block") {
                x.children[2].style.display = "none";
                x.children[6].style.display = "none";
                x.children[5].style.display = "none";
                x.children[4].style.display = "none";
            }
        }
        else if (y.value === "Bachelor") {
            x.children[4].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if (x.children[2].style.display === "block" || x.children[5].style.display === "block" || x.children[6].style.display === "block" || x.children[3].style.display === "block") {
                x.children[2].style.display = "none";
                x.children[6].style.display = "none";
                x.children[5].style.display = "none";
                x.children[3].style.display = "none";
            }
        }
        else if (y.value === "Diploma") {
            x.children[5].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if (x.children[2].style.display === "block" || x.children[3].style.display === "block" || x.children[6].style.display === "block" || x.children[4].style.display === "block") {
                x.children[2].style.display = "none";
                x.children[6].style.display = "none";
                x.children[3].style.display = "none";
                x.children[4].style.display = "none";
            }
        }
        else if (y.value === "Certificate") {
            x.children[6].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if ( x.children[2].style.display === "block" || x.children[3].style.display === "block" || x.children[5].style.display === "block" || x.children[4].style.display === "block") {
                x.children[2].style.display = "none";
                x.children[5].style.display = "none";
                x.children[3].style.display = "none";
                x.children[4].style.display = "none";
            }
        }

}




    function showEmployment() {
        var clonebutton1 = document.getElementById('clonebutton1');
        var clonebutton2 = document.getElementById('clonebutton2');
        var employer = document.getElementsByClassName('employerwrapper');

         for(i=0; i<employer.length; i++){
            employer[i].style.display="block";
            // employer[i].setAttributeNode('required')[i]
            // employer[i].getElementsByTagName('textarea')[i].setAttribute('required','required');

         }

         // for(x=0; x<employer.length; x++){
         //    employer[x].getElementsByTagName('input')[x].setAttribute('required','required');
         // }
        clonebutton1.style.display = "block";
        clonebutton2.style.display = "block";
    }
    function hideEmployment() {
        var clonebutton1 = document.getElementById('clonebutton1');
        var clonebutton2 = document.getElementById('clonebutton2');
        var employer = document.getElementsByClassName('employerwrapper');

        for(i=0; i<employer.length; i++){
            employer[i].style.display="none";

        }
         clonebutton1.style.display = "none";
         clonebutton2.style.display = "none";
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




// (function ($) {
//     // USE STRICT
//     "use strict";
//     $(".animsition").animsition({
//       inClass: 'fade-in-left',
//       outClass: 'fade-out-right',
//       inDuration: 900,
//       outDuration: 900,
//       linkElement: 'a:not([target="_blank"]):not([href^="#"]):not([class^="chosen-single"]):not([class^="not_a_link"]) textarea:not([class^="form-control"])',
//       loading: true,
//       loadingParentElement: 'html',
//       loadingClass: 'Loader-bg',
//       loadingInner: '<div class="loader">' +
//                           '<span></span>' +
//                           '<span></span>' +
//                           '<span></span>' +
//                           '<span></span>' +
//                       '</div>',
//       timeout: false,
//       touchSupport  :   true,
//       timeoutCountdown: 5000,
//       onLoadEvent: true,
//       browser: ['animation-duration', '-webkit-animation-duration'],
//       overlay: false,
//       overlayClass: 'animsition-overlay-slide',
//       overlayParentElement: 'body',
//       transition: function (url) {
//         window.location.href = url;
//       }
//     });
//
//
//   })(jQuery);








