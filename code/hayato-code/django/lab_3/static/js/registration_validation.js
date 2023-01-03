$(document).ready(function () {
  const EMAIL = document.forms["sign-up-form"]["email"];
  const PASSWORD = document.forms["sign-up-form"]["password1"];
  const EMAIL_ERROR = document.getElementById("email_error");
  const PASSWORD_ERROR = document.getElementById("password_error1");
  const PASSWORD_ERROR_TWO = document.getElementById("password_error2");

  // validation email
  function ValidateEmail(email) {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
      return true;
    }
    return false;
  }

  $("#id_email").on("keyup", function () {
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

  // function to verify password 1
  $("#id_password1").on("keyup", function () {
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
  });

  // function to verify second password
  $("#id_password2").on("keyup", function () {
    if ($("#id_password2").val() === $("#id_password1").val()) {
      this.style.border = "1px solid green";
      PASSWORD_ERROR_TWO.innerHTML = "";
      return true;
    } else {
      this.style.border = "1px solid red";
      PASSWORD_ERROR_TWO.innerHTML = "the two passwords do not match";
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

  function check_if_password_is_valid(password1, password2) {
    if (
      password2 === password1 &&
      password2.match(/^[0-9a-zA-Z@!#$%*]+$/) &&
      password2.length > 7
    ) {
      return true;
    } else {
      return false;
    }
  }

  $("#sign-up-form").submit(function (e) {
    if (
      !check_if_email_is_valid(EMAIL.value) &&
      !check_if_password_is_valid(
        $("#id_password1").val(),
        $("#id_password2").val()
      )
    ) {
      e.preventDefault();
    }
  });
});
