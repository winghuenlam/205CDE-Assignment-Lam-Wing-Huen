function checkFirstName(name){ /**check if first name is letters and space**/
    var letters = /^[a-zA-Z\s]*$/;  
    var alertFirst = document.getElementById("alertFirstName");
    
    if(name.value.match(letters) || name.value==""){
        alertFirst.style.display = "none";
        /**trim and remove extra spaces**/
        var input2 = name.value;
        input2 = input2.replace(/\s\s+/g, ' ');
        name.value = input2.trim();
    }else{
        alertFirst.innerHTML="First name should only consists of letters and space.";
        alertFirst.style.display = "block";
    }   
    checkAlertBox()
}


function checkLastName(name){ /**check if last name is letters**/
    var letters = /^[A-Za-z]+$/;
    var alertLast = document.getElementById("alertLastName");
    
    name.value = name.value.trim();
    
    if(name.value.match(letters) || name.value==""){
        alertLast.style.display = "none";
    }else{
        alertLast.innerHTML="Last name should only consists of letters.";
        alertLast.style.display = "block";
    }   
    checkAlertBox()
    
}

function checkUsername(name){
    var rule = /^[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]+$/; /**must start with a letter, end with numbers or letters, can have "_" or "-" in between**/
    var alertUsername = document.getElementById("alertUsername");
    
    if(name.value.match(rule) && name.value.length >= 5 && name.value.length <=20 || name.value==""){ /**must also be between 5 to 20 characters**/
        alertUsername.style.display = "none";
    }else{
        alertUsername.style.display = "block";
    }
    checkAlertBox()
}

function checkPassword(pw){
    var rule1 = /^\S*[A-Za-z]+\S*[0-9]+\S*$/; 
    var rule2 = /^\S*[0-9]+\S*[A-Za-z]+\S*$/;
    var alertSetPassword = document.getElementById("alertSetPassword");
    var valid = false;
    
    if(pw.value.match(rule1) || pw.value.match(rule2)){ /**rule1 rule2 : must have numbers and letters**/
       valid = true;
       }
    
    if(valid == true && pw.value.length >= 8 && pw.value.length <=16 || pw.value==""){ /**must also be between 8 to 16 characters**/
        alertSetPassword.style.display = "none";
    }else{
        alertSetPassword.style.display = "block";
    }
    
    checkConfirmPW();
    checkAlertBox()
}

function checkConfirmPW(){ /**check if confirmed password == password set**/
    var setPW = document.getElementById("setPassword").value;
    var alertConfirmPW = document.getElementById("alertConfirmPW");
    var confirmPW = document.getElementById("confirmPassword").value;
    
    if(confirmPW == setPW || confirmPW == ""){ 
        alertConfirmPW.style.display = "none";
    }else{
        alertConfirmPW.style.display = "block";
    }
    checkAlertBox()
}

function checkAlertBox(){
    var alFName = document.getElementById("alertFirstName").style.display;
    var alLName = document.getElementById("alertLastName").style.display;
    var alUsername = document.getElementById("alertUsername").style.display;
    var alSetPW = document.getElementById("alertSetPassword").style.display;
    var alConfirmPW = document.getElementById("alertConfirmPW").style.display;

    var submitButton = document.getElementById("submitButton");

    if (alFName == "block" || alLName == "block" || alUsername == "block" 
        || alSetPW == "block" || alConfirmPW == "block"){
        
        submitButton.disabled = true;
    }else{
        submitButton.disabled = false;
    }

}

