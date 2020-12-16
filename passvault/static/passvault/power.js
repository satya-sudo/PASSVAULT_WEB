document.addEventListener('DOMContentLoaded',() =>{
    try{
        document.querySelector('.form-login').addEventListener('submit',()=>checkForm());
    } catch (e){
        console.log(e)
    }
    
});

function checkForm(){
    event.preventDefault();
    let formToCheck = document.forms[0];
    if (formToCheck.name === 'register-form'){
        let username = formToCheck['username'];
        let email = formToCheck['email'];
        let password = formToCheck['password'];
        let confirmPassword = formToCheck['confirm'];

        if (username.value === '' || username.value.length < 8){
            window.alert("Username must be atleast 9 charactors long!!");
            username.focus();
            return false;
        }
        if (email.value === '' || !(email.value.includes('@') && email.value.includes('.com'))){
            window.alert("Please provide a valid email");
            email.focus();
            return false;
        }
        if (password.value.length < 10){
            window.alert("password must be longer than 10 characters!!");
            password.focus();
            return false;
        }if (confirmPassword.value !== password.value){
            window.alert("Passwords Don't match!");
            email.focus();
            return false;
        }
        formToCheck.submit();
        return true;

    } else if (formToCheck.name === 'login-form'){
        let username = formToCheck['username'];
        let password = formToCheck['password'];

        if (username.value === ''){
            window.alert("Please enter a username");
            username.focus();
            return false;
        }
        
        if (password.value === ""){
            window.alert("Please enter a password!");
            password.focus();
            return false;
        }
        formToCheck.submit();
        return true;
    } else if (formToCheck.name === 'NewCred-form'){
        let Sitename = formToCheck['Sitename'];
        let siteusername = formToCheck['siteusername'];

        let password = formToCheck['password'];

        if (Sitename.value === ''){
            window.alert("Please enter a Sitename");
            username.focus();
            return false;
        }
        
        if (siteusername.value === ""){
            window.alert("Please enter a siteusername!");
            password.focus();
            return false;
        }
        if (password.value === ""){
            window.alert("Please enter a password!");
            password.focus();
            return false;
        }
        formToCheck.submit();
        return true;
    }  else if (formToCheck.name === 'Search-form'){
        let Searchquery = formToCheck['Searchquery']
        if (Searchquery.value === ''){
            window.alert("Please enter a Search Query")
            Searchquery.focus();
            console.log(Searchquery.value)
            return false;
        }
        console.log(Searchquery.value)
        formToCheck.submit();
        return true;
    } else {
        formToCheck.submit();
        return true;
    }
}
