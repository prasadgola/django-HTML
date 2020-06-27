
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});


function validateform()
{  
  
if (username.value==null || username.value=="")
{  
  alert("Please enter the username");  
  return false;  
}
else if(password.value==null || password.value=="")
{  
  alert("Please enter the password");
  return false;
}
}

function validate()
{
 if(fullname.value=="")
 {
     
     alert("Please Enter your name")
     return false
 }else if(!(/^[a-zA-Z ]+$/).test(fullname.value))
 {
     alert("Name should have only alphabets ")
     return false
 }

 if(email.value=="")
 {
    alert("Please enter Email Id")
    return false
 }

if(dob.value=="")
 {
     alert("enter date of birth")
     return false
 }

 if(mobile.value=="")
 {
     alert("Please enter mobile number")
     return false
 }else if(!(/^[0-9]{10}$/).test(mobile.value))
 {
     alert("Enter proper mobile number")
     return false
 }

  if(pass.value=="")
 {
     alert("Please Enter Password")
     return false 
 }else if(!((/^[A-Za-z0-9@#*&]\w{7,14}\d{1,4}$/)).test(pass.value))
 {
     alert("Password should contain atleast 7-14 characters and 1-4 digits")
    return false
 }
 else if(rpass.value=="")
 {
     alert("Please Comfirm Password")
     return false 
 }
 else if(rpass.value!=pass.value)
 {
     alert("Password did not match")
     return false
 }


}
