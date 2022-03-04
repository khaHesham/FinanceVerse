
var DeletingBtn=document.getElementById("Deleting");
var LockBtn=document.getElementById("Update")


var DeletingIcon=document.getElementById("DeleteIcon");
var PassIcon=document.getElementById("LockIcon")


function DeletingClick(){

    DeletingBtn.style.display="block";
    LockBtn.style.display="none";

    DeletingIcon.style.color=("#103b67");
    PassIcon.style.color=("White");
    DeletingIcon.style.fontSize=("30px");
    PassIcon.style.fontSize=("20px");

}

function PassClick(){

    DeletingBtn.style.display="none";
    LockBtn.style.display="block";
    DeletingIcon.style.color=("white");
    PassIcon.style.color=("#103b67");
    DeletingIcon.style.fontSize=("20px");
    PassIcon.style.fontSize=("30px");

}

function CheckPassword(){
    let password=document.getElementById("password").value;
    let cnfrmPassword=document.getElementById("Confirm_password").value;
    let message=document.getElementById("msg");
    if(password.length !=0)
      if(password==cnfrmPassword)
      {
        message.textContent="passwords match";
        message.style.background="#3ae374";
      }
      else{
        message.textContent="passwords don't match";
        message.style.background="#ff4d4d";
      }
      else {
          alert("password can't be null")
      }

}
