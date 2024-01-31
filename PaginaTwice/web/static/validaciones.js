function login() {

    event.preventDefault()
    var usuario = document.getElementById('exampleInputUsername').value;
    var password = document.getElementById('exampleInputPassword').value;
    
    alert("Usuario: " + usuario + ", Contraseña: " + password);
    console.log("Mensaje desde la consola:", "Datos de inicio de sesión:", usuario, password);
    console.log("Usuario: "+usuario+", Password: "+password);
  }
  