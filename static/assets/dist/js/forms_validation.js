function validateFormEmployee() {
    let x = document.forms["employee_form"]["primeiro_nome"].value;
    if (x == "") {
      alert("Name must be filled out");
      return false;
    }
  }