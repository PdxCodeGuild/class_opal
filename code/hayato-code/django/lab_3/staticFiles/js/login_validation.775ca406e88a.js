$(document).ready(function () {
  const EMAIL = document.forms["login-form"]["username"];
  const PASSWORD = document.forms["login-form"]["password"];
  const EMAIL_ERROR = document.getElementById("email_error");
  const PASSWORD_ERROR = document.getElementById("password_error");

  // validation if email is valid
  function ValidateEmail(email) {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
      return true;
    }
    return false;
  }

  $("#id_username").on("keyup", function () {
    if (ValidateEmail(EMAIL.value)) {
      this.style.border = "1px solid green";
      EMAIL_ERROR.textContent = "";
      return true;
    } else {
      this.style.border = "1px solid red";
      EMAIL_ERROR.textContent = "invalid email";
      this.focus();
      return false;
    }
  });

  function check_if_email_is_valid(email) {
    if (ValidateEmail(email)) {
      return true;
    } else {
      return false;
    }
  }

  //validating if passoword is valid
  // function to verify passowrd
  $("#id_password").on("keyup", function () {
    if (PASSWORD.value.length >= 1) {
      if (PASSWORD.value.match(/^[0-9a-zA-Z@!#$%*]+$/)) {
        if (PASSWORD.value.length < 8) {
          PASSWORD.style.border = "1px solid red";
          PASSWORD_ERROR.textContent = "password too short";
          PASSWORD.focus();

          return false;
        } else {
          PASSWORD.style.border = "1px solid green";
          PASSWORD_ERROR.innerHTML = "";

          return true;
        }
      } else {
        PASSWORD.style.border = "1px solid red";
        PASSWORD_ERROR.textContent = "invalid characters in password";
        PASSWORD.focus();

        return false;
      }
    } else {
      PASSWORD.style.border = "1px solid red";
      PASSWORD_ERROR.textContent = "password is required";
      PASSWORD.focus();
      return false;
    }
  });

  function check_if_password_is_valid(password) {
    if (password.match(/^[0-9a-zA-Z@!#$%*]+$/) && password.length > 7) {
      return true;
    } else {
      return false;
    }
  }
  //on submit

  $("#login-form").submit(function (e) {
    if (
      !check_if_email_is_valid(EMAIL.value) &&
      !check_if_password_is_valid(PASSWORD.value)
    ) {
      e.preventDefault();
    }
  });
});
