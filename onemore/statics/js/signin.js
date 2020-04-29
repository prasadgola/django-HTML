function validateform()
{  
// var name=document.myform.email.value;  
// var password=document.myform.pass.value;  
  
if (username.value==null || username.value=="")
{  
  alert("Please enter the username");  
  return false;  
}else if(password.value==null || password.value=="")
{  
  alert("Please enter the password");  
  return false;  
}  
} 