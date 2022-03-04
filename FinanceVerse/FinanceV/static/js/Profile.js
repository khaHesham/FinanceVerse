var PersonalBtn=document.getElementById("profile");
var PaymentBtn=document.getElementById("payment");
var SubscribtionBtn=document.getElementById("subscribtion");
var PrivacyBtn=document.getElementById("privacy");
var SettingsBtn=document.getElementById("settings");
var DeletingBtn=document.getElementById("Deleting");
var LockBtn=document.getElementById("Update")

var PersonalIcon=document.getElementById("ProfileIcon");
var CreditCardIcon=document.getElementById("CreditCardIcon");
var TVIcon=document.getElementById("TVIcon");
var TasksIcon=document.getElementById("TasksIcon");
var SettingIcon=document.getElementById("SettingIcon");
var DeletingIcon=document.getElementById("DeleteIcon");
var PassIcon=document.getElementById("LockIcon")



function UserClick(){
    PersonalBtn.style.display="block";
    PaymentBtn.style.display="none";
    SubscribtionBtn.style.display="none";
    PrivacyBtn.style.display="none";
    SettingsBtn.style.display="none";
    DeletingBtn.style.display="none";
    LockBtn.style.display="none";


    PersonalIcon.style.color=("#103b67");
    CreditCardIcon.style.color=("white");
    TVIcon.style.color=("white");
    TasksIcon.style.color=("White");
    SettingIcon.style.color=("white");
    DeletingIcon.style.color=("White");
    PassIcon.style.color=("White");
    DeletingIcon.style.fontSize=("20px");
    PassIcon.style.fontSize=("20px");

    PersonalIcon.style.fontSize=("30px");
    CreditCardIcon.style.fontSize=("20px");
    TVIcon.style.fontSize=("20px");
    TasksIcon.style.fontSize=("20px");
    SettingIcon.style.fontSize=("20px");
};

function CreditCardClick(){
    PersonalBtn.style.display="none";
    PaymentBtn.style.display="block";
    SubscribtionBtn.style.display="none";
    PrivacyBtn.style.display="none";
    SettingsBtn.style.display="none";
    DeletingBtn.style.display="none";
    LockBtn.style.display="none";

    PersonalIcon.style.color=("white");
    CreditCardIcon.style.color=("#103b67");
    TVIcon.style.color=("white");
    TasksIcon.style.color=("White");
    SettingIcon.style.color=("white");
    DeletingIcon.style.color=("White");
    PassIcon.style.color=("White");
    DeletingIcon.style.fontSize=("20px");
    PassIcon.style.fontSize=("20px");
    PersonalIcon.style.fontSize=("20px");
    CreditCardIcon.style.fontSize=("30px");
    TVIcon.style.fontSize=("20px");
    TasksIcon.style.fontSize=("20px");
    SettingIcon.style.fontSize=("20px");
};

function TVclick(){
    PersonalBtn.style.display="none";
    PaymentBtn.style.display="none";
    SubscribtionBtn.style.display="block";
    PrivacyBtn.style.display="none";
    SettingsBtn.style.display="none";
    DeletingBtn.style.display="none";
    LockBtn.style.display="none";




    PersonalIcon.style.color=("white");
    CreditCardIcon.style.color=("white");
    TVIcon.style.color=("#103b67");
    TasksIcon.style.color=("White");
    SettingIcon.style.color=("white");
    DeletingIcon.style.color=("White");
    PassIcon.style.color=("White");
    DeletingIcon.style.fontSize=("20px");
    PassIcon.style.fontSize=("20px");
    PersonalIcon.style.fontSize=("20px");
    CreditCardIcon.style.fontSize=("20px");
    TVIcon.style.fontSize=("30px");
    TasksIcon.style.fontSize=("20px");
    SettingIcon.style.fontSize=("20px");
};

function TasksClick(){
    PersonalBtn.style.display="none";
    PaymentBtn.style.display="none";
    SubscribtionBtn.style.display="none";
    PrivacyBtn.style.display="block";
    SettingsBtn.style.display="none";
    DeletingBtn.style.display="none";
    LockBtn.style.display="none";




    PersonalIcon.style.color=("white");
    CreditCardIcon.style.color=("white");
    TVIcon.style.color=("white");
    TasksIcon.style.color=("#103b67");
    SettingIcon.style.color=("white");
    DeletingIcon.style.color=("White");
    PassIcon.style.color=("White");
    DeletingIcon.style.fontSize=("20px");
    PassIcon.style.fontSize=("20px");
    PersonalIcon.style.fontSize=("20px");
    CreditCardIcon.style.fontSize=("20px");
    TVIcon.style.fontSize=("20px");
    TasksIcon.style.fontSize=("30px");
    SettingIcon.style.fontSize=("20px");
};

function SettingClick(){
    PersonalBtn.style.display="none";
    PaymentBtn.style.display="none";
    SubscribtionBtn.style.display="none";
    PrivacyBtn.style.display="none";
    SettingsBtn.style.display="block";
    DeletingBtn.style.display="none";
    LockBtn.style.display="none";
    PersonalIcon.style.color=("white");
    CreditCardIcon.style.color=("white");
    TVIcon.style.color=("white");
    TasksIcon.style.color=("White");
    SettingIcon.style.color=("#103b67");
    DeletingIcon.style.color=("White");
    PassIcon.style.color=("White");
    DeletingIcon.style.fontSize=("20px");
    PassIcon.style.fontSize=("20px");
    PersonalIcon.style.fontSize=("20px");
    CreditCardIcon.style.fontSize=("20px");
    TVIcon.style.fontSize=("20px");
    TasksIcon.style.fontSize=("20px");
    SettingIcon.style.fontSize=("30px");
};

function DeletingClick(){
    PersonalBtn.style.display="none";
    PaymentBtn.style.display="none";
    SubscribtionBtn.style.display="none";
    PrivacyBtn.style.display="none";
    SettingsBtn.style.display="none";
    DeletingBtn.style.display="block";
    LockBtn.style.display="none";
    PersonalIcon.style.color=("white");
    CreditCardIcon.style.color=("white");
    TVIcon.style.color=("white");
    TasksIcon.style.color=("White");
    SettingIcon.style.color=("white");
    DeletingIcon.style.color=("#103b67");
    PassIcon.style.color=("White");
    DeletingIcon.style.fontSize=("30px");
    PassIcon.style.fontSize=("20px");
    PersonalIcon.style.fontSize=("20px");
    CreditCardIcon.style.fontSize=("20px");
    TVIcon.style.fontSize=("20px");
    TasksIcon.style.fontSize=("20px");
    SettingIcon.style.fontSize=("20px");
}

function PassClick(){
    PersonalBtn.style.display="none";
    PaymentBtn.style.display="none";
    SubscribtionBtn.style.display="none";
    PrivacyBtn.style.display="none";
    SettingsBtn.style.display="none";
    DeletingBtn.style.display="none";
    LockBtn.style.display="block";
    PersonalIcon.style.color=("white");
    CreditCardIcon.style.color=("white");
    TVIcon.style.color=("white");
    TasksIcon.style.color=("White");
    SettingIcon.style.color=("white");
    DeletingIcon.style.color=("white");
    PassIcon.style.color=("#103b67");
    DeletingIcon.style.fontSize=("20px");
    PassIcon.style.fontSize=("30px");
    PersonalIcon.style.fontSize=("20px");
    CreditCardIcon.style.fontSize=("20px");
    TVIcon.style.fontSize=("20px");
    TasksIcon.style.fontSize=("20px");
    SettingIcon.style.fontSize=("20px");
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