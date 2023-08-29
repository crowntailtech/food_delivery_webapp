

function showdrivelicensebicycle(){
   
    if(document.getElementById('bicycle').checked==false){
        document.getElementById('display').style.display='block';
    }
    else{
        document.getElementById('display').style.display='none';
    }
}

function showdrivelicensebike(){
    if(document.getElementById('bike').checked==true){
        document.getElementById('display').style.display='block';
        
    }
    else{
        document.getElementById('display').style.display='none';
    }
}

function showdrivelicenseother(){
    if(document.getElementById('other').checked==true){
        document.getElementById('display').style.display='block';
    }
    else{
        document.getElementById('display').style.display='none';
    }
}
function identity(){
    if(document.getElementById('pancard').checked==true) {
        document.getElementById('display2').style.display='block';
    }
    else{
        document.getElementById('display2').style.display='none';
    }
}
function identity1(){
    if(document.getElementById('adharcard').checked==true) {
        document.getElementById('display2').style.display='block';
    }
    else{
        document.getElementById('display2').style.display='none';
    }
}

function identity2(){
    if(document.getElementById('other2').checked==true) {
        document.getElementById('display2').style.display='block';
    }
    else{
        document.getElementById('display2').style.display='none';
    }
}

document.getElementById("display").style.display = "none";
document.getElementById("display2").style.display = "none";


