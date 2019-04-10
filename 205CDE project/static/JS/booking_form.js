function checkDate() { /**Check if date is within the up coming 6 months**/
  var bd = document.getElementById("bookingDate").value;
  var bd = new Date(bd);
  var bd = new Date(bd.getFullYear(), bd.getMonth(), bd.getDate()); /**get booking date value and change to date format**/
  
  var getToday = new Date();
  
  var latest_day = new Date(getToday);
  latest_day.setMonth(getToday.getMonth() + 6);  /**set latset date to 6 months ahead of today**/

  var alertDate = document.getElementById("alertDate");

  if(bd <= getToday){  /**compare date**/
  
      alertDate.style.display = "block";
      alertDate.innerHTML="Please select a future date!";}
  
  else if(bd > latest_day){
    	
    alertDate.style.display = "block";  
    alertDate.innerHTML="Please select a date within 6 months!";
    }
    else{
        alertDate.style.display = "none";
    }
    checkAlertBox();
    
}

function checkNum() {
    var num = document.getElementById("participantNum").value;
    var alertNum = document.getElementById("alertNum");
    if (num < 5){
        alertNum.style.display = "block"; 
        alertNum.innerHTML = "Please reservate with at least 5 people";
    }else {
        alertNum.style.display = "none"; 
    }
    checkAlertBox();
}

function checkTime() {
    
    var start = document.getElementById("bookingStartTime").value;
    var end = document.getElementById("bookingEndTime").value;
    var alertTime = document.getElementById("alertTime");
  
    var ST = start.split(":");
    var ET = end.split(":");
  
    var startH = ST[0];  /*** Separtate the data to starting hour/ starting min/ ending hour/ ending min ***/
    var startM = ST[1];
    var endH = ET[0];
    var endM = ET[1];
    if(endH == '00') {endH = 24}
  
	if (startH == "" || startM == "" || endH == "" || endM == ""){ /**Check for missing input**/
		alertTime.style.display = "block"; 
        alertTime.innerHTML = "invalid time range";}
    
	else if(startM != "00" || endM != "00" ) {  /**Check for time range to be each hour as unit**/
		alertTime.style.display = "block"; 
        alertTime.innerHTML = "Please select on an hourly basis";}
    
    else if(Number(startH) < 8 || (Number(endH)>0 && Number(endH)<8 )) {  /**time range within working hour**/
		alertTime.style.display = "block"; 
        alertTime.innerHTML = "Our time available is 08:00 - 24:00";}

    else if(startH >= endH) {  /**End time must be greater than Start time**/
		alertTime.style.display = "block"; 
        alertTime.innerHTML = "Start time must not be greater than or equal to End time";}
    
    else if((Number(startH)+3) > Number(endH)) {  /**booking must for at least 3 hours**/
		alertTime.style.display = "block"; 
        alertTime.innerHTML = "Please select a time range for minimum 3 hours";} 
    else {
        alertTime.style.display = "none";
    }
    
    checkAlertBox();
}
    

function showMenu() { /**Only enable menu choice if Catering Service Checkbox is clicked**/
    var catering = document.getElementById("cateringService");
    if (catering.checked == true){
        document.getElementById("menuA").disabled= false;
        document.getElementById("menuB").disabled= false;
        document.getElementById("menuC").disabled= false;
        
    } else {
        document.getElementById("menuA").disabled= true;
        document.getElementById("menuB").disabled= true;
        document.getElementById("menuC").disabled= true;
    }
    
}

function showMenuAmtA(){
    var clicked = document.getElementById("menuA");
    if (clicked.checked == true){
        document.getElementById("menuAamt").disabled= false;
        
    } else {
        document.getElementById("menuAamt").disabled= true;
    }
    
}

function showMenuAmtB(){
    var clicked = document.getElementById("menuB");
    if (clicked.checked == true){
        document.getElementById("menuBamt").disabled= false;
        
    } else {
        document.getElementById("menuBamt").disabled= true;
    }
}

function showMenuAmtC(){
    var clicked = document.getElementById("menuC");
    if (clicked.checked == true){
        document.getElementById("menuCamt").disabled= false;
        
    } else {
        document.getElementById("menuCamt").disabled= true;
    }
}


function checkAlertBox(){
    var alNum = document.getElementById("alertNum").style.display;;
    var alDate = document.getElementById("alertDate").style.display;
    var alTime = document.getElementById("alertTime").style.display;

    var submitButton = document.getElementById("submitButton");

    if (alNum == "block" || alDate == "block" || alTime == "block"){
        submitButton.disabled = true;
    }else{
        submitButton.disabled = false;
    }
}
