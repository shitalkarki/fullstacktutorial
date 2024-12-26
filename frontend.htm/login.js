let myform = document.getElementById('form_register');
myform.addEventListener('submit', function (event) {
    // Prevent form submission
    event.preventDefault();
    let myUsername = document.getElementById('name');
    let mypassword = document.getElementById('password');
    let myaddress = document.getElementById('address');
    let mycontact = document.getElementById('contact');
    let myemail = document.getElementById('email');
    console.log(myUsername.value);
    console.log(mypassword.value);
    console.log(myaddress.value);
    console.log(mycontact.value);
    console.log(myemail.value);
})
